from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

# Load JSON data
def load_json_data():
    with open("products.json", "r") as f:
        return json.load(f)["items"]  # must match JSON structure

# Load CSV data
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
    id_filter = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template("product_display.html", error="Wrong source")

    data = load_json_data() if source == "json" else load_csv_data()

    # Filter by id if provided
    if id_filter:
        try:
            id_filter = int(id_filter)
        except ValueError:
            return render_template("product_display.html", error="Invalid ID")

        data = [item for item in data if item["id"] == id_filter]
        if not data:
            return render_template("product_display.html", error="Product not found")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
