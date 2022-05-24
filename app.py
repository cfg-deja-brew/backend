from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from db_connection import DB_HOST, DB_USER, DB_PASS, DB_NAME
from twilio.rest import Client
import random
import json

app = Flask(__name__)
cors = CORS(app)
port = 4000

account_sid = 'ACb7f4ee561c5fda8544277315de007d1c' 
auth_token = '52f6114614e3040d598dea8c78605731' 
client = Client(account_sid, auth_token) 

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
    query = "SELECT * FROM CAFES WHERE City = %s"
    if request.args.get('VeganFriendly'):
        query += " WHERE VeganFriendly = TRUE"
    if request.args.get('Accessibility'):
        query += " WHERE Accessibility = TRUE"
    if request.args.get('DogFriendly'):
        query += " WHERE DogFriendly = TRUE"
    if request.args.get('WorkFriendly'):
        query += " WHERE WorkFriendly = TRUE"
    if request.args.get('Trendy'):
        query += " WHERE Trendy = TRUE"
    if request.args.get('Parking'):
        query += " WHERE Parking = TRUE"
    if request.args.get('DateFriendly'):
        query += " WHERE DateFriendly = TRUE"
    cursor.execute(query, [city])
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)


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

@app.post('/login')
def login():
    mobile = json.loads(request.data.decode()).get('mobile')
    code = json.loads(request.data.decode()).get('code')
    with connection.cursor(dictionary=True) as cursor:
        if code is None:
            cursor.execute("""SELECT * FROM USERS
                              WHERE Mobile = %s""", [mobile])
            if not cursor.fetchone():
                return jsonify({"data": "error"})
            code = str(random.randint(0, 999999))  # Generate a random 6-digit code
            cursor.execute("""INSERT INTO LOGIN_SESSIONS
                              (Mobile, Code)
                              VALUES
                              (%s, %s)""", [mobile, code])
            client.messages.create(from_='whatsapp:+14155238886',  
                                   body=f'Your one-time login code is {code}',      
                                   to=f'whatsapp:{mobile}')
            return jsonify({"data": "success"})
        else:
            cursor.execute("""SELECT SessionId FROM LOGIN_SESSIONS
                              WHERE Mobile = %s
                              AND Code = %s""", [mobile, code])
            result = cursor.fetchone()
            return jsonify({"data": result or "error"})


app.run(port=port)
