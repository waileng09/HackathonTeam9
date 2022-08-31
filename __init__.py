from flask import Flask, render_template, request, redirect, url_for, session, current_app, flash
from fastapi.templating import Jinja2Templates
from uuid import uuid4
import os, shelve
from Form import RecyclingForm
from functions import RecyclingForm
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

app = Flask(__name__)
BASEDIR = os.getcwd()
basedir = os.path.abspath(os.path.dirname(__file__))
db_recycle = f"{BASEDIR}/database/recycling_form"

templates = Jinja2Templates(directory=f"{BASEDIR}/templates")

app.config['UPLOADED_PHOTOS_DEST'] = "static/img"
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

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
    create_product_form = RecyclingForm(request.form)
    if request.method == "POST" and create_product_form.validate():
        product_dict = {}
        db = shelve.open(db_recycle, "c")
        try:
            product_dict = db["Products"]
        except:
            print("Error in retrieving Products from product.db.")
        uuid = str(uuid4())[:6]

        image_1 = photos.save(request.files.get('img1'), name="picture_of_" +uuid)

        product = RecyclingForm.Recycling(uuid, RecyclingForm.date.data, RecyclingForm.type.data,
                                  RecyclingForm.weight.data, RecyclingForm.description.data,image_1)
        quantity = create_product_form.product_quantity.data
        print(request.form.get('date'))
        product.set_stock(quantity)
        product_dict[uuid] = product
        db["Products"] = product_dict
        db.close()
        return redirect(url_for('retrieve_product'))
    return render_template('Product/createProduct.html', form=create_product_form,
                           img_data=encoded_img_data)

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
