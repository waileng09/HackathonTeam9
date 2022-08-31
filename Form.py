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


class RecyclingForm(Form):
    date = DateField('Date of Recycle',format='%d-%m-%Y',)
    type = RadioField('Type of Waste', choices=[('Plastic'), ('Metal'),('Glass'),('Paper'),('Batteries'),('Other')],)
    weight = DecimalField('Weight of Waste (kg):',[validators.number_range(min=0.1)],default=0.1,)
    description = StringField('Please briefly decribe the waste.',[validators.Length(min=5, max=150), validators.DataRequired()])
    image_1 = FileField('Please upload a pictures for verification.', validators=[FileAllowed(['jpg', 'png', 'gif', 'jpeg'], validators.DataRequired())])