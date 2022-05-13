from flask import Flask, jsonify
import mysql.connector
from db_connection import DB_HOST, DB_USER, DB_PASS, DB_NAME

app = Flask(__name__)
port = 5000

#Below are manual db retrieval tests - I have started creating functions in separate files - see cafe and user management

connection = mysql.connector.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
)


@app.get('/')
def hello_world():
    return("hello world")

@app.get('/leicester')
def leicester_cafes():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CAFES WHERE City='Leicester'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

@app.get('/nottingham')
def nottingham_cafes():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CAFES WHERE City='Nottingham'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

@app.get('/derby')
def derby_cafes():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CAFES WHERE City='Derby'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

# gets the latitude and longitude for coffee shops in derby, for use with markers
@app.get('/derby/cafes')
def derby_cafes_location():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT Latitude, Longitude FROM CAFES WHERE City='Derby'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

# gets the latitude and longitude for coffee shops in leicester, for use with markers
@app.get('/leicester/cafes')
def leicester_cafes_location():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT Latitude, Longitude FROM CAFES WHERE City='Leicester'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)

# gets the latitude and longitude for coffee shops in nottingham, for use with markers
@app.get('/nottingham/cafes')
def nottingham_cafes_location():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT Latitude, Longitude FROM CAFES WHERE City='Nottingham'")
    result = cursor.fetchone()
    cursor.close()
    return jsonify(result)


# get users by id - NOT CURRENTLY WORKING
@app.get('/users/<int:user_id>')
def get_user_by_id(Id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT Id
                      FROM USERS
                      WHERE Id = %s""", [Id])
    result = cursor.fetchone()
    cursor.close()
    response = jsonify(result)
    return response


app.run(port=port)








