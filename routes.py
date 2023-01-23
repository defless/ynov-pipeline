from bottle import route, run
from controllers import add, index


@route('/hello/<name>')
def route_index(name):
    return index(name)


@route('/add/<a>/<b>')
def route_add(a, b):
    return add(a, b)


run(host='localhost', port=8080, reloader=True)
