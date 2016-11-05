from flask_restful import Api
from flask import Flask, jsonify
from flask import request
from server.handlers.location_handler import LocationHandler
from server.handlers.user_handler import UserHandler, TokenHandler
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/redcarpet_dev'
app.config['SECRET_KEY'] = 'This is the secret key'
db = SQLAlchemy(app)

api = Api(app)

api.add_resource(LocationHandler, "/api/locations", "/api/locations/<location_name>")
api.add_resource(UserHandler, "/api/users")
api.add_resource(TokenHandler, "/api/token")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

