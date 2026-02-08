
from data import products

from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]

# Homepage route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"}), 200

# GET /products (optionally filter by category)
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")

    if category:
        category = category.strip().lower()
        filtered = [p for p in products if p["category"].lower() == category]
        return jsonify(filtered), 200

    return jsonify(products), 200

# GET /products/<id>
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)

    if product is None:
        return jsonify({"error": "Product not found"}), 404

    return jsonify(product), 200


if __name__ == "__main__":
    app.run(debug=True)
