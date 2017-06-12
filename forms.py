from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators = [DataRequired("Please enter the First Name")])
	last_name = StringField('Last Name', validators = [DataRequired("Please enter the Last Name")])
	email = StringField('email', validators = [DataRequired("Please enter the Email id"), Email("Please enter valid emailid")])
	password = PasswordField('password', validators = [DataRequired("Please enter the password"), Length (min=6, message = "Password must be atleast 6 characters")])
	submit = SubmitField('Sign Up')