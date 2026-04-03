from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, EmailField, BooleanField
from wtforms import validators


class RegisterForm(FlaskForm):
    email = EmailField("Email", [validators.DataRequired()])
    password = PasswordField(
        "Password",
        [
            validators.DataRequired(),
            validators.EqualTo("confirm", message="Passwords should match"),
        ],
    )
    confirm = PasswordField("Repeat Password")
    surname = StringField("Surname")
    name = StringField("Name")
    age = IntegerField("Age")
    position = StringField("Position")
    speciality = StringField("Speciality")
    address = StringField("Address")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    email = EmailField("Email", [validators.DataRequired()])
    password = PasswordField("password", validators=[validators.DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')