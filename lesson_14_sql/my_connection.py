from psycopg2 import connect
from psycopg2.extensions import connection


def get_connection(dbname) -> connection:
    conn: connection = connect(
        dbname=dbname,
        host='127.0.0.1',
        user='postgres',
        password='1234'
    )
    return conn
