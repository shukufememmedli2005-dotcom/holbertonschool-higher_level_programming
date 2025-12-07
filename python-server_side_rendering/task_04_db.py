from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def read_json():
    """reads from JSON file"""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def read_csv():
    """reads from CSV file"""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                products.append(row)
    except FileNotFoundError:
        return []
    return products


def read_sql():
    """reads from SQLite Database"""
    products = []
    try:
        # connect to the database
        conn = sqlite3.connect('products.db')

        # this allows us to access columns by name (row['name']) instead of index (row[1])
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()

        # convert database rows to a list of dictionaries
        for row in rows:
            products.append(dict(row))

        conn.close()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

    return products


@app.route('/products')
def products():
    # get Query Parameters
    source = request.args.get('source')
    p_id = request.args.get('id')

    products_list = []

    # input Validation (Allowlist)
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    elif source == 'sql':  # <--- NEW: Handle SQL source
        products_list = read_sql()
    else:
        return render_template('product_display.html', error_msg="Wrong source")

    # ID Filtering Logic
    if p_id:
        # We perform filtering in Python here for simplicity,
        # ensuring consistent behavior across JSON, CSV, and SQL.
        filtered_products = [p for p in products_list if str(p['id']) == str(p_id)]

        if not filtered_products:
            return render_template('product_display.html', error_msg="Product not found")

        products_list = filtered_products

    # render Template
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
