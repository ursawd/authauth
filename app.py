import os
from dotenv import load_dotenv
from flask import Flask,request,redirect,render_template,flash
from flask_debugtoolbar import DebugToolBarExtension
from models import db, connect_db, User, Feedback
load_dotenv()
app=Flask(__name__)
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")
debug=DebugToolBarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql:///authauth"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_ECHO"]=True

connect_db(app)

