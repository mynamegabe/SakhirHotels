from wtforms import Form, StringField, DecimalField, RadioField, SelectField, TextAreaField, DateField, IntegerField, PasswordField, validators

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    membership = RadioField('Membership', choices=[('C', 'Customer'), ('M', 'Member'), ('A', 'Admin')], default='C')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    pw = StringField('Change Password', [validators.Length(min=1, max=150), validators.Optional()])

class CreatePromoForm(Form):
    promo_name = StringField('Promotion Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    desc = StringField('Description', [validators.Length(min=1, max=150), validators.DataRequired()])
    endDate = DateField('End Date', [validators.DataRequired()], format='%d/%m/%Y')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateSignupForm(Form):
    first_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    birthdate = DateField('', [validators.DataRequired()], format='%d/%m/%Y')
    pw = PasswordField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateLoginForm(Form):
    username = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    pw = PasswordField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateUserSearchForm(Form):
    username = StringField('Username or User ID', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateDetailsForm(Form):
    name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = IntegerField('', [validators.DataRequired()])
    query = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateChatForm(Form):
    inputtext = StringField('',[validators.Length(min=0, max=400), validators.DataRequired()])

class CreateRoomSearchForm(Form):
    startdate = DateField('', [validators.DataRequired()], format='%d/%m/%Y')
    enddate = DateField('', [validators.DataRequired()], format='%d/%m/%Y')
    adults = IntegerField('', [validators.DataRequired()])
    children = IntegerField('', [validators.DataRequired()])

class CreateUpdateDetailsForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = IntegerField('Phone Number', [validators.DataRequired()])
    query = StringField('Query', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateUpdateSwabForm(Form):
    ic = StringField('IC', [validators.Length(min=1, max=4), validators.DataRequired()])
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = IntegerField('Last Name', [validators.DataRequired()])
    swabcheck = StringField('Swab Test', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateSwabForm(Form):
    ic = StringField('', [validators.Length(min=1, max=4), validators.DataRequired()])
    first_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    swabcheck = SelectField('', choices=[('Positive', 'Positive'), ('Negative', 'Negative')])

class CreateRoomForm(Form):
    category = SelectField('Category', choices=[('Studio', 'Studio'), ('Regular', 'Regular'), ('Suite', 'Suite')])
    room_name = StringField('Room Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    rooms = IntegerField('Rooms', [validators.DataRequired()])
    avail_rooms = IntegerField('Available Rooms', [validators.DataRequired()])
    price = IntegerField('Price', [validators.DataRequired()])
    capacity = StringField('Capacity', [validators.Length(min=1, max=150), validators.Optional()])
    details = StringField('Details', [validators.Length(min=1, max=150), validators.Optional()])

class CreateTempForm(Form):
    id = IntegerField('User ID',[validators.DataRequired()])
    temperature = DecimalField('Temperature(°C)',places=1)
