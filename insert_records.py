import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Conectando ao database do PostgreSQL...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname="db"
            user="db_user",
            password="db_passsword"
        )

        print(conn)
    except: psycopg2.Error as e:
        print(f"Conexão falhou {e}")
        raise

connect_to_db()

