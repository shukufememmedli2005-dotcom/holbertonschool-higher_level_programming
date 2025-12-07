from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def load_json_data():
    with open("products.json", "r") as f:
        return json.load(f)

def load_csv_data():
    products = []
    with open("products.csv", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")

    # Wrong source check
    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source")

    # Load correct data source
    data = load_json_data()["items"] if source == "json" else load_csv_data()

    # If id provided → filter
    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        filtered = [p for p in data if p["id"] == product_id]

        if not filtered:
            return render_template("product_display.html", error="Product not found")

        data = filtered

    return render_template("product_display.html", products=data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
