from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.models_favorites import Favorites
from flask_app.models.models_authors import Authors

@app.route('/select_fav')
def fav():
    return render_template('select_fav.html')

@app.route('/authors/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("select_fav.html", author = Authors.get_one(data))