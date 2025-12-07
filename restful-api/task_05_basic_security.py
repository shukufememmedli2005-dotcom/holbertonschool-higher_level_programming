#!/usr/bin/python3
"""
API security and authentication techniques.
this module demonstrates Basic Auth, JWT Auth, and Role-Based Access Control
"""
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()  # For Basic Auth

# configuration for JWT
# Change this in production
app.config['JWT_SECRET_KEY'] = 'your-strong-secret-key'
jwt = JWTManager(app)

# --- USER DATA STORAGE ---
# storing passwords as hashes, never plain text
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# --- BASIC AUTH HANDLERS ---

@auth.verify_password
def verify_password(username, password):
    """
    callback for Basic Auth to verify username and password.
    returns the username if valid, otherwise None.
    """
    if username in users:
        # Check the hashed password
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    route protected by Basic Authentication.
    """
    return "Basic Auth: Access Granted"


# --- JWT AUTH HANDLERS ---

@app.route('/login', methods=['POST'])
def login():
    """
    route to authenticate user and return a JWT token.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    # validate credentials
    if username in users and \
            check_password_hash(users[username]["password"], password):
        # Embed role in the token for RBAC
        role = users[username]["role"]

        # generate the token (identity identifies the user)
        # it can add additional claims (like role) to the token
        access_token = create_access_token(identity={"username": username, "role": role})
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    route protected by JWT Authentication.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """
    route protected by JWT and Role (Admin only).
    """
    # retrieve the identity embedded in the token
    current_user = get_jwt_identity()

    # check the role
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


# --- JWT ERROR HANDLERS (Required for the Checker) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
