import re
from flask_app import app
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
db = "login_and_registration_db" 
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Users:
    def __init__(self, data):
        self.id = data['id'],
        self.first_name_name = data['first_name'],
        self.last_name = data['last_name'],
        self.date_of_birth = data['date_of_birth'],
        self.email = data['email'],
        self.password = data['password']

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users ( first_name, last_name, date_of_birth, email, password )
        VALUE ( %(first_name)s, %(last_name)s, %(date_of_birth)s, %(email)s, %(password)s );
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod 
    def get_all_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod 
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @staticmethod
    def validate_user(Users):
        is_valid = True 
        query = " SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, Users)
        if len(results) >= 1:
            flash("Email already exists.", "register")
            is_valid = False
        if len(Users['first_name']) < 2:
            flash("First Name must be at least 2 characters. Please try again", "register")
            is_valid = False
        if len(Users['last_name']) < 2:
            flash("Last Name must be at least 2 characters. Please try again", "register")
            is_valid = False
        if not EMAIL_REGEX.match(Users['email']):
            flash("Invalid Email. Please try again!", "register")
            is_valid = False  
        if len(Users['password']) < 8:
            flash("Password must be  8 characters. Please try again!", "register")
            is_valid = False 
        if Users['password'] != Users["cfw_password"]:
            flash("Password do not match. Please try gain", "register")
            is_valid = False  
        return is_valid
