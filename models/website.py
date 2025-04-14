from odoo import models, fields

class Website(models.Model):
    _inherit = 'website'

    mail_server_id = fields.Many2one('ir.mail_server', string='Outgoing Mail Server',
                                     help="Specific outgoing mail server for this website")
