from typing import Optional
from psycopg2 import connect
from psycopg2.extensions import connection


class ConnectionDB:
    DBNAME = "tms"
    HOST = "127.0.0.1"
    USER = "postgres"
    PASSWORD = "1234"
    __instance: Optional[connection] = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = connect(
                dbname=cls.DBNAME, host=cls.HOST, user=cls.USER, password=cls.PASSWORD
            )
        return cls.__instance


# test Singleton
if __name__ == "__main__":
    conn1 = ConnectionDB()
    conn2 = ConnectionDB()
    assert conn1 is conn2
