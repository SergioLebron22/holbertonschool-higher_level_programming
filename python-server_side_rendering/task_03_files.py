from flask import Flask, render_template
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html'), 200

@app.route('/about')
def about():
    return render_template('about.html'), 200

@app.route('/contact')
def contact():
    return render_template('contact.html'), 200

@app.route('/items')
def items():
    with open("items.json", 'r') as file:
        items = json.load(file)
    return render_template('items.html', items=items), 200

@app.route('/products')
def products():
    
    return render_template('product_display.html'), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)