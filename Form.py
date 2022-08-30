from wtforms import Form, StringField, RadioField, SelectField, validators, DecimalField, TextAreaField, PasswordField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import EmailField, DateField,IntegerField

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email_address = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=5, max=150), validators.DataRequired()])
    password2 = PasswordField('Confirm Password', [validators.Length(min=5, max=150), validators.DataRequired()])
    type = RadioField(' ', choices=[('Administrator'), ('Customer')])
    birthday = DateField('birthday', format='%Y-%m-%d')
    phone_num = StringField('Phone Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=10, max=150), validators.DataRequired()])
