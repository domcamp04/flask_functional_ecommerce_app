from app import app
from flask import render_template
from app.forms import RegistrationForm

@app.route('/')
def index():
    return render_template('index.html', name='Dominick')

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        password = register_form.password.data
        print(username, password)
    return render_template('register.html', form=register_form)