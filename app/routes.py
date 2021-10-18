from app import app, db
from flask import render_template, redirect, url_for
from app.forms import RegistrationForm
from app.models import Product, User


@app.route('/')
def index():
    return render_template('index.html', name='Brian')


@app.route('/register', methods=["GET", "POST"])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        password = register_form.password.data
        # print(username, password)
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('register.html', form=register_form)


@app.route('/products')
def products():
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)


@app.route('/products/<prod_id>')
def product_detail(prod_id):
    product = Product.query.get_or_404(prod_id)
    return render_template('product_detail.html', product=product)