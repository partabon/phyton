# let's import the flask
from pymongo.mongo_client import MongoClient
from flask import Flask, render_template
import os # importing operating system module
uri = "mongodb+srv://avizat:eU7GoE3TJV8JICSs@cluster0.rdhcqr5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient()
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
