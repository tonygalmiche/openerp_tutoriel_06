# -*- coding: utf-8 -*-

from osv import osv
from osv import fields


# Le nom de la class doit être le même que le nom de la class à surcharger
class res_partner(osv.osv):

    # Le nom du modèle doit être le même que celui à surcharger
    _name = "res.partner"

    # Cette ligne permet d'indiquer que l'on souhaite surcharger cette class
    _inherit = 'res.partner'
    
    # Ce tableau permet d'indiquer les champs à ajouter au modèle de base
    _columns = {  
        'prenom': fields.char("Prénom", size=255)
    }


# Chargement de la class
res_partner()


