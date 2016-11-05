from flask_restful import Api
from flask import Flask, jsonify
from flask import request
from server.handlers.location_handler import LocationHandler


app = Flask(__name__)

api = Api(app)

api.add_resource(LocationHandler, "/locations")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

