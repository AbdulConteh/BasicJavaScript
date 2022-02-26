from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.survey_models import Dojos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_survey():
    if Dojos.is_valid(request.form):
        Dojos.save(request.data)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def result():
    return render_template('results.html', dojo = Dojos.get_last_survey())
