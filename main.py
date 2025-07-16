# Введение во Flask
# MVC-(Model View Controller)
from flask import Flask

app = Flask(__name__)
debug = False


@app.route('/')
@app.route('/index')
def index():
    print('Вызвана функция index')
    return 'Привет, Flask'


@app.route('/about')
def about():
    print('Вызвана функция about')
    return 'О нас'


@app.route('/countdown')
def cd():
    lst = [str(x) for x in reversed(range(10))]
    lst.append('Полетели!!!')
    return '<br>'.join(lst)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=debug)
