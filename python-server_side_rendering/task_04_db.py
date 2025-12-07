#!/usr/bin/python3
"""
Flask app that displays products from JSON, CSV, or SQLite database.
Use query parameter 'source' to select the data source:
- ?source=json
- ?source=csv
- ?source=sql
"""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# ---------- JSON data loader ----------
def load_json_data():
    try:
        with open("products.json", "r") as f:
            return json.load(f)["items"]  # Ensure your JSON structure has "items"
    except Exception as e:
        print(f"JSON error: {e}")
        return []

# ---------- CSV data loader ----------
def load_csv_data():
    try:
        with open("products.csv", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception as e:
        print(f"CSV error: {e}")
        return []

# ---------- SQLite data loader ----------
def load_sql_data():
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        # Convert to list of dicts for template compatibility
        return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]
    except Exception as e:
        print(f"SQL error: {e}")
        return []

# ---------- Flask route ----------
@app.route("/products")
def products():
    source = request.args.get("source", "json").lower()
    if source == "json":
        data = load_json_data()
    elif source == "csv":
        data = load_csv_data()
    elif source == "sql":
        data = load_sql_data()
    else:
        return "Wrong source", 400
    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5252)
