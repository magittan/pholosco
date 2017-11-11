from flask import Flask, render_template, url_for
from flask_login import LoginManager
#from flask_bootstrap import Bootstrap
f#rom flask_mongoengine import MongoEngine
#from flask_moment import Moment

import os


login_manager = LoginManager()
login_manager.session_protection = 'string'
login_manager.login_view = 'auth.login'
bootstrap = Bootstrap()
db = MongoEngine()
mail = Mail()
moment = Moment()

app = Flask(__name__)
login_manager = LoginManager()


app.config['DEBUG'] = True

@app.route('/hello')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
