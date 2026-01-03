import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'alx_book_store'

try:
    # Connect to the MySQL server
    conn = mysql.connector.connect(
        user='Alai-ne',
        password='',
        host='127.0.0.1' # Assuming local server
    )
    cursor = conn.cursor()
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

    cursor.execute(create_database_query)
    print(f"Database '{DB_NAME}' created successfully!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Error: Database does not exist.")
    else:
        print(f"Error connecting to the DB: {err}")

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'conn' in locals() and conn is not None and conn.is_connected():
        conn.close()

