from flask import Flask, render_template, request, redirect
from users import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/user/new')
def new():
    return render_template("index.html")

@app.route('/users')
def user_list():
    users = Users.get_all()
    return render_template('index2.html', users = users )

@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    Users.save(request.form)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True)