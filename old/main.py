# Введение во Flask
# MVC-(Model View Controller)
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, Flask'


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
