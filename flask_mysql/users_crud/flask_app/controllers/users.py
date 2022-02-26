from flask import render_template,redirect,request
from flask_app import app

from flask_app.models.user import Users

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/user/new')
def new():
    return render_template("new_user.html")

@app.route('/users')
def user_list():
    users = Users.get_all()
    return render_template('index2.html', users = users )

@app.route('/create_user', methods=["POST"])
def create_user():
    Users.save(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:users_id>')
def destroy(users_id):
    data = {
        "id": users_id
    }
    Users.destroy(data)
    return redirect ('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user =Users.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show_user.html",user = Users.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    Users.update(request.form)
    return redirect('/users')
