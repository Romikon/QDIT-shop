# DB config
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = None
try:
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
        host = os.getenv('DB_HOST'),
        dbname = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER_NAME'),
        password = os.getenv('DB_USER_PASSWORD'),
        port = os.getenv('DB_PORT'),
    )
    cur = conn.cursor()
    print('Connected to the PostgreSQL database')
    cur.execute('SELECT version()')

except(Exception, psycopg2.DatabaseError) as error:
    print(f"[Database connection error] something went wrong while connecting to the PostgreSQL database!")
    exit()