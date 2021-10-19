from app import app, db
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.forms import RegistrationForm, LoginForm
from app.models import Product, User, Cart


@app.route('/')
def index():
    all_products = Product.query.all()
    return render_template('index.html', products=all_products)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            return redirect(url_for('login'))

        login_user(user)
        
        return redirect(url_for('index'))
    flash ('Username or Password incorrect')
    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/my-cart')
@login_required
def my_cart():
    my_products = current_user.products
    return render_template('my_cart.html', products= my_products)

@app.route('/add-to-cart/<prod_id>')
@login_required
def add_to_cart(prod_id):
    product = Product.query.get_or_404(prod_id)
    current_user.products.append(product)
    db.session.commit()
    return redirect(url_for('my_cart'))


@app.route('/my-cart/<int:prod_id>/cart_item', methods=['POST'])
@login_required
def cart_delete(prod_id):
    Cart.query.filter(Cart.id == prod_id).delete()
    db.session.commit()
    flash("Item has been removed", 'primary')
    return redirect(url_for('index'))