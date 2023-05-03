from odoo import models, fields     
class planeok_vol(models.Model): 
    _name = 'planeok.vol' 
    codi = fields.Integer('Código', required=True) 
    passatgers = fields.Integer('Pasajeros', required=True)     
    dataSortida = fields.Datetime('Fecha de Salida', required=True)     
    dataArrivada = fields.Datetime('Fecha de Llegada', required=True)