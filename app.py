from flask import Flask, render_template, url_for, request, session, redirect, json
from flask_login import LoginManager, UserMixin
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

from methodCall import Photo
from methodCall import mainPhoto

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "THISISSECRET"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/thinky/Desktop/HackPrinceton/masterPholosco/database.db'
# db = MongoEngine()
# db.init_app(app)

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if (user_id == "wjz2101@columbia.edu"):
        return User()
    else:
        return
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique = True)
    password = db.Column(db.String(80))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message = 'Invalid Email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8,max =80)])

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message = 'Invalid Email'), Length(max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8,max =80)])

@app.route('/')
def index():
    # if 'username' in session:
    #     print('check')
    #     return 'You are logged in as' + session['username']
    mainP = mainPhoto()
    photos = mainP.getData(5)
    dataForUse = {}
    for i in photos:
        dataForUse[i.get_photo_id()] = [i.get_latitude(),i.get_longitude()]
    return render_template('home.html', dataForUse=json.dumps(dataForUse))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print("What")
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            if user.password == form.password.data:
                return redirect(url_for('profile'))
        return '<h1> nah </h1>'
    return render_template('login.html', form = form)

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/profile')
def profile():

    return render_template('profile.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(email = form.email.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1>' + 'New User has been created' + '</h1>'

        return '<h1>' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form = form)

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run('0.0.0.0',debug=True)
