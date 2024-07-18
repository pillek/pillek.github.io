from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class RegistrationForm(FlaskForm):
    usermail = StringField('Usermail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name')
    description = StringField('Description')
    image = StringField('Image URL')
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    usermail = StringField('Usermail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')