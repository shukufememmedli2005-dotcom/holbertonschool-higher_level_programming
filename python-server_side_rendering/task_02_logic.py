from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route('/items')
def items():
    # 1. Read the data from the JSON file
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Extract the list from the dictionary key "items"
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Safety fallback if file is missing or broken
        items_list = []

    # 2. Render the template and pass the data
    # We pass 'items_list' (python variable) to the template as 'items'
    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
