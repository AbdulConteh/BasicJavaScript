from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
db = 'dojo_survey_db'

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    @classmethod
    def save(cls, data):
        query = '''
        INSERT INTO dojos ( name, location, language, comment)
        VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s);
        '''
        return connectToMySQL(db).query_db(query,data)

    @classmethod
    def get_last_survey(cls):
        query = 'SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;'
        results = connectToMySQL(db).query_db(query)
        return Dojos(results[0])

    @staticmethod
    def is_valid(dojos):
        is_valid = True
        if len(dojos['name']) < 3:
            is_valid = False
            flash('Name must be 3 characters.')
        if len(dojos['location']) < 3:
            is_valid = False
            flash('Must be dojo location.')
        if len(dojos['language']) < 3:
            is_valid = False
            flash('Must choose favorite language.')
        if len(dojos['comment']) < 3:
            is_valid = False
            flash('Comments must be at least 5 characters')
        return is_valid