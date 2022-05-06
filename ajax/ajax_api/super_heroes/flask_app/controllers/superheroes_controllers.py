from flask_app import app
import requests
import os
from flask import jsonify
from flask import redirect, render_template, request

@app.route('/')
def index():
    return render_template('index.html`')

@app.route('/search', methods=['POST'])
def search():
    print(requests.form['query'])
    r = requests.get(f"https://superheroapi.com/api/id{os.environ.get('FLASK_API_KEY')}/search?
    ={request.form['query']}")
    return jsonify( r.json() )
