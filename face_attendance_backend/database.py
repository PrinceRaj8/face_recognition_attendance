import os
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")  # Render से Database URL मिलेगा

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn

