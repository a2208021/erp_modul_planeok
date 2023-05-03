from odoo import models, fields     
class planeok_avio(models.Model): 
    _name = 'planeok.avio' 
    codi = fields.Integer('Código', required=True) 
    marca = fields.Integer('Marca', required=True)     
    model = fields.Char('Modelo', required=True)     
    maxVel = fields.Float('Velocidad Máxima', required=True)