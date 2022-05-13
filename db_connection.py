from mysql.connector import connect

DB_NAME = 'DEJA_BREW'
DB_HOST = 'localhost'

# Change these values according to your own local setup
DB_USER = 'root'
DB_PASS = 'password'


# Connect to the database
def get_db_connection():
    connection = connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME)
    return connection
