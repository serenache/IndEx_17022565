from app import db


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    forecast = db.relationship("Forecast")


class City(db.Model):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(250), nullable=False)
    forecast = db.relationship("Forecast")


class Forecast(db.Model):
    __tablename__ = 'forecast'
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    forecast_datetime = db.Column(db.String(250), nullable=False)
    forecast = db.Column(db.String(250), nullable=False)
    comment = db.Column(db.String(250))
