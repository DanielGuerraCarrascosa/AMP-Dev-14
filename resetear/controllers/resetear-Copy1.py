# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class Resetear(http.Controller):
    @http.route('/resetear', auth='public', website=True)
    def resetear(self, **kw):
        
        emailRecibido = request.params['email']
        
        resetear = http.request.env['res.partner'].search([('email', '=', emailRecibido)])
        
        """return "Nombre de la persona del correo: " + resetear.name"""
        
        """self.mapped('partner_id').signup_prepare(signup_type="reset", expiration=False)"""
    
        template = http.request.env.ref('auth_signup.reset_password_email')
        
        assert template._name == 'mail.template'
        
        template_values = {
            'email_to': resetear.email,
            'email_cc': False,
            'auto_delete': True,
            'partner_to': False,
            'scheduled_date': False,
        }
        template.write(template_values)
        
        template.send_mail(resetear.id, force_send=False, raise_exception=True)
            
        """template.send_mail(resetear.id, force_send=False, raise_exception=True)"""
            
        
        return "Nombre de la persona del correo: " + resetear.name
    
        """
        create_mode = bool(self.env.context.get('create_user'))
        
        expiration = False if create_mode else now(days=+1)
        
        self.mapped('partner_id').signup_prepare(signup_type="reset", expiration=expiration)
        
        template = False
        
        if create_mode:
            try:
                template = self.env.ref('auth_signup.set_password_email', raise_if_not_found=False)
            except ValueError:
                pass
        
        if not template:
            template = self.env.ref('auth_signup.reset_password_email')
        assert template._name == 'mail.template'
        
        template_values = {
            'email_to': '${object.email|safe}',
            'email_cc': False,
            'auto_delete': True,
            'partner_to': False,
            'scheduled_date': False,
        }
        template.write(template_values)
        
        for user in self:
            if not user.email:
                raise UserError(_("Cannot send email: user %s has no email address.", user.name))
            
            with self.env.cr.savepoint():
                force_send = not(self.env.context.get('import_file', False))
                template.send_mail(user.id, force_send=force_send, raise_exception=True)
            _logger.info("Password reset email sent for user <%s> to <%s>", user.login,user.email)
            
            
            """