from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'pineapples'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forminfo', methods=['POST'])
def forminfo():
    session['name'] = request.form['name']
    session['dojo location'] = request.form['dojo location']
    session['fav lang'] = request.form['favorite language']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('index2.html')


if __name__=="__main__":
    app.run(debug=True)