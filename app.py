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

app.run(port=port)








