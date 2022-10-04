from odoo import api, fields, models
class Pista(models.Model):
    _name = 'Registro_corse'
    _description = "Corsa"
    _rec_name = 'ID_pista'

    ID_pista = fields.Char(string='ID_pista', required=True, readonly=True, default='New')
    Nome = fields.Char(string= 'nome')
    Lunghezza = fields.Float(string= 'lunghezza')
    Tipologia = fields.Selection([('Grande'),('Piccola')], required=True, default='new')
    
def create(self, vals):
    if vals.get('ID_pista','New') == 'New':
        vals['ID_pista'] = self.env['ir.sequence'].next_by_code('registro_corse.sequence')
    result = super(Pista, self).create(vals)
    return result


    @api.model
