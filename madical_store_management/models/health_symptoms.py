from odoo import models, fields


class HealthSymptoms(models.Model):
	_name = "health.symptoms"

	name = fields.Char(string="Name")

		



