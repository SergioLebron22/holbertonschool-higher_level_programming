#!/usr/bin/python3

from flask import Flask, jsonify, request #type: ignore

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
    user = users.get(username)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    name = data.get("name")
    age = data.get("age")
    city = data.get("city")

    if not username or not name or not age or not city:
        return jsonify({"error": "Username, name, age, city are requierd"}), 400
    
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({"message": "User added", "user": users[username]})
    

if __name__ == "__main__":
    app.run()