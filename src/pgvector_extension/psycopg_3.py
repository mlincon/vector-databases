import math
import os

import psycopg
from pgvector.psycopg import register_vector
from psycopg import sql


def get_db_connection_string() -> str:
    """Generates the connection string for postgres database

    Returns:
        str: the connection string
    """
    HOST = os.environ["POSTGRES_HOST"]
    PORT = os.environ["POSTGRES_PORT"]
    USER = os.environ["POSTGRES_USER"]
    PASSWORD = os.environ["POSTGRES_PASSWORD"]
    DB_NAME = os.environ["POSTGRES_DB_NAME"]

    return f"dbname={DB_NAME} user={USER} host={HOST} password={PASSWORD} port={PORT}"


def execute_search_query(query, values: tuple) -> list:
    """Returns search result for a query. Note this function opens a connection
    with the database and closes after execution.

    Args:
        query: the query to be executed
        values (tuple): any parameter values

    Returns:
        list of row objects
    """
    with psycopg.connect(get_db_connection_string()) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute(query, values)
            return cur.fetchall()


def execute_insert_query(query, values: list[tuple]):
    """Execute insert in database

    Args:
        query: the query to be executed
        values (tuple): any parameter values
    """
    with psycopg.connect(get_db_connection_string()) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.executemany(query, values)
            conn.commit()


def create_ivfflat_index(schema: str, table: str, index_col: str):
    """Create IVFFlat index after inserting data

    Args:
        table: name of the table to create the index
    """
    with psycopg.connect(get_db_connection_string()) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            # get number of records for setting index parameters
            count_query = sql.SQL("SELECT COUNT(*) as cnt FROM {0}.{1}").format(
                sql.Identifier(schema), sql.Identifier(table)
            )
            cur.execute(count_query)
            num_records = cur.fetchone()
            if num_records is not None:
                num_records = num_records[0]
                # calculate the index parameters according to best practices
                num_lists = num_records / 1000
                num_lists: int
                if num_lists < 10:
                    num_lists = 10
                if num_records > 1000000:
                    num_lists = int(math.sqrt(num_records))
            else:
                raise ValueError("Cannot create index")

            index_query = sql.SQL(
                "CREATE INDEX ON {0}.{1} USING ivfflat ({2} vector_cosine_ops) "
                + " WITH (lists = {3});"
            ).format(
                sql.Identifier(schema),
                sql.Identifier(table),
                sql.Identifier(index_col),
                sql.Identifier(str(num_lists)),
            )
            cur.execute(index_query)
            conn.commit()
