# forms.py is a file that contains all of the forms used in the application.

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, EqualTo

# SignUpForm inherits from FlaskForm class
class SignUpForm(FlaskForm):
          #    First Name is what will appear on the label
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    # Make sure the confirm password is equal to the password. Use EqualTo('password')
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')
    # remember = BooleanField('Remember Me')

# Create a class that creates a post form
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    # TextareaField is a form field that can accept multiline text.
    body = TextAreaField('Body', validators=[DataRequired()])
    image_url = StringField('Image URL')
    submit = SubmitField(' Create Post')

