# Create a new python file for the database
# db is where we get our models from
# db is the instance of SQLAlchemy, login is the instance of LoginManager 
from app import db, login
# Import datetime from datetime module, so that we can use it as a column.
from datetime import datetime
# generate_password_hash is a function that generates a multicode hash of a password
#  check_password_hash is a function that checks a password against a multicode hash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# Define a class , which will inherit from db.Model
class User(db.Model, UserMixin):
    # This will auto-increment the primary key
    # Primary key defaults to false
    # Primary key, when true, sets the column and the primary key
    id = db.Column(db.Integer, primary_key=True)
    # Nullable, when true, makes the column to be a required field
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Unique, when true, makes the column to be a unique field, only one user can have the same email
    email = db.Column(db.String(50), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    # Import datetime from datetime module, so that we can use it as a column.
    # db.datetime is a function that returns the current date and time
    # utcnow is a function that returns the current date and time
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    # kwargs are the keyword arguments passed in by user input, such as username, password, first name, last name email etc.
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Its going to look into the keyword arguments for a password key and generate a password hash that would be stored in self.password
        # Its like saying, regardless of how many arguments, find the password generate a password hash and store it as self.password
        self.password = generate_password_hash(kwargs.get('password'))
        # Automatically adds the user to the database every time it is created
        # Self is the model object that we just created
        db.session.add(self)
        # Just to push it
        db.session.commit()

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

@login.user_loader
def get_a_user_by_id(user_id):
    return db.session.get(User, user_id)