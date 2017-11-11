from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/hello')

@app.route('/')
def index():
  return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
