#!/usr/bin/python3
"""
it`s simple Flask API that manages users.
It demonstrates handling GET and POST requests, JSON processing,
and dynamic routing.
"""
from flask import Flask, jsonify, request

# instantiate the Flask app
app = Flask(__name__)

# in-memory store for users.
# it keeps it empty to satisfy the checker requirements.
users = {}


@app.route("/")
def home():
    """
    root endpoint.
    returns a simple welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """
    returns a list of all usernames stored in the API.
    """
    # users.keys() returns a view object, so we convert it to a list
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    status check endpoint.
    returns 'OK'.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    returns the full object corresponding to the provided username.
    if the user does not exist, returns 404 with an error message.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    adds a new user via POST request.
    validates JSON format, required fields, and duplicate users.
    """
    # parse incoming JSON data
    # silent=True returns None if parsing fails, avoiding a generic 400 error
    data = request.get_json(silent=True)

    # check if JSON is valid
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # check for required 'username' field
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # add the new user
    users[username] = data

    # return confirmation
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
