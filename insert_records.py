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
    
    except psycopg2.Error as e:
        print(f"Conexão falhou {e}")
        raise

#connect_to_db()

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
        raise
    

def insert_records(conn, data):
    print("Inserindo dados no banco")

    try:
        tempo_clima = data['current']
        local = data['location']
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO dev.dados_brutos (
                       cidade,
                       temperatura,
                       descricao_tempo,
                       velocidade_vento,
                       tempo,
                       inserido_em,
                       utc_offset
                    ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        ''', (
                local['name'],
                tempo_clima['temperature'],
                tempo_clima['weather_descriptions'][0],
                tempo_clima['wind_speed'],
                local['localtime'],
                local['utc_offset']
        ))
        conn.commit()
        print("Dados inseridos com sucesso.")

    except psycopg2.Error as e:
        print(f"Erro ao inserir dados: {e}")
        raise


def main():
    try:
        data = mock_fetch_data()
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except psycopg2.Error as e:
        print(f"Ocorreu um erro no processo: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
            print("Conexão fechada")

main()