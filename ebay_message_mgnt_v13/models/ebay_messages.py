
from odoo import api, fields, models, _

import logging

logger = logging.getLogger('list_item')


class ebay_messages(models.Model):
    _name = "ebay.messages"
    # _inherit = ['mail.thread', 'ir.needaction_mixin']
    _inherit = ['mail.thread']
    _rec_name = 'message_id'

    def write(self, values):
        if values.get('assigned_user'):
            values.update({'state': 'pending'})
        print("-==values==", values)
        return super(ebay_messages, self).write(values)

    def reply(self):
        view_ref = self.env['ir.model.data'].get_object_reference('ebay_message_mgnt_v13',
                                                                  'compose_messages_on_ebay_wiz')
        view_id = view_ref and view_ref[1] or False,
        context = self._context
        return {
            'type': 'ir.actions.act_window',
            'name': _('Compose Message'),
            'res_model': 'compose.message',
            'view_mode': 'form',
            'view_id': view_id,
            'target': 'new',
            'nodestroy': True,
            'context': context
        }

    name = fields.Char('Subject')
    shop_id = fields.Many2one('sale.shop', 'Shop')
    message_id = fields.Char('MessageID', size=256)
    external_msg_id = fields.Char('ExternalMessageID')
    send_to_name = fields.Char('SendToName', size=256)
    sender = fields.Many2one('res.partner', 'Sender', size=256)
    sender_email = fields.Char('Sender Email')
    recipient_user_id = fields.Many2one('res.partner', 'RecipientID')
    item_id = fields.Char('ItemID')
    expiry_on_date = fields.Datetime('ExpirationDate')
    body = fields.Text('Body')
    state = fields.Selection([('unassigned', 'Unassigned'), ('pending', 'Pending'), ('solved', 'Solved')], 'State',
                             default='unassigned')
    assigned_user = fields.Many2one('res.users', 'Assigned User', size=256)
