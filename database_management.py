import psycopg2
from dotenv import dotenv_values


def get_connected() -> None:
    """Creates a museum database.
    WARNING: will drop existing 'museum' database"""

    try:
        config = dotenv_values(""".env""")
        conn = psycopg2.connect(
        database = config['database'],
        user=config['user'],
        password=config['password'],
        host=config['host']
        )
        return conn
    except psycopg2.DatabaseError:
        raise psycopg2.DatabaseError("Error connecting to database")