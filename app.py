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

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)




@app.route('/hello')

@app.route('/')
def index():
  return render_template('home.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 80)
