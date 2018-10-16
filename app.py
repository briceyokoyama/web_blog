from flask import Flask

# __name__ is a built in private variable which contains '__main__'
app = Flask(__name__)

@app.route('/') # www.mysite.com/api/
def hello_method():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run()