from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

# from app.models import User

class SignupForm (FlaskForm):
    username = StringField ('Username', validators=[DataRequired ()])
    email = StringField ('Email address', validators=[DataRequired (), Email ()])
    password = PasswordField ('Password', validators=[DataRequired (), EqualTo ('confirm', message='Passwords must match')])
    confirm = PasswordField ('Repeat Password')
    submit = SubmitField ('Sign Up')
