#!/usr/bin/python3

from flask import Flask, jsonify, request #type: ignore
from flask_httpauth import HTTPBasicAuth #type: ignore
from flask_jwt_extended import JWTManager, get_jwt_identity #type: ignore
from flask_jwt_extended import jwt_required, create_access_token #type: ignore
from werkzeug.security import generate_password_hash, check_password_hash #type: ignore

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'
jwt = JWTManager(app)

users = {
      "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/login', methods=['POST'])
@auth.login_required
def login():
    username = auth.current_user()
    token = create_access_token(identfy=username)
    return jsonify(access_token=token), 200


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

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
