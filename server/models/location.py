from server.app import db

class Location(db.Model):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)