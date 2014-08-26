__author__ = 'Danilo'


def index(_resp):
    _resp.write("Fuck the police!")
    return RedirectResponse("/")