# -*- coding: utf-8 -*-
# from odoo import http


# class Corsa(http.Controller):
#     @http.route('/corsa/corsa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/corsa/corsa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('corsa.listing', {
#             'root': '/corsa/corsa',
#             'objects': http.request.env['corsa.corsa'].search([]),
#         })

#     @http.route('/corsa/corsa/objects/<model("corsa.corsa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('corsa.object', {
#             'object': obj
#         })
