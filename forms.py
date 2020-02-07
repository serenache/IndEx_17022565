from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('Repeat password')

