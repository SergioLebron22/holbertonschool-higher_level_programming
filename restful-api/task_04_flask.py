#!/usr/bin/python3

from flask import Flask, jsonify, request, abort #type: ignore

app = Flask(__name__)
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
          "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    return jsonify(list(users.keys()))
    
@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user(username):

    if username not in users:
        jsonify({"error": "User not found"}), 404

    user = users[username]
    user[username] = username

    return jsonify(user)

    
@app.route('/add_user', methods=['POST'])
def add_user():
    if request.get_json is None:
        abort(400, "Not a json")
    
    data = request.get_json()
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    
    users[data["username"]] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }

    output = {
        "username": data["username"],
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201
    

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)