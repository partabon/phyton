# let's import the flask

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import os
from bson.json_util import dumps
import pymongo
from datetime import datetime
import requests

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient()
db = client['thirty_days_of_python'] # accessing the database

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(students), mimetype='application/json')

@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = requests.form['name']
    country = requests.form['country']
    city = requests.form['city']
    skills = requests.form['skills'].split(', ')
    bio = requests.form['bio']
    birthyear = requests.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return 

def update_student (id):
    if __name__ == '__main__':
    # for deployment
    # to make it work for both production and development
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=True, host='0.0.0.0', port=port)