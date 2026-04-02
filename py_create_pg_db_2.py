import psycopg2
from psycopg2 import sql

def create_postgresql_database(db_name, user, password, host="127.0.0.1", port="5432"):
    conn = None
    try:
        # 1. Connect to the default 'postgres' database
        conn = psycopg2.connect(
            dbname="postgres",
            user=user,
            password=password,
            host=host,
            port=port
        )
        
        # 2. Set autocommit to True (Required for CREATE DATABASE)
        conn.autocommit = True
        
        # 3. Create a cursor and execute the command
        with conn.cursor() as cursor:
            # Use sql.Identifier to safely handle the database name and prevent SQL injection
            query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))
            cursor.execute(query)
            print(f"Database '{db_name}' created successfully.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while creating database: {error}")
    
    finally:
        # 4. Close the connection
        if conn:
            conn.close()

if __name__ == "__main__":
    # Replace with your actual PostgreSQL credentials
    create_postgresql_database(
        db_name="my_new_database",
        user="postgres",
        password="your_password"
    )
