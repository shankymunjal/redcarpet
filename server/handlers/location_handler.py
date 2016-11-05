from flask_restful import Resource
from flask import request
import json

class LocationHandler(Resource):
    def get(self):
    	return "get locations"

    def post(self):
    	from server.models.location import Location, db
    	input_data = json.loads(request.data)
    	location = Location(name=input_data.get('name'), latitude=input_data.get('latitude'),
    		longitude=input_data.get('longitude'))
    	db.session.add(location)
        db.session.commit()
    	return {"success":True}
    	
