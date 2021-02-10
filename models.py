from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()


def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)


class User(db.Model):
    """User Model"""

    __tablename__ = "users"

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        s = self
        return f"<User {s.username} {s.password} {s.email} {s.first_name} {s.last_name}>"

    @classmethod
    def register(cls, username, password):
        hashed_password = bcrypt.generate_password_hash(password)
        # change from b string to utf8 string
        hashed_password = hashed_password.decode("utf8")
        return cls(username=username, password=hashed_password)