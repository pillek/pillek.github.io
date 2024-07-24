from flask_wtf import FlaskForm
from wtforms import FileField, StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    usermail = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name')
    description = TextAreaField('Description')
    image = FileField('Image')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    usermail = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')