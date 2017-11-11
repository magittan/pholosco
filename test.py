from flask import Flask, render_template, url_for, request, session, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, Email
from flask_login import LoginManager, UserMixin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
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

class User(UserMixin):
    username = "wjz2101@columbia.edu"
    password = "hackprinceton"
    email = "wjz2101@columbia.edu"

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Enter email'), Email('Invalid email')])
    password = PasswordField('Password', validators=[InputRequired('Enter a password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log In')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # Here we use a class of some kind to represent and validate our
#     # client-side form data. For example, WTForms is a library that will
#     # handle this for us, and we use a custom LoginForm to validate.
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Login and validate the user.
#         # user should be an instance of your `User` class
#         user = User(form.username.data, form.email.data,
#                     form.password.data)
#
#         login_user(user)
#
#         flash('Logged in successfully.')
#
#         next = request.args.get('next')
#         # is_safe_url should check if the url is safe for redirects.
#         # See http://flask.pocoo.org/snippets/62/ for an example.
#         if not is_safe_url(next):
#             return abort(400)
#
#         return redirect(next or url_for('index'))
#     return render_template('login.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.objects(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.home'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as' + session['username']

    return render_template('home.html')

@app.route('/register')
def register():
    return ''

if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)
