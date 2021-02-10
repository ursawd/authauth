import os
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import RegisterForm

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///authauth"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

connect_db(app)

# *****************************************************
# routes


@app.route("/")
def index():
    """ index redirect to register"""
    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def register():
    """show registration form
    process registration form
    add user to db
    """
    # create form
    form = RegisterForm()
    # check if valid  submitted, this check false if GET
    if form.validate_on_submit():
        # get form values
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        db.session.add(user)
        db.session.commit()

        flash(f" Added user {username}")
        return redirect("/secret")
    else:
        return render_template("register.html", form=form)


@app.route("/secret")
def secret():
    return "SECRET ROUTE"