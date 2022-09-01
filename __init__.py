from flask import Flask, render_template, request, redirect, url_for
from fastapi.templating import Jinja2Templates
from Form import CreateCustomerForm
import Customer
from uuid import uuid4
import os, shelve
from Form import RecyclingForm
from functions import Recycling
from werkzeug.utils import secure_filename
from flask_uploads import UploadSet, configure_uploads, IMAGES
from datetime import datetime, timedelta, date
from starlette.requests import Request

app = Flask(__name__)
BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))
db_recycle = f"{BASEDIR}/database/recycling_form"

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

app.config['UPLOADED_PHOTOS_DEST'] = "static/img/upload_img"
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)


# customer page routes
@app.route('/')
def customer_home():
    return render_template('customer page/customer_home.html')


# start recycling page
@app.get("/recycling_page")
def recycling_page():
    return render_template('customer page/recycling_page.html')


# recycling form page
@app.route('/recycling_form', methods=['GET', 'POST'])
def create_form():
    encoded_img_data = ""
    if request.method == "POST":
        recycling_dict = {}
        db = shelve.open(db_recycle, "c")
        try:
            recycling_dict = db["Recycling_database"]
        except:
            print("Error in retrieving records from recycling.db .")
        uuid = str(uuid4())[:6]
        image_1 = photos.save(request.files.get('img1'), name="recycling_of_" + uuid)

        recycling_dict[uuid] = {"id": uuid,
                                "location": request.form['location'],
                                "type": request.form['type'],
                                "weight": request.form['weight'],
                                "description": request.form['description'],
                                "profile_img": image_1,
                                "date_created": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                                "status": "Process"
                                }
        db["Recycling_database"] = recycling_dict
        db.close()
        return redirect(url_for('recycling_thank_page'))
    return render_template('customer page/recycling_form.html',
                           img_data=encoded_img_data)


@app.route('/recycling_thank_page')
def recycling_thank_page():
    return render_template('customer page/recycling_thank_page.html')


# View record page ( for customer and both also can work)
@app.route('/recycling_record')
def retrieve_recycling_record():
    recycling_dict = {}
    try:
        db = shelve.open(db_recycle, "r")
        recycling_dict = db["Recycling_database"]
    except:
        db = shelve.open(db_recycle, "n")
    db.close()
    records_list = []

    for item in recycling_dict:
        product = recycling_dict.get(item)
        records_list.append(product)

    return render_template('customer page/recycling_record.html', count=len(records_list),
                           records_list=records_list)


@app.route('/recycling_point')
def recycling_point():
    return render_template('customer page/recycling_point.html')


@app.route('/contact')
def contact():
    return render_template('customer page/contact.html')


# staff page routes
@app.route('/staff_dashboard')
def staff_dashboard():
    return render_template('staff page/staff_dashboard.html')


# staff view application
@app.route('/staff_view')
def staff_view():
    recycling_dict = {}
    try:
        db = shelve.open(db_recycle, "r")
        recycling_dict = db["Recycling_database"]
    except:
        db = shelve.open(db_recycle, "n")
    db.close()
    records_list = []

    for item in recycling_dict:
        product = recycling_dict.get(item)
        records_list.append(product)
    return render_template('staff page/staff_view_item.html', records_list=records_list)



# staff manage application
@app.route('/staff_manage')
def staff_manage():
    recycling_dict = {}
    try:
        db = shelve.open(db_recycle, "r")
        recycling_dict = db["Recycling_database"]
    except:
        db = shelve.open(db_recycle, "n")
    db.close()
    records_list = []

    for item in recycling_dict:
        product = recycling_dict.get(item)
        if product['status'] == 'Process':
            records_list.append(product)
    return render_template('staff page/staff_manage_item.html', records_list=records_list)


@app.route('/application_approved/<id>', methods=['GET', 'POST'])
def application_approved(id):
    if request.method == "POST":
        recycling_dict = {}
        try:
            db = shelve.open(db_recycle, "w")
            recycling_dict = db["Recycling_database"]
        except:
            db = shelve.open(db_recycle, "n")
        key = recycling_dict.get(id)
        if request.form['approve'] == "approve":
            key["status"] = "Approved"
            print('yes')
        if request.form['reject'] == "reject":
            key["status"] = "Rejected"
            print('no')
    db["Recycling_database"] = recycling_dict
    db.close()

    return redirect(url_for('staff_view'))


# Tree page
@app.route('/tree')
def tree():
    return render_template('')


# sign up page
@app.route('/createCustomer', methods=['GET', 'POST'])
def create_user():
    # fix the counting
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    if len(customers_dict) > 0:
        x = list(reversed(list(customers_dict)))[0]
        print(x)
        total_count = x + 1
    else:
        total_count = 1
    # total_count = len(customers_dict)+1
    create_customer_form = CreateCustomerForm(request.form)
    print(create_customer_form)
    if request.method == 'POST':
        customers_dict = {}
        db = shelve.open('customer.db', 'c')
        print('pass')
        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        if create_customer_form.password.data == create_customer_form.password2.data:
            last_login = datetime.now()
            status = True
            customer = Customer.Customer(create_customer_form.first_name.data, create_customer_form.last_name.data,
                                         create_customer_form.email_address.data,
                                         create_customer_form.password.data, create_customer_form.password2.data,
                                         create_customer_form.type.data, create_customer_form.birthday.data)

            from flask import session
            session['logged_in'] = True
            if customer.get_type() == 'Customer':
                print('added')
                customer.set_customer_id(total_count)
                customers_dict[customer.get_customer_id()] = customer
                db['Customers'] = customers_dict

                # login file
                login_file = open('login.txt', 'w')
                email = customer.get_email_address()
                birthday = customer.get_birthday()
                login_name = customer.get_first_name() + ' ' + customer.get_last_name()
                login_file.write(login_name + '\n')
                login_file.write(email + '\n')
                login_file.write(str(birthday))
                login_file.close()

                print('customer_info')


        else:
            print("password is different")
            from flask import flash
            flash("password is different", category='error')
            return render_template('customer page/create_acc.html', form=create_customer_form)
        # fix
        customer.set_customer_id(total_count)
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        print('retrieve')
    return render_template('customer page/create_acc.html', form=create_customer_form)


# login page
@app.route('/CustomerLogin', methods=['GET', 'POST'])
def user_login():
    print('ok')
    user_login_form = CreateCustomerForm(request.form)
    if request.method == 'POST':
        email = user_login_form.email_address.data
        password = user_login_form.password.data
        print('{} {}'.format(email, password))
        # validation
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        customer = customers_dict.get(id)
        for key in customers_dict:
            if email == customers_dict[key].get_email_address():
                if password == customers_dict[key].get_password():
                    print("Login successfuly")
                    # login file
                    login_name = customers_dict[key].get_first_name() + ' ' + customers_dict[key].get_last_name()
                    birthday = customers_dict[key].get_birthday()
                    login_file = open('login.txt', 'w')
                    login_file.write(login_name + '\n')
                    login_file.write(email + '\n')
                    login_file.write(str(birthday))
                    login_file.close()

                    date = birthday.strftime("%d")
                    month = birthday.strftime("%m")
                    print(birthday)
                    print(date)
                    print(month)

                    if customers_dict[key].get_type() == 'Customer':
                        return redirect(url_for('customer_info'))

                    else:
                        return redirect(url_for('staff_dashboard'))

                else:
                    print("Incorrect password")

            else:
                print("email does not exist")

        db.close()
    return render_template('customer page/customer_login.html', form=user_login_form)



# customer info
@app.route('/CustomerInfo')
def customer_info():
    login_file = open('login.txt', 'r')
    name = login_file.readline()
    email = login_file.readline()
    birthday = login_file.readline()
    print(name + email + birthday)
    login_file.close()
    return render_template('customer page/customer_info.html', name=name, email=email, birthday=birthday)


# reward display(customer side)
@app.route('/displayrewards')
def display_rewards():
    return render_template('customer page/customer_rewards.html')


# logout
@app.route('/logout')
def logout():
    return render_template('customer page/customer_home.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
