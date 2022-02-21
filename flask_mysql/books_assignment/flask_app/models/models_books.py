# methods
from flask_app.config.mysqlconnection import connectToMySQL

class Books:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books"
        book = connectToMySQL('books_db').query_db(query)
        books = []
        for b in book:
            books.append(cls(b))
        return books

    @classmethod
    def Insert_Book(cls):
        query = """
        INSERT INTO books (title, num_of_pages)
        VALUES (%(title)s, %(num_of_pages)s)
        """
        book = connectToMySQL('books_db').query_db(query)
        return book

    @classmethod
    def get_one(cls, data):
        query = """
            SELECT * FROM books WHERE id = {{data.id}}
        """
        book = connectToMySQL('books_db').query_db(query)
        return book