import os
import psycopg


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
        with conn.cursor() as curr:
            curr.execute(query, values)
            return curr.fetchall()


def execute_insert_query(query, values: list[tuple]):
    """Execute insert in database

    Args:
        query: the query to be executed
        values (tuple): any parameter values
    """
    with psycopg.connect(get_db_connection_string()) as conn:
        with conn.cursor() as curr:
            curr.executemany(query, values)
            conn.commit()
