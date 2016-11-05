from flask_restful import Resource
from flask import request
import json


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