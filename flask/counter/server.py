from flask import Flask, render_template, session, redirect

app = Flask(__name__)

app.secret_key = "key of secrets!"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template("index.html")

@app.route('/')
def add2():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 2
    return render_template("index3.html")

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/counter')
def counter():
    return render_template('index2.html')

if __name__=="__main__":
    app.run(debug=True)