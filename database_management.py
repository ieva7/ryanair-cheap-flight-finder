"""Methods to do with the database"""
import psycopg2
from dotenv import dotenv_values


def get_connected() -> None:
    """Connects to local psql database"""

    try:
        config = dotenv_values(""".env""")
        conn = psycopg2.connect(
        database = config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
        )
        return conn
    except psycopg2.DatabaseError:
        raise psycopg2.DatabaseError("Error connecting to database")
    

conn = get_connected()

def make_db(conn) -> None:
    """Makes the database"""

    with conn.cursor() as cur:
        conn.autocommit = True
        cur.execute("CREATE database flights;")

def make_tables(conn) -> None:

    with conn.cursor() as cur:
        sql_file = open('DDL.sql','r')
        cur.execute(sql_file.read())

make_tables(conn)
conn.close()