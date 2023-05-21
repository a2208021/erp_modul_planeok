from odoo import models, fields     
class planeok_pilot(models.Model): 
    _name = 'planeok.pilot'
    codi = fields.Integer('Código', size=20, required=True)
    name = fields.Char(compute='_get_name', string="Nom_complet", readonly='True', store=False)
    nom = fields.Char('Nombre', size=50, required=True)     
    cognoms = fields.Char('Apellidos', size=200, required=True)     
    nif = fields.Char('NIF', size=10, required=True)
    telf = fields.Char('Tlfn.', size=20, required=True)     
    email = fields.Char('Email', size=200, required=True)
    vols_ids = fields.One2many('planeok.vol', 'pilot_id', string='Vols pilot')

    def _get_name(self):
        for r in self:
            r.name = str(r.nom) + " " + str(r.cognoms)