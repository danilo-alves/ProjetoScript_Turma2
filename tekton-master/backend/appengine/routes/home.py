# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required


@login_not_required
@no_csrf
def index(_handler, _logged_user):
    if _logged_user:
        url = r'/usuario/index/' + _logged_user.name
        _handler.redirect(url)
    return TemplateResponse()