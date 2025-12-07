from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """reads the JSON file and returns a list of dictionaries"""
    with open('products.json', 'r') as f:
        return json.load(f)


def read_csv():
    """reads the CSV file and returns a list of dictionaries"""
    products = []
    with open('products.csv', 'r') as f:
        # dictReader automatically uses the header row (id,name...) as keys
        reader = csv.DictReader(f)
        for row in reader:
            # CSV reads everything as strings. Convert ID to int to match JSON behavior
            row['id'] = int(row['id'])
            products.append(row)
    return products


@app.route('/products')
def products():
    # get Query Parameters
    source = request.args.get('source')
    p_id = request.args.get('id')

    products_list = []
    error_msg = None

    # input Validation (The "Allowlist")
    if source == 'json':
        products_list = read_json()
    elif source == 'csv':
        products_list = read_csv()
    else:
        # EDGE CASE: Invalid source
        return render_template('product_display.html', error_msg="Wrong source")

    # ID Filtering Logic
    if p_id:
        # filter the list to find the matching ID
        # it converts items to string for safe comparison
        filtered_products = [p for p in products_list if str(p['id']) == str(p_id)]

        if not filtered_products:
            # EDGE CASE: ID not found
            return render_template('product_display.html', error_msg="Product not found")

        products_list = filtered_products

    # render Success
    return render_template('product_display.html', products=products_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
