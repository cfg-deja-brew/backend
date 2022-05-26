from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from db_connection import DB_HOST, DB_USER, DB_PASS, DB_NAME
from twilio.rest import Client
from config import twilio_account_sid, twilio_auth_token
import random
import json

app = Flask(__name__)
cors = CORS(app)
port = 4000

client = Client(twilio_account_sid, twilio_auth_token) 

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
    query = """SELECT * FROM CAFES
               JOIN CAFE_ATTRIBUTES ON Id = CafeId
               WHERE City = %s"""
    if request.args.get('veganFriendly') == 'true':
        query += " AND VeganFriendly = TRUE"
    if request.args.get('accessible') == 'true':
        query += " AND Accessible = TRUE"
    if request.args.get('dogFriendly') == 'true':
        query += " AND DogFriendly = TRUE"
    if request.args.get('workFriendly') == 'true':
        query += " AND WorkFriendly = TRUE"
    if request.args.get('trendy') == 'true':
        query += " AND Trendy = TRUE"
    if request.args.get('parking') == 'true':
        query += " AND Parking = TRUE"
    if request.args.get('dateFriendly') == 'true':
        query += " AND DateFriendly = TRUE"
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
