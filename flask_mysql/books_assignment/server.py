from flask_app.controllers import controllers_books
from flask_app.controllers import controllers_authors
from flask_app.controllers import controllers_favorites
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)