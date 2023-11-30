import psycopg2

# Configurações do banco de dados
db_settings = {
    "user": "admin",
    "password": "admin",
    "host": "localhost",
    "port": "5432",
    "dbname": "postgres",  # Banco de dados "postgres" é necessário para criar outros bancos de dados
}

# Nome do banco de dados que você deseja criar
new_db_name = "api_crud"

try:
    # Conecte-se ao PostgreSQL
    connection = psycopg2.connect(**db_settings)
    cursor = connection.cursor()

    # Crie o novo banco de dados
    cursor.execute(f"CREATE DATABASE {new_db_name};")

    print(f"Banco de dados '{new_db_name}' criado com sucesso!")

except Exception as e:
    print(f"Ocorreu um erro: {e}")

finally:
    if 'connection' in locals():
        cursor.close()
        connection.close()
