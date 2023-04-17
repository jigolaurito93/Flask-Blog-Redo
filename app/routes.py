#  From the app module, import the app instance, import db to make selection query
# From the __init__.py file, import the app instance (app = Flask(__name__))
from app import app, db
from flask import render_template, redirect, url_for, flash
from fake_data import posts
from app.forms import SignUpForm, LoginForm
# Import user model from app.models
from app.models import User


# Use route() decorator to tell Flask what URL should trigger our function
@app.route("/")
def index():
    # return the html template you want to render
    return render_template("index.html", posts=posts, logged_in = True)




@app.route("/signup", methods = ["GET", "POST"])
def signup():
    # form is an instance of the SignUpForm class. Create an instance of the form (in the context of the current request)
    form = SignUpForm()
    # When the form is submitted, validate the data
    # Check if the form is validated, (is submitted), and that all of the fields are valid
    if form.validate_on_submit():   
        # If so, get the data from the form fields
        print('Hooray our form is validated!!!')
        # first_name is the name of whatever the user enetered as first name
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        print(first_name, last_name, email, username, password) 
        # Check to see if there is already an existing user with that username or email.
        check_user = db.session.execute(db.select(User).filter((User.username == username) | (User.email == email))).scalars().all()
        # If check_user is True, if username or email is already taken:
        if check_user:
            # Flash a message saying that the user with email or username is already taken
            flash("A user with that username or email already exists", "warning")
            # It redirects the user back to the signup page if username or email is already taken
            return redirect(url_for('signup'))
        # If check_user is empty, create a new record in the user table
        # new_user is an instance of User, then pass in the key-word arguments from the form
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        # Import flash from flask
        flash(f"Thank you {new_user.username} for signing up! You can now log in", "success")
        # It then redirects the user back to the index page if form is validated   
        # Import redirect, url_for from flask
        return redirect(url_for('index'))
    return render_template("signup.html", form=form)






# Set up methods for post and get to make the submit button work
@app.route('/login', methods = ["GET", "POST"])
def login():
    # form is an instance of the LoginForm class. Create an instance of the form (in the context of the current request)
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        print(username, password)
        print('Hooray our form is validated!!!')
        #  TODO: Check if the username and password are valid
        user = User.query.filter_by(username=username).first()
        # if user is not None, meaning we get back a user and when we call the check_password method, with the password we get back from the form:
        # If both comes back as True, run this code.
        if user is not None and user.check_password(password):
            flash(f'You have successfully logged in as {username}','success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username and/or password Please try again', 'danger')
            return redirect(url_for('login'))

    # Send the instance of LoginForm as form to the template, login.html
    return render_template("login.html", form=form)