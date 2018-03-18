from flask import render_template, request
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
  user = {'username': 'Demogorgon'}
  return render_template('index.html', title='Helllz', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  print("form data", form)
  return render_template('login.html', title='Sign in', form=form)
