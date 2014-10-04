from gaecookie.decorator import no_csrf

__author__ = 'Danilo'

@no_csrf
def index(_resp):
    _resp.write("A")
