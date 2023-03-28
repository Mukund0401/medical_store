from odoo import models, fields

class MadicineStock(models.Model):
	_name = "madicine.stock"

	madicine_stock = fields.Integer(string='Madicine Stock')