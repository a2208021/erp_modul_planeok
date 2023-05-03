from odoo import models, fields     
class planeok_pilot(models.Model): 
    _name = 'planeok.pilot' 
    codi = fields.Integer('Código', required=True) 
    nom = fields.Char('Nombre', required=True)     
    cognoms = fields.Char('Apellidos', required=True)     
    nif = fields.Char('NIF', required=True)
    telf = fields.Char('Tlfn.', required=True)     
    email = fields.Char('Email', required=True)
