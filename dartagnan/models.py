from configs import db


class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ph = db.Column(db.Float, nullable=False)
    turbidez = db.Column(db.Float, nullable=False)
    condutividade = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)