from app import app
from flask import render_template
from app.forms import RegistrationForm

@app.route('/')
def index():
    return render_template('index.html', name='Dominick')

@app.route('/register')
def register():
    register_form = RegistrationForm()
    return render_template('register.html', form=register_form)