import re
from flask import flash
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
db = "private_wall_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM user "
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO user (first_name, last_name, email, password)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_account(cls, data):
        query = " SELECT * FROM user WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return User(results[0])

    @classmethod 
    def get_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_user( User):
        is_valid = True
        if len(User['first_name']) < 2:
            flash("First name must be atleast 2 characters. Please try again", "register")
            is_valid = False
        if len(User['last_name']) < 2:
            flash("Last name must be atleast 2 characters. Please try again", "register")
            is_valid = False
        if not EMAIL_REGEX.match(User['email']):
            flash("Invalid Email. Please try again!", "register")
            is_valid = False
        if len(User['password']) < 8:
            flash("Password must be atleast 8 characters. Please try again", "register")
            is_valid = False
        if User["password"] != User["cfw_password"]:
            flash("Password don't match. Please try again", "login")
            is_valid = False
        return is_valid

