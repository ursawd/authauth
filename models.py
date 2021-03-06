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
    feedback = db.relationship("Feedback", cascade="all,delete")

    def __repr__(self):
        s = self
        return f"<User {s.username} {s.password} {s.email} {s.first_name} {s.last_name}>"

    @classmethod
    def register(cls, username, password):
        hashed_password = bcrypt.generate_password_hash(password)
        # change from b string to utf8 string
        hashed_password = hashed_password.decode("utf8")
        return cls(username=username, password=hashed_password)

    @classmethod
    def login(cls, username, password):
        # check username / password
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Feedback(db.Model):
    """Feedback Model"""

    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), db.ForeignKey("users.username"))

    def __repr__(self):
        s = self
        return f"<User {s.id} {s.title} {s.content} {s.username}>"
