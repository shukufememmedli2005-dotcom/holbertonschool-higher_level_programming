from flask import Flask, render_template

app = Flask(__name__)

# Route for the Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    # Run the app on port 5000 with debugging enabled
    app.run(debug=True, port=5000)
