from odoo import models, fields     
class planeok_aeroport(models.Model): 
    _name = 'planeok.aeroport' 
    codi = fields.Integer('Código', required=True) 
    nom = fields.Char('Nombre', required=True) 
    ciutat = fields.Char('Ciudad', required=True)     
    pais = fields.Char('País', required=True)
    latitud = fields.Float('Latitud', required=True)
    longuitud = fields.Float('Longuitud', required=True)