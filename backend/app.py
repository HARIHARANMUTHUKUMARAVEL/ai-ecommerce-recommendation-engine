from flask import Flask, request, jsonify
from flask_cors import CORS
from model import recommend_items

app = Flask(__name__)
CORS(app)

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()
    product_id = int(data["product_id"])

    if product_id not in recommend_items.__globals__['item_similarity_df'].columns:
        return jsonify({"recommended_products": [], "error": "Invalid Product ID"})

    recommendations = recommend_items(product_id)

    return jsonify({"recommended_products": recommendations})


if __name__ == "__main__":
    app.run(debug=True)
