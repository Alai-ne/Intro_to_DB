import mysql.connector
from mysql.connector import errorcode

def create_database():
    """Creates the alx_book_store database if it doesn't exist."""
    config = {
        'user': 'root',
        'password': '',
        'host': '127.0.0.1',
        'raise_on_warnings': True
    }

    cnx = None
    cursor = None
    DB_NAME = 'alx_book_store'

    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        print("Connected to MySQL server successfully!")

        create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
        cursor.execute(create_db_query)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error connecting to the DB: {err}")
    finally:
        if cursor:
            cursor.close()
        if cnx:
            cnx.close()
            print("Database connection clsed")
