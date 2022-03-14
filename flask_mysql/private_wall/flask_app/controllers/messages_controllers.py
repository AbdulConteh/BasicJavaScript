import re
from flask_app import app
from flask_app.models.messages_models import Message
from flask_app.models.users_models import User
from flask import  redirect, session, request

@app.route('/create/message', methods=['POST'])
def create_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content'],
    }
    Message.save(data)
    return redirect('/dashboard')

@app.route('/delete/message/<int:id>')
def delete(id):
    data = {
        "id" : id
    }
    Message.delete(data)
    return redirect('/dashboard')