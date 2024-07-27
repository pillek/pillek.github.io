import click
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import LargeBinary
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
    image = db.Column(LargeBinary, nullable=True)  # Change to LargeBinary


def insert_sample_with_image(image_path):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    advisor = Advisor(
        usermail='sample@example.com',
        password='secursepassword',
        name='Sample Advisor',
        description='This is a sample advisor.',
        image=image_data  # Save binary data
    )
    db.session.add(advisor)
    db.session.commit()
