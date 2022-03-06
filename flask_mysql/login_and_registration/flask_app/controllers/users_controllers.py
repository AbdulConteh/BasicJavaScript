from flask_app import app
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)
from flask_app.models.users_models import Users
from flask import render_template, request, redirect, session, flash

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/create", methods=['POST'])
def create():
    if not Users.validate_user(request.form):
        return redirect('/')
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "date_of_birth" : request.form["date_of_birth"],
        "email" : request.form["email"],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    print(data['password'])
    id = Users.save(data)
    session['users_id'] = id
    return redirect ('/')

@app.route("/login", methods=['POST'])
def register():
    user = Users.get_all_email(request.form)
    if not user:
        flash("Unregistered Email. Please try again", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid password. Please try again.", "login")
    session['users_id'] = user.id
    return redirect('/profile')

@app.route('/profile')
def profile():
    if 'users_id' not in session:
        return redirect ('/logout')
    data = {
        'id' : session['users_id']
    }
    print(Users.get_id(data))
    return render_template("accepted.html", user=Users.get_id(data))

@app.route('/logout')
def logout():
    session.clear()
    return redirect ('/')