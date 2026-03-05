from flask import Flask, request, jsonify
from flask_cors import CORS
from database import users_collection, interactions_collection
from model import recommend_items

app = Flask(__name__)
CORS(app)

# -----------------------------
# USER REGISTRATION
# -----------------------------
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    if users_collection.find_one({"username": username}):
        return jsonify({"error": "User already exists"}), 400

    users_collection.insert_one({
        "username": username,
        "password": password
    })

    return jsonify({"message": "User registered successfully"})


# -----------------------------
# USER LOGIN
# -----------------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = users_collection.find_one({
        "username": username,
        "password": password
    })

    if user:
        return jsonify({
            "message": "Login successful",
            "user_id": str(user["_id"])
        })

    return jsonify({"error": "Invalid credentials"}), 401


# -----------------------------
# STORE USER INTERACTION
# -----------------------------
@app.route("/interaction", methods=["POST"])
def interaction():

    data = request.get_json()

    user_id = data.get("user_id")
    product_id = data.get("product_id")

    if not user_id or not product_id:
        return jsonify({"error": "Missing user_id or product_id"}), 400

    interactions_collection.insert_one({
        "user_id": user_id,
        "product_id": product_id
    })

    return jsonify({"message": "Interaction stored successfully"})


# -----------------------------
# RECOMMENDATION API
# -----------------------------
@app.route("/recommend", methods=["POST"])
def recommend():

    data = request.get_json()

    product_id = int(data.get("product_id"))

    recommendations = recommend_items(product_id)

    return jsonify({
        "recommended_products": recommendations
    })


# -----------------------------
# START SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)