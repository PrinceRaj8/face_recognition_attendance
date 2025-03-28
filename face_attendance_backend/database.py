import psycopg2

DATABASE_URL = "postgresql://your_user:your_password@your_host:your_port/your_db"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
