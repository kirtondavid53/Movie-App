import json
from flask import Flask, request, render_template, redirect, flash, url_for
from flask_jwt import JWT, jwt_required, current_identity
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
from sqlalchemy.exc import IntegrityError
from flask_bootstrap import Bootstrap
from datetime import timedelta 

from models import db, User
from forms import SignUp, LogIn


''' Begin Flask Login Functions '''
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

''' End Flask Login Functions '''

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  login_manager.init_app(app)
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app)
''' End Boilerplate Code '''


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/movie')
def movie():
  return render_template('movie.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignUp() # create form object
  if form.validate_on_submit():
    data = request.form # get data from form submission
    newuser = User(username=data['username'], email=data['email']) # create user object
    newuser.set_password(data['password']) # set password
    db.session.add(newuser) # save new user
    db.session.commit()
    flash('Account Created!')# send message
    return redirect(url_for('login'))# redirect to login page
  return render_template('signup.html', form=form) # pass form object to template

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LogIn()
  if form.validate_on_submit(): # respond to form submission
    data = request.form
    user = User.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']): # check credentials
      flash('Logged in successfully.') # send message to next page
      login_user(user) # login the user
      return redirect(url_for('index')) # redirect to main page if login successful
    else:
      flash('Invalid username or password') # send message to next page
  return render_template('login.html', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == "__main__":
    app.run(debug=True)