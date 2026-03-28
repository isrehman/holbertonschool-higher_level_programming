#!/usr/bin/python3
"""Module that implements API security with Basic Auth and JWT"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "supersecretkey"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

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


@auth.verify_password
def verify_password(username, password):
    """Verifies username and password for basic auth"""
    user = users.get(username)
    if user and check_password_hash(user.get('password'), password):
        return username
    return None


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing or invalid token errors"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token errors"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_data):
    """Handles expired token errors"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_data):
    """Handles revoked token errors"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_data):
    """Handles fresh token required errors"""
    return jsonify({"error": "Fresh token required"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Returns access granted message for basic auth"""
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """Authenticates user and returns a JWT token"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if not user or not check_password_hash(user.get('password'), password):
        return jsonify({"error": "Invalid credentials"}), 401
    token = create_access_token(
        identity={"username": username, "role": user.get('role')}
    )
    return jsonify({"access_token": token})


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """Returns access granted message for JWT auth"""
    return "JWT Auth: Access Granted"


@app.route('/admin-only')
@jwt_required()
def admin_only():
    """Returns access granted message for admin role only"""
    identity = get_jwt_identity()
    if identity.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
