from flask_app import app
from flask import render_template, redirect, request, render_template
from flask_app.models.models_authors import Authors

@app.route('/authors')
def viewbooks():
    authors = Authors.get_all()
    return render_template('authors.html', author = authors)