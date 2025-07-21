from flask import Flask, request, make_response, redirect, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'just_secret_key'


@app.route('/')
def index():
    return redirect('/cookie_test')


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))

    if visit_count:
        res = make_response(f'Вы посетили эту страницу {visit_count} раз(а).')
        res.set_cookie('visit_count', str(visit_count + 1),
                       max_age=60 * 60 * 24 * 30)
    else:
        res = make_response('Вы впервые тут у нас за этот месяц!')
        res.set_cookie('visit_count', '1',
                       max_age=60 * 60 * 24 * 30)
    return res


@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    print(visit_count)
    session['visit_count'] = visit_count + 1
    return make_response(
        f'Вы на этой странице {visit_count + 1} раз(а)'
    )


if __name__ == '__main__':
    app.run(host='localhost', port=8000)
