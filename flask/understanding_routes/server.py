from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase = "hello", times = 5)

@app.route('/dojo')
def dojo():
    return "Dojo!"

# @app.route('/say/flask')
# def hi_flask():
#     return "Hi Flask"

# @app.route('/say/<name>')
# def michael(name):
#     return f"Hi {name()}!"

# @app.route('/say/<name>')
# def john(name):
#     return f"Hi {name()}!"

# @app.route('/repeat/<int:num>/<string:word')
# def hello(x):
#     return "Hello", str(x)

# @app.route('/repeat/<int: x/bye')
# def bye(x):
#     return "Bye", str(x)

# @app.route('/repeat/<int: x/dogs')
# def dogs(x):
#     return "Dogs", str(x)

# @app.route('/repeat/<int:num>/<string:word')
# def repeated_words(num, word):
#     output = ''

#     for i in range(0,num):
#         output += f"<p>{word}</p>"

#     return output

if __name__=="__main__":
    app.run(debug=True)  