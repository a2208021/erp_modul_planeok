from odoo import models, fields     
class planeok_aeroport(models.Model): 
    _name = 'planeok.aeroport' 
    codi = fields.Integer('Código', size=20, required=True) 
    name = fields.Char(compute='_get_name', string="Nom", readonly='true', store=False)
    nom = fields.Char('Nombre', size=200, required=True) 
    ciutat = fields.Char('Ciudad', size=200, required=True)     
    pais = fields.Char('País', size=100, required=True)
    latitud = fields.Float('Latitud', size=50, required=True)
    longuitud = fields.Float('Longuitud', size=50, required=True)
    vols_desti_ids = fields.One2many('planeok.vol', 'aeroport_desti_id', string='Vols desti')
    vols_origen_ids = fields.One2many('planeok.vol', 'aeroport_origen_id', string='Vols origen')

    def _get_name(self):
        for r in self:
            r.name = str(r.nom)