from flask import Flask, render_template, redirect, request
from models_ninjas import Ninjas
from models_dojos import Dojos


app = Flask(__name__)

@app.route('/dojos')
def index():
    dojos = Dojos.get_all()
    return render_template('index.html', dojos = dojos)

@app.route('/ninjas')
def ninjas():
    return render_template('add_ninja.html')

@app.route('/create_ninjas', methods=["POST"])
def new():
    Ninjas.save(request.form)
    return redirect('/dojos')

@app.route('/dojo_list')
def dojo_list():
    # display info on page
    ninjas = Ninjas.get_all()
    return render_template('dojo_list.html', ninjas = ninjas)

if __name__ == "__main__":
    app.run(debug=True)

