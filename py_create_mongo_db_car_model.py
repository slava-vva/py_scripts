from pymongo import MongoClient

# Connect to the local MongoDB instance (default port is 27017)
# For a cloud database, use your [MongoDB Atlas](https://mongodb.com) connection string.
client = MongoClient("mongodb://localhost:27017/")

# Create (or access) a database named 'car_dealership'
db = client["car_dealership"]

# Create (or access) a collection named 'cars'
cars_collection = db["cars"]
