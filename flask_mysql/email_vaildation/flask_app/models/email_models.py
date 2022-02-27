from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db = "email_validation_db"
    def __init__(self, data):
        self.id = data['id'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = " INSERT INTO email (email) VALUES ( %(email)s )"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = " SELECT * FROM email "
        result = connectToMySQL(cls.db).query_db(query)
        emails = []
        for row in result:
            emails.append (cls (row))
        return emails

    @staticmethod
    def validate_email(email):
        is_valid = True 
        query = "SELECT * FROM email WHERE email = %(email)s"
        results = connectToMySQL(Email.db).query_db(query, email)
        if len(results) >= 1:
            flash("Email alredy taken")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email was entered incorrectly. Please try again!")
            is_valid = False 
        return is_valid

