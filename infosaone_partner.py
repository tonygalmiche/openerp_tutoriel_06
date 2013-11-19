# -*- coding: utf-8 -*-

from osv import osv
from osv import fields


class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = 'res.partner'
    
    _columns = {  
        'prenom': fields.char("Prénom", size=255)
    }

res_partner()


