from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, TextAreaField
from wtforms.validators import InputRequired, Email


class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    first_name = StringField("First Name", validators=[InputRequired()])
    last_name = StringField("Last Name", validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])


class UserForm(FlaskForm):
    username = StringField("User Name")
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")


class FeedbackForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    content = TextAreaField("Content", render_kw={"rows": 5}, validators=[InputRequired()])
