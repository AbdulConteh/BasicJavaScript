from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',row=8,col=8,color_one='red',color_two='black')

@app.route('/<int:x>')
def gameboard(x):
    return render_template('index.html',row=x,col=8,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>')
def gameboard_one(x,y):
    return render_template('index.html',row=x,col=y,color_one='blue',color_two='orange')

@app.route('/<int:x>/<int:y>/<string:one>')
def gameboard_two(x,y,one):
    return render_template('index.html',row=x,col=y,color_one=one,color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def gameboard_three(x,y,one,two):
    return render_template('index.html',row=x,col=y,color_one=one, color_two=two)

if __name__=="__main__":
    app.run(debug=True)