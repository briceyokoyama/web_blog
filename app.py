from flask import Flask, render_template

# __name__ is a built in private variable which contains '__main__'
app = Flask(__name__)

@app.route('/') # www.mysite.com/api/
def hello_method():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()