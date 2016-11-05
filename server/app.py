from flask_restful import Api
from flask import Flask, jsonify
from flask import request
from server.handlers.location_handler import LocationHandler
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/redcarpet_dev'
db = SQLAlchemy(app)

api = Api(app)

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Name %r>' % self.name

api.add_resource(LocationHandler, "/locations")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

