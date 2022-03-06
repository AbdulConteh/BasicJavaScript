from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user_models import User
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirmpw' : request.form['confirmpw']
    }
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['pw_hash'] = pw_hash
    valid = User.create_user(data)
    if valid:
        results = User.create_user(data)
        return redirect(f'/results/{results}')
    return redirect('/')

@app.route('/results/<int:id>')
def get_one(id):
    data = {
        'id' : id
    }
    user = User.get_one(data)
    return render_template('results.html', user = user )