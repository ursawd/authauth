"""Seed file to make sample data for authauth.users and feedback tables.
   Database authauth must exist before running this file.
   defined in app.py():
   app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///authauth"
"""

from models import db, User, Feedback
from app import app

# create all tables
db.drop_all()
db.create_all()

# create user
user1 = User(
    username="username1",
    # hashed password for "password = 'password'"
    password="$2b$12$h9kN440NdtdbCimRcpu.Z.JSRGMWv42TJFlxeeBLPn6JqelMCQCPe",
    email="user@user.com",
    first_name="userfirstname",
    last_name="userlastname",
)

db.session.add(user1)
db.session.commit()

# create feedback for user1
feedback1 = Feedback(
    title="This is a title of the first feedback",
    content="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean quis orci eget neque tempor euismod non ut dui. Donec velit felis, auctor nec sapien ut, scelerisque congue dui. Nullam non quam arcu. Praesent in felis accumsan, molestie magna sed, suscipit dolor. Nullam rutrum vestibulum arcu quis facilisis. Cras dapibus lorem ac gravida eleifend. Nunc non hendrerit libero. Vestibulum nunc neque, imperdiet vel commodo in, ultricies ac nisi. Nam rhoncus vel velit quis finibus. Praesent eu arcu tortor.",
    username="username1",
)
feedback2 = Feedback(
    title="Title of the second feedback",
    content="Nam placerat nec lectus id bibendum. Praesent blandit libero consequat, auctor felis in, ultricies metus. Suspendisse at mattis est, at dapibus felis. Aliquam erat volutpat. Fusce eget tellus neque. Quisque id diam aliquet, feugiat enim non, ultricies sapien. Quisque congue ac eros at porttitor. Praesent ut sodales ex.",
    username="username1",
)
db.session.add(feedback1)
db.session.add(feedback2)
db.session.commit()
