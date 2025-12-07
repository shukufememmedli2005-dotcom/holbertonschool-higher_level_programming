from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to read JSON data
def read_json(file_path):
    with open(file_path) as f:
        return json.load(f)

# Function to read CSV data
def read_csv(file_path):
    products = []
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert id to int and price to float for consistency
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_filter = request.args.get('id', type=int)
    
    if source not in ('json', 'csv'):
        return render_template('product_display.html', error="Wrong source", products=None)
    
    # Read data from the correct source
    if source == 'json':
        data = read_json('products.json')
    else:
        data = read_csv('products.csv')

    # Filter by id if provided
    if id_filter:
        filtered = [product for product in data if product["id"] == id_filter]
        if not filtered:
            return render_template('product_display.html', error="Product not found", products=None)
        data = filtered

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True)
