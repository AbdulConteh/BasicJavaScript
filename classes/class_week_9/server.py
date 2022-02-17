from flask import Flask, request, render_template, redirect
from friend import Friend
app = Flask(__name__)

@app.route('/')
def init():
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', friends=friends)

# @app.route('/')
# def init():
# return render_template('index.html', friends=Friends.get_all())

if __name__ == "__main__":
    app.run(debug=True)