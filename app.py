from flask import Flask, render_template, url_for
from flask_login import LoginManager,  UserMixin

app = Flask(__name__)
app.config['DEBUG'] = True
login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(UserMixin):
    pass


@app.route('/')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/login')
def settings():
    return render_template('login.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80)
