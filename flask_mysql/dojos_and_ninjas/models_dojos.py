# #methods
# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the table from our database
class Dojos:
    def __init__(self, data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas_db').query_db(query)
        # Create an empty list to append our instances of the table
        dojos = []
        # Iterate over the db results and create instances of table with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

