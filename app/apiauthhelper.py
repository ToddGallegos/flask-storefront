from flask import request
from .models import User

def token_auth_required(func):
    
    def decorated():
        #before
        data = request.json
        username = data['username']
        password = data['password']
        
        user = User.query.filter_by(username = username)
        if user:
            if user.password == password:
                func()
                return user.token
    return decorated

def basic_auth_required():
    pass