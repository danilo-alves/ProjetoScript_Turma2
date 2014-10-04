from google.appengine.ext.db import DateProperty
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property
from tekton import router

__author__ = 'Danilo'


@no_csrf
def index(_handler, usuario):
    contexto = {'config_geral_path' : router.to_path(salvar_configuracao)}
    return TemplateResponse(contexto)

def salvar_configuracao(usuario, blog, nome_completo, alias):
    usr = Usuario(usuario=usuario, blog=blog, nome_completo=nome_completo, alias=alias)
    usr.put()