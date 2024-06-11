"""Methods to do with the database"""
import psycopg2
from psycopg2 import sql
from dotenv import dotenv_values
import pandas as pd


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

def populate_destination_pairs(conn) -> None:
    """Populates the destination_pairs table"""

    with conn.cursor() as cur:
        pairs = pd.read_csv("data.csv")
        pairs = set(pairs.itertuples(index=False, name=None))
        
        query = sql.SQL("""INSERT INTO destination_pairs (departure_airport, arrival_airport)
                        VALUES (%s,%s);""")
        cur.executemany(query, pairs)
        conn.commit()


def find_available_pairs(conn) -> set:
    """Finds available pairs, returns a set with the triples"""

    flight_pairs = set()
    with conn.cursor() as cur:
        cur.execute("""SELECT a.departure_airport, a.arrival_airport, b.arrival_airport 
                    FROM flight_info.destination_pairs a LEFT JOIN flight_info.destination_pairs b
                    ON a.arrival_airport = b.departure_airport;""")
        results = cur.fetchall()
        print(results)

conn.close()