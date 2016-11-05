from flask_restful import Resource
from flask import request
import json

class LocationHandler(Resource):
    def get(self, location_name):
    	from server.models.location import Location, db
    	location = db.session.query(Location).filter(Location.name == location_name).first()
    	if location:
    		results = db.engine.execute(
    			"select * from locations WHERE earth_box(ll_to_earth({latitude}, {longitude}), 10) @> ll_to_earth(locations.latitude, locations.longitude)".format(latitude=location.latitude, longitude=location.longitude)
    			)
    		nearby_locations = []
    		for row in results:
			
			    nearby_locations.append({'name': row.name, 'latitude': row.latitude, 'longitude': row.longitude})
    		return {"nearby_locations": nearby_locations}
    	else:
    		return {"error": "Location not found"}

    def post(self):
    	from server.models.location import Location, db
    	input_data = json.loads(request.data)
    	location = Location(name=input_data.get('name'), latitude=input_data.get('latitude'),
    		longitude=input_data.get('longitude'))
    	db.session.add(location)
        db.session.commit()
    	return {"success":True}
    	
