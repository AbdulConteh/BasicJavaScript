from flask_app import app
from flask import render_template, redirect, request, render_template
from flask_app.models.models_authors import Authors
from flask_app.models.models_books import Books

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def viewbooks():
    return render_template('authors.html', a = Authors.get_all())

@app.route('/add/authors', methods=['POST'])
def add_author():
    data = {
        "name": request.form['name']
    }
    a = Authors.save(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def show_author(id):
    data = {
        "id": id
    }
    return render_template('show_fav_authors.html',author=Authors.get_by_id(data),unfavorited_books=Books.unfavorited_books(data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Authors.add_favorite(data)
    return redirect(f"/authors/<int:id>/{request.form['author_id']}")