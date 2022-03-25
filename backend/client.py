"""
Connect to the mysql database
"""
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """Create a mysql connection."""
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as err:
        print(f"The error '{err}' occurred")
    return connection


def query_database(connection, query):
    """Query the database"""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print(f"Database successfully with following command: {query}")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("my-simple-scalable-server_db_1", "root", "example", "")
query_database(connection, "DROP DATABASE IF EXISTS sm_app")
query_database(connection, "CREATE DATABASE sm_app")
connection = create_connection("my-simple-scalable-server_db_1", "root", "example", "sm_app")