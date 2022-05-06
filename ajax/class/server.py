from urllib import response
from flask import Flask, render_template, request, redirect 
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_github', methods=["POST"])
def get_github():
    github = request.form["github"]
    url = f"https://api.github.com/users/"
    response = requests.get(url)
    print (response.json())
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)