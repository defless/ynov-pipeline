from bottle import template


def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def add(a, b):
    """Return the sum of two url params as JSON.
    Usage examples:
    >>> add(4, 2)
    {'result': 6}
    """
    return {'result': int(a) + int(b)}
