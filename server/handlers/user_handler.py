from flask_restful import Resource
from flask import request, g
from flask.ext.httpauth import HTTPBasicAuth
import functools
from flask import request

import json

auth = HTTPBasicAuth()

class UserHandler(Resource):

    def post(self):
        from server.models.user import User, db
        username = request.json.get('username')
        password = request.json.get('password')
        if username is None or password is None:
            return {"error": "Missing arguments"}
        if User.query.filter_by(username=username).first() is not None:
            return {"error": "Already existing user"}
        user = User(username=username)
        user.hash_password(password)
        db.session.add(user)
        db.session.commit()
        return {'username': user.username}

class TokenHandler(Resource):
    def get(self):
        # import pdb; pdb.set_trace()
        user = load_user(request.authorization)
        if user:
            token = user.generate_auth_token()
            return { 'token': token.decode('ascii') }
        else:
            return {'error': "Invalid user"}

def load_user(credential):
    from server.models.user import User, db
    # first try to authenticate by token
    username_or_token = credential.get('username')
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(credential.get('password')):
            return False
    return user



def authenticate_user(f):
    def decore(f):
        @functools.wraps(f)
        def new_f(*args, **kwargs):
            if load_user(request.authorization):
                return f(*args, **kwargs)

        return new_f

    return decore(f)

