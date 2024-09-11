# -*- coding: utf-8 -*-
# from odoo import http


# class SrtMaterials(http.Controller):
#     @http.route('/srt_materials/srt_materials/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/srt_materials/srt_materials/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('srt_materials.listing', {
#             'root': '/srt_materials/srt_materials',
#             'objects': http.request.env['srt_materials.srt_materials'].search([]),
#         })

#     @http.route('/srt_materials/srt_materials/objects/<model("srt_materials.srt_materials"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('srt_materials.object', {
#             'object': obj
#         })
