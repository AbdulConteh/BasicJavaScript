import re
from flask_app import app
from flask_app.models.messages_models import Message
from flask_app.models.users_models import User
from flask import  redirect, session, request

@app.route('/post_message', methods=['POST'])
def create_message():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    print(data)
    Message.save(data)
    return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id" : id
    }
    Message.destroy(data)
    return redirect('/dashboard')