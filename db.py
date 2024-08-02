import click
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import LargeBinary
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///advisors.sqlite'

db = SQLAlchemy()
db.init_app(app)



