import psycopg2


def get_connection(dbname):
    connection = psycopg2.connect(
        dbname=dbname,
        host='127.0.0.1',
        user='postgres',
        password='1234'
    )
    return connection
