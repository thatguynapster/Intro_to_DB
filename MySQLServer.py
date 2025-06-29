import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (adjust host/user/password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="@Alpha1994"  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: Could not connect to MySQL server.\n{e}")

    finally:
        # Close connections
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
