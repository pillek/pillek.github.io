import click
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advisors.sqlite'

db = SQLAlchemy()
db.init_app(app)


class Advisor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usermail = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(150), nullable=True)


# def insert_sample():
