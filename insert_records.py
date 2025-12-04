import psycopg2
from api_request import mock_fetch_data

def connect_to_db():
    print("Conectando ao database do PostgreSQL...")
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5000,
            dbname="db",
            user="db_user",
            password="db_password"
        )

        return conn

        print(conn)
    except psycopg2.Error as e:
        print(f"Conexão falhou {e}")
        raise

connect_to_db()

def create_table(conn):
    print("Criando tabela caso não exista...")
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE SCHEMA IF NOT EXISTS dev;
                       CREATE TABLE IF NOT EXISTS dev.dados_brutos (
                        id SERIAL PRIMARY KEY,
                        cidade TEXT,
                        temperatura FLOAT,
                        descricao_tempo TEXT,
                        velocidade_vento FLOAT,
                        tempo TIMESTAMP,
                        inserido_em TIMESTAMP DEFAULT NOW(),
                        utc_offset TEXT
                       )
        ''')
        conn.commit()
        print("Tabela criada.")
    except psycopg2.Error as e:
        print(f"Criação da tabela falhou: {e}")
    