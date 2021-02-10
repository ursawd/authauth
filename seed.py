"""Seed file to make sample data for authauth.users table"""

from models import db, User
from app import app

# create all tables
db.drop_all()
db.create_all()

# create user
user1 = User(
    username="username1",
    password="password1",
    email="user@user.com",
    first_name="userfirstname",
    last_name="userlastname",
)

db.session.add(user1)
db.session.commit()
