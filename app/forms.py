from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class SignupForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email address', validators=[DataRequired(),Email()])


