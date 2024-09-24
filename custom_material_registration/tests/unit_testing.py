# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class TestMaterialRegistration(TransactionCase):

    def setUp(self):
        super(TestMaterialRegistration, self).setUp()
        # Create a supplier for testing
        self.supplier = self.env['res.partner'].create({
            'name': 'Test Supplier',
            'supplier_rank': 1,
        })

    def test_material_creation(self):
        # Test creating a material
        material = self.env['material.registration'].create({
            'name': 'Test Material',
            'code': 'TM001',
            'material_type': 'fabric',
            'price_unit': 150,
            'supplier_id': self.supplier.id,
        })
        self.assertTrue(material.id)

    def test_material_price_constraint(self):
        # Test constraint for price
        with self.assertRaises(ValidationError):
            self.env['material.registration'].create({
                'name': 'Cheap Material',
                'code': 'CM001',
                'material_type': 'cotton',
                'price_unit': 50,  # This should raise a ValidationError
                'supplier_id': self.supplier.id,
            })

    def test_material_update(self):
        # Create a material and update it
        material = self.env['material.registration'].create({
            'name': 'Update Material',
            'code': 'UM001',
            'material_type': 'jeans',
            'price_unit': 200,
            'supplier_id': self.supplier.id,
        })
        material.write({'price_unit': 250})
        self.assertEqual(material.price_unit, 250)

    def test_material_deletion(self):
        # Create a material and delete it
        material = self.env['material.registration'].create({
            'name': 'Delete Material',
            'code': 'DM001',
            'material_type': 'fabric',
            'price_unit': 300,
            'supplier_id': self.supplier.id,
        })
        material_id = material.id
        material.unlink()
        self.assertFalse(self.env['material.registration'].search([('id', '=', material_id)]))
