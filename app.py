from flask import Flask, render_template, request, session
from common.database import Database
from models.user import User

# __name__ is a built in private variable which contains '__main__'
app = Flask(__name__)
app.secret_key = "Brice"

@app.route('/') # www.mysite.com/api/
def hello_method():
    #render the html files containing Jinja2 (used to simplify the html by flask)
    return render_template("login.html")

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    #render template when user is logged in. We can give render_template any data that we want (email in this instance) which is given to the template as a JINJA variable
    return render_template("profile.html", email=session['email'])

if __name__ == '__main__':
    app.run()