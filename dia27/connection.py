from pymongo import MongoClient

MONGO_URI = "mongodb+srv://luis:Zjm5ufzWKVmRVrqv@cluster0.rdhcqr5.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
for db_name in client.list_database_names():
    print(db_name)