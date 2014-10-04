from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from usuario_app.model import Usuario

__author__ = 'Danilo'


@no_csrf
def index(_handler, _logged_user, _resp, usuario):
    # verificar 1 acesso
    query = Usuario.query(Usuario.email == usuario)
    usuario_cadastrado = query.fetch(1)

    # usuario ja cadastrado
    if usuario_cadastrado:
        url = r'/usuarios/admin/edit/' + str(usuario_cadastrado[0].key.id())
        #resp.write(usuario_cadastrado[0].key.id())
    else:
        url = r'/usuarios/admin/new'

    _handler.redirect(url)
    return TemplateResponse()
