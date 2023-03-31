from odoo import models, fields


class HealthSymptoms(models.Model):
	_name = "health.symptoms"

	name = fields.Char(string="Name")
	medicine_ids = fields.One2many('medicine.information','symtops_id',string='medicine Id')

		

	

