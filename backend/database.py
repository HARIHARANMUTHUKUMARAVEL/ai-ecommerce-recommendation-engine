from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["ecommerce_ai"]

users_collection = db["users"]
products_collection = db["products"]
interactions_collection = db["interactions"]