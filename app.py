from flask import Flask, request, jsonify
import os

app = Flask(__name__)

APP_ENV = os.getenv("APP_ENV", "DEV")
DB_HOST = os.getenv("DB_HOST", "localhost")
APP_PORT = int(os.getenv("APP_PORT", "5000"))

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 25000
    }
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "environment": APP_ENV
    })


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(new_product)

    return jsonify(new_product), 201


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    for product in products:
        if product["id"] == product_id:
            product["name"] = data["name"]
            product["price"] = data["price"]
            return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return jsonify({"message": "Product deleted"})

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)