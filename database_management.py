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


def find_available_pairs(conn)


conn.close()