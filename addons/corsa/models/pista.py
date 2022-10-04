from odoo import api, fields, models
class Pista(models.Model):
    _name = 'Pista'
    _description = 'Pista'
    _rec_name = 'ID_pista'

    ID_pista = fields.Char(string='ID_pista', required=True)
    Nome = fields.Char(string= 'nome')
    Lunghezza = fields.Float(string= 'lunghezza')
    Tipologia = fields.Selection([('grande','Grande'),('piccola','Piccola')], required=True)
    

   


  
 