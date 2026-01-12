import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'alx_book_store'

def create_database():
    """Creates the alx_book_store database in MySQL server."""
    cnx = None
    cursor = None
    try:
        cnx = mysql.connector.connect(
            user='root',  
            password='Girama!@12A',  
            host='127.0.0.1'
        )
        cursor = cnx.cursor()

        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Alx_book_store}")
        print(f"Database '{Alx_book_store}' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Invalid username or password")
        else:
            print(f"Error connecting to DB: {err}")
    finally:
        if cursor:
            cursor.close()
        if cnx and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_database()
