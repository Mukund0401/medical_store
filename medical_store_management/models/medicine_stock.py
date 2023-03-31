from odoo import models, fields

class medicineStock(models.Model):
	_name = "medicine.stock"

	medicine_name = fields.Char(string="Name")
	medicine_stock = fields.Integer(string='medicine Stock')
	remaining = fields.Integer(string="Remaining")