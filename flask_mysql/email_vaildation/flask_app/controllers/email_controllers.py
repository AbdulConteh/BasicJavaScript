from flask_app import app
from flask import render_template, request, redirect 
from flask_app.models.email_models import Email


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/access', methods=['POST'])
def create_email():
    Email.save(request.form)
    if not Email.validate_email(request.form):
        return redirect('/results')
    data = {
        "email" : request.form["email"]
    }
    print(data['email'])
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("info.html", e = Email.get_all())

