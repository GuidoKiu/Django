import psycopg2

try:
    connection = psycopg2.connect(
        # host="192.168.10.71",
        host = "192.168.10.19",
        port="5432",
        database="Data2",
        user="postgres",
        password="indocyber"
    )
    print("Connection to PostgreSQL server successful")
    connection.close()
except Exception as e:
    print(f"Connection to PostgreSQL server failed: {e}")
