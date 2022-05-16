from flask import Flask, request, jsonify
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

@app.get('/<city>')
def cafes(city):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM CAFES WHERE City='%s'"
    if request.args.get('VeganFriendly'):
        query += " WHERE VeganFriendly = TRUE"
    if request.args.get('DogFriendly'):
        query += " WHERE DogFriendly = TRUE"
    cursor.execute(query, [city])
    results = cursor.fetchall()
    cursor.close()
    response = jsonify(results)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


# get users by id - NOT CURRENTLY WORKING
@app.get('/users/<int:user_id>')
def get_user_by_id(user_id):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("""SELECT Id
                      FROM USERS
                      WHERE Id = %s""", [user_id])
    result = cursor.fetchone()
    cursor.close()
    response = jsonify(result)
    return response


app.run(port=port)








