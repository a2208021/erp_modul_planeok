from odoo import models, fields     
class planeok_vol(models.Model): 
    _name = 'planeok.vol' 
    name = fields.Char(compute='_get_name', string="Codi_vol", readonly='True', store=False)
    codi = fields.Integer('Código', size=20, required=True) 
    passatgers = fields.Integer('Pasajeros', size=20, required=True)     
    dataSortida = fields.Datetime('Fecha de Salida', required=True)     
    dataArrivada = fields.Datetime('Fecha de Llegada', required=True)
    avio_id = fields.Many2one('planeok.avio', string='Avio')
    pilot_id = fields.Many2one('planeok.pilot', string='Pilot')
    aeroport_desti_id = fields.Many2one('planeok.aeroport', string='Aeroport desti')
    aeroport_origen_id = fields.Many2one('planeok.aeroport', string='Aeroport origen')


    def _get_name(self):
        for r in self:
            r.name = str(r.codi)

    