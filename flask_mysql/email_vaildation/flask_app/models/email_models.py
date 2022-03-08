from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
db = "email_validation_db"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id'],
        self.email = data['email'],
        self.created_at = data['created_at'],
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = " INSERT INTO email (email) VALUES ( %(email)s )"
        result = connectToMySQL(db).query_db(query, data)
        return result

    @classmethod
    def get_all(cls):
        query = " SELECT * FROM email "
        result = connectToMySQL(db).query_db(query)
        emails = []
        for row in result:
            emails.append (cls (row))
        return emails

    @classmethod
    def delete(cls):
        query = "DELETE * FROM email WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query)
        return results

    @staticmethod
    def validate_email(email):
        is_valid = True 
        query = "SELECT * FROM email WHERE email = %(email)s;"
        results = connectToMySQL(db).query_db(query, email)
        if len(results) >= 1:
            flash("Email alredy taken!")
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("Email was entered incorrectly. Please try again!")
            is_valid = False 
        return is_valid

