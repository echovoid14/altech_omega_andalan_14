# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from werkzeug.exceptions import NotFound
import json

class MaterialRegistrationController(http.Controller):

    @http.route('/materials', auth='public', type='http', methods=['GET'], csrf=False)
    def list_materials(self, material_type=None):
        domain = []
        if material_type:
            domain.append(('material_type', '=', material_type))
        
        materials = request.env['material.registration'].sudo().search(domain)
        result = []
        for material in materials:
            result.append({
                'id': material.id,
                'name': material.name,
                'code': material.code,
                'material_type': material.material_type,
                'price_unit': material.price_unit,
                'supplier': material.supplier_id.name
            })

        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/material/<int:material_id>', auth='public', type='http', methods=['GET'], csrf=False)
    def view_material(self, material_id):
        material = request.env['material.registration'].sudo().browse(material_id)
        if not material.exists():
            raise NotFound()

        result = {
            'id': material.id,
            'name': material.name,
            'code': material.code,
            'material_type': material.material_type,
            'price_unit': material.price_unit,
            'supplier': material.supplier_id.name
        }

        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )

    @http.route('/material/update/<int:material_id>', auth='user', type='http', methods=['POST'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['material.registration'].sudo().browse(material_id)
        if not material.exists():
            raise NotFound()
        
        material.write({
            'name': kwargs.get('name', material.name),
            'code': kwargs.get('code', material.code),
            'material_type': kwargs.get('material_type', material.material_type),
            'price_unit': kwargs.get('price_unit', material.price_unit),
            'supplier_id': kwargs.get('supplier_id', material.supplier_id.id),
        })

        result = {'status': 'success', 'message': 'Material updated successfully'}
        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )
    @http.route('/material/delete/<int:material_id>', auth='user', type='http', methods=['POST'], csrf=False)
    def delete_material(self, material_id):
        material = request.env['material.registration'].sudo().browse(material_id)
        if not material.exists():
            raise NotFound()

        material.unlink()
        result = {'status': 'success', 'message': 'Material deleted successfully'}
        return request.make_response(
            json.dumps(result),
            headers=[('Content-Type', 'application/json')]
        )
