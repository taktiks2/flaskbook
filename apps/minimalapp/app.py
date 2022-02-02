from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello flask'


@app.route('/hello/<name>',
           methods=['GET', 'POST'],
           endpoint='hello-endpoint')
def hello(name):
    return f'hello {name}!'
