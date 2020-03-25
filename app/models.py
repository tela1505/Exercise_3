from werkzeug.security import generate_password_hash, check_password_hash

from app import db

from app import db


class User(db.Model):

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    # forecast = db.relationship('Forecast', backref='users')


class City(db.Model):
    __tablename__ = 'city'
    city_id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(250), nullable=False)
    # forecast = db.relationship ('Forecast', backref='cities')


class Forecast(db.Model):
    forecast_id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.city_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    forecast_datetime = db.Column(db.String(), nullable=False)
    comment = db.Column(db.String(250))
