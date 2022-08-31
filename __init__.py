from flask import Flask, render_template, request, redirect, url_for
from fastapi.templating import Jinja2Templates
from uuid import uuid4
import os, shelve
from Form import RecyclingForm
from functions import Recycling
from flask_uploads import UploadSet, configure_uploads, IMAGES

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

@app.route('/recycling_page')
def recyclingform():
    return render_template('customer page/recycling_page.html')

@app.route('/recycling_form', methods=['GET', 'POST'])
def create_form():
    encoded_img_data = ""
    create_recycling_form = RecyclingForm(request.form)
    if request.method == "POST" and create_recycling_form.validate():
        recycling_dict = {}
        db = shelve.open(db_recycle, "c")
        try:
            recycling_dict = db["Recycling_database"]
        except:
            print("Error in retrieving records from recycling.db .")
        uuid = str(uuid4())[:6]

        image_1 = photos.save(request.files.get('img1'))

        recycling_item = Recycling.Recycling(uuid, create_recycling_form.date.data, create_recycling_form.type.data,
                                  create_recycling_form.weight.data, create_recycling_form.description.data,image_1)
        recycling_dict[uuid] = recycling_item
        db["Recycling_database"] = recycling_dict
        db.close()
        return redirect(url_for('retrieve_recycling_record'))
    return render_template('customer page/recycling_form.html', form=create_recycling_form,
                           img_data=encoded_img_data)

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
    return render_template('customer page/recycling_record.html', count=len(records_list), records_list=records_list)

@app.route('/contact')
def contact():
    return render_template('customer page/contact.html')

# staff page routes
@app.route('/staff_dashboard')
def staff_dashboard():
    return render_template('staff page/staff_dashboard.html')


# Tree page
@app.route('/tree')
def tree():
    return render_template('')


if __name__ == '__main__':
    app.debug = True
    app.run()
