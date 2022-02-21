# routes
from flask_app import app
from flask import render_template, redirect, request, render_template
from flask_app.models.models_books import Books

@app.route('/books')
def index():
    books = Books.get_all()
    return render_template('books.html', book = books)

