# to create SQLite
# python
# from app import db, app
# db.create_all()
# app.app_context().push()
# exit()

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from database import db
#db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
class Login(db.Model):
    login_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    usermail = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    customer = db.relationship('Customer', backref='login', uselist=False)
    consultant = db.relationship('Consultant', backref='login', uselist=False)

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.login_id'), nullable=False)
    requests = db.relationship('CustomerRequest', backref='customer', lazy=True)

class Consultant(db.Model):
    consultant_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    adresse = db.Column(db.String(200), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)
    VAT = db.Column(db.String(50), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.login_id'), nullable=False)
    responses = db.relationship('ConsultantResponse', backref='consultant', lazy=True)

class CustomerRequest(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=False)

class ConsultantResponse(db.Model):
    response_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    consultant_id = db.Column(db.Integer, db.ForeignKey('consultant.consultant_id'), nullable=False)
    request_id = db.Column(db.Integer, db.ForeignKey('customer_request.request_id'), nullable=False)
