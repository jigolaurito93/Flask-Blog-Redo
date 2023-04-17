from flask import Flask 
# Import the Config class from the config module that has the app configurations like SECRET_KEY, etc...
from config import Config
# Import the classes from Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Import class Migrate from flask-migrate
from flask_migrate import Migrate
from flask_login import LoginManager

#  Create an instance of Flask class
app = Flask(__name__)
app.config.from_object(Config)

#  Create an instance of SQLAlchemy class to connect app to the database
db = SQLAlchemy(app)

# Create an instance of Migrate class to keep track of the database and app
migrate = Migrate(app, db)

#  Create an instance of LoginManager class to set up authentication
login = LoginManager(app)
# Tell the login manager wher to redirect if user is not logged in
# login here is an endpoint name that comes from the function names in routes.py
login.login_view = 'login'
# It shows a default message when user is not logged in
# To change the default message, do this
login.login_message = "You have to log in first to create a post"
# It just passes in what category the message should be displayed on the screen
login.login_message_category = 'danger'

#  Import all of the routes from the routes.py file, models from the models.py into the current package
#  From this current directory, import the routes.py file
from app import routes, models







