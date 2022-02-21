from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL

class Authors:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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
    def get_one(cls, data):
        query = """
            SELECT * FROM authors WHERE id = {{data.id}}
        """
        author = connectToMySQL('books_db').query_db(query)
        print(author)
        return author
