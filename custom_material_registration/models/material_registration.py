# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class MaterialRegistration(models.Model):
  _name = 'material.registration'
  _description = 'Material Registration'
  _inherit = ['mail.thread', 'mail.activity.mixin']

  name = fields.Char(string="Name", required=True, tracking=True)
  code = fields.Char(string="Code", required=True, tracking=True)
  material_type = fields.Selection(string="Type", required=True, tracking=True,
                                   selection=[('fabric', 'Fabric'), ('jeans', 'Jeans'), ('cotton', 'Cotton')])
  price_unit = fields.Monetary(string="Price", tracking=True, required=True) 
  currency_id = fields.Many2one('res.currency', string="Currency", required=True, default=lambda self: self.env.company.currency_id)
  supplier_id = fields.Many2one('res.partner', string="Material's Supplier", required=True, tracking=True)

  @api.constrains('price_unit')
  def constraints_price_unit_minimum(self):
      for rec in self:
          if rec.price_unit < 100:
              raise ValidationError(_("The buy price cannot be less than 100, please change the price!"))
