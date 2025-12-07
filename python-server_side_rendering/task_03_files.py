#!/usr/bin/env python3
"""
Flask app to display products from JSON or CSV files
"""

from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

def load_json_data():
    """Load products from JSON file"""
    with open("products.json") as f:
        return json.load(f)  # returns a list of products

def load_csv_data():
    """Load products from CSV file"""
    products = []
    with open("products.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert price to float, id to int
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route("/products")
def products():
    """Route to display products"""
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source", products=[])

    try:
        data = load_json_data() if source == "json" else load_csv_data()
    except Exception as e:
        return render_template("product_display.html", error=f"Error loading data: {e}", products=[])

    if product_id is not None:
        filtered = [p for p in data if p["id"] == product_id]
        if not filtered:
            return render_template("product_display.html", error="Product not found", products=[])
        data = filtered

    return render_template("product_display.html", error=None, products=data)

if __name__ == "__main__":
    app.run(debug=True)
