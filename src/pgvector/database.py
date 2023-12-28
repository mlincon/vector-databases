import os
import pgvector
import psycopg2
import psycopg
from psycopg2.extras import execute_values
from pgvector.psycopg import register_vector


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
