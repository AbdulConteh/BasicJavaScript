from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import models_books

class Authors:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.favorited_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorited_books = []

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM authors
        """
        author = connectToMySQL('books_db').query_db(query)
        authors = []
        for a in author:
            authors.append(cls(a))
        return authors

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO authors (name) VALUES (%(name)s);
        """
        return connectToMySQL('books_db').query_db(query, data)

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        a = []
        results = connectToMySQL('books_db').query_db(query,data)
        for row in results:
            a.append(cls(row))
        return a

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books_db').query_db(query,data)

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books_db').query_db(query,data)
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorited_books.append(models_books.Books(data))
        return author