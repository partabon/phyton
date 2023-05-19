import pymongo

from pymongo import MongoClient
client = MongoClient()

uri = "mongodb+srv://avizat:Cuajimalpa7@cluster0.rdhcqr5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
#client = MongoClient(uri)


db = client.test_database

collection = db.test_collection

import datetime
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(db.list_collection_names())

import pprint
pprint.pprint(posts.find_one())

pprint.pprint(posts.find_one({"author": "Mike"}))

pprint.pprint(posts.find_one({"author": "Eliot"}))