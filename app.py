from flask import Flask, render_template, url_for, request, session, redirect
from flask_login import LoginManager, UserMixin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True
# db = MongoEngine()
# db.init_app(app)

bootstrap = Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    if (user_id == "wjz2101@columbia.edu"):
        return User()
    else:
        return

@app.route('/')
def index():
    if 'username' in session:
        print('check')
        return 'You are logged in as' + session['username']

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run('0.0.0.0',debug=True)
