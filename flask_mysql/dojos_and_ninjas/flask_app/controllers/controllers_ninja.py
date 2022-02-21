from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import models_dojos, models_ninjas

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html',dojos= models_dojos.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    models_ninjas.Ninja.save(request.form)
    return redirect('/dojos')