# Введение во Flask
# MVC-(Model View Controller)
from fileinput import filename

from flask import Flask, url_for
import sqlite3

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


@app.route('/image')
def show_image():
    return f'<img src="{url_for('static', filename='images/python.jpg')}">'


@app.route('/sample-page')
def sample_page():
    return f"""<!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8">
                <title>Картинка Питона</title>
            </head>
            <body>
                <img src="{url_for('static', filename='images/python.jpg')}" alt="Python">
            </body>
            </html>
    """


@app.route('/sample-page2')
def sample_page2():
    with open('temp.html', 'r', encoding='utf-8') as html:
        return html.read()


# Так делать мы не будем
# x = 5
# @app.route('/1')
# def show_num():
#     global x
#     x += 1
#     return str(x)

# <string> - по умолчанию строка
# <int:number> - целое
# <float:number> - дес. дробь
# <path:p> - может содержать слэши для указания пути
# <uuid:id> - строка-идентификатор (16-байт в HEX-формате)
@app.route('/greeting/<string:user>/<int:id_num>')
def greeting(user, id_num):
    return f'Привет, {user} c id={id_num}'


@app.route('/get-user/<int:id_num>')
def get_user(id_num):
    con = sqlite3.connect('db/movies.sqlite')
    cur = con.cursor()
    query = f'SELECT name, city FROM users WHERE trip_id={id_num}'
    response = cur.execute(query)
    result = response.fetchone()
    # print(result)
    name, city = result
    cur.close()
    con.close()
    return f'''<table border="1">
    <tr>
    <td>ФИО</td>
    <td>Город</td>
    </tr>
    <tr>
    <td>{name}</td>
    <td>{city}</td>
    </tr>
    </table>'''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=debug)
