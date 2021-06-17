# -*- coding: utf-8 -*-

import logging

from ast import literal_eval
from collections import defaultdict
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools.misc import ustr

from odoo.addons.base.models.ir_mail_server import MailDeliveryException
from odoo.addons.auth_signup.models.res_partner import SignupError, now

_logger = logging.getLogger(__name__)

from odoo import http
from odoo.http import request

class Resetear(http.Controller):
    
    _inerit = 'ResUsers'
    
    @http.route('/resetear', auth='public', website=True)
    def resetear(self, **kw):
        
        emailRecibido = request.params['email']
        
        user = http.request.env['res.users'].search([('email', '=', emailRecibido)])
        
        """ create signup token for each user, and send their signup url by email """
        if http.request.env.context.get('install_mode', False):
            return
        # prepare reset password signup
        create_mode = bool(http.request.env.context.get('create_user'))

        # no time limit for initial invitation, only for reset password
        expiration = False if create_mode else now(days=+1)

        # send email to users with their signup url
        template = False
        if create_mode:
            try:
                template = http.request.env.ref('auth_signup.set_password_email', raise_if_not_found=False)
            except ValueError:
                pass
        if not template:
            template = http.request.env.ref('auth_signup.reset_password_email')
        assert template._name == 'mail.template'

        template_values = {
            'email_to': '${object.email|safe}',
            'email_cc': False,
            'auto_delete': True,
            'partner_to': False,
            'scheduled_date': False,
        }
        template.write(template_values)

        force_send = not(http.request.env.context.get('import_file', False))
        template.send_mail(user.id, force_send=force_send, raise_exception=True)
        
        return 'okey'