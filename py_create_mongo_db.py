from pymongo import MongoClient

# 1. Connect to your MongoDB instance
# Replace 'localhost' with your MongoDB Atlas connection string if using the cloud
client = MongoClient('mongodb://localhost:27017/')

# 2. Define the database (it won't exist on the server yet)
db = client['my_new_database']

# 3. Define a collection
collection = db['my_collection']

# 4. Trigger creation by inserting a document
document = {"name": "example", "type": "test"}
collection.insert_one(document)

print("Database and collection created!")
