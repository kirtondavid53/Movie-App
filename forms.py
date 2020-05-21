from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, EqualTo, Email

class SignUp(FlaskForm):
  username = StringField('username', validators=[InputRequired()])
  email = StringField('email', validators=[Email(), InputRequired()])
  password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
  confirm  = PasswordField('Repeat Password')

class LogIn(FlaskForm):
  username = StringField('username', validators=[InputRequired()])
  password = PasswordField('Password', validators=[InputRequired()])