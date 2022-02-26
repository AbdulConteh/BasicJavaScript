# routes
from flask_app import app
from flask import render_template, redirect, request, render_template
from flask_app.models.models_books import Books
from flask_app.models.models_authors import Authors

@app.route('/')
def start():
    return redirect('/books')

@app.route('/books')
def show():
    books = Books.get_all()
    return render_template('books.html', book = books)

@app.route('/add/books', methods=['POST'])
def add_book():
    data = {
        "title": request.form['title'],
        "num_of_pages": request.form["num_of_pages"]
    }
    b = Books.save(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_books(id):
    data = {
        "id":id
    }
    return render_template('show_fav_book.html',book=Books.get_by_id(data),unfavorited_authors=Authors.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Authors.add_favorite(data)
    return redirect(f"/books/{request.form['book_id']}")
