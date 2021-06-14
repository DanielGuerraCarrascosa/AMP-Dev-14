# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class Resetear(http.Controller):
    @http.route('/resetear', auth='public', website=True)
    def resetear_password(self, **kw):
        return "Recibo correo: " + request.params['email']
    