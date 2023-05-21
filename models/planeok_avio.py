from odoo import models, fields     
class planeok_avio(models.Model): 
    _name = 'planeok.avio' 
    name = fields.Char(compute='_get_name', string="Model_codi", readonly='True', store=False)
    codi = fields.Integer('Código', size=10, required=True) 
    imatge = fields.Image
    marca = fields.Integer('Marca', size=20, required=True)     
    model = fields.Char('Modelo', size=50, required=True)     
    maxVel = fields.Float('Velocidad Máxima', size=10, required=True)
    vols_ids = fields.One2many('planeok.vol', 'avio_id', string='Vols avio')

    def _get_name(self):
        for r in self:
            r.name = str(r.model) + " " + str(r.codi)

    