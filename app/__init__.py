from flask import Flask 
# Import the Config class from the config module that has the app configurations like SECRET_KEY, etc...
from config import Config
# Import the classes from Flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
# Import class Migrate from flask-migrate
from flask_migrate import Migrate

#  Create an instance of Flask class
app = Flask(__name__)
app.config.from_object(Config)

#  Create an instance of SQLAlchemy class to connect app to the database
db = SQLAlchemy(app)

# Create an instance of Migrate class to keep track of the database and app
migrate = Migrate(app, db)

#  Import all of the routes from the routes.py file, models from the models.py into the current package
#  From this current directory, import the routes.py file
from app import routes, models







