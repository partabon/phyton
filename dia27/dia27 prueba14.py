# let's import the flask
from pymongo.mongo_client import MongoClient
from flask import Flask, render_template
import os # importing operating system module
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = MongoClient()
db = client['thirty_days_of_python'] # accessing the database

query = {'name':'John'}

db.students.delete_one(query)

for student in db.students.find():
    print(student)


