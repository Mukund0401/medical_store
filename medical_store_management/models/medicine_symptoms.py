from odoo import models, fields, api 

class MedicineSymptoms(models.Model):
	_name = "medicine.symptoms"
	_rec_name = 'medicines_id'

	medicines_id = fields.Many2one('medicine.information',string='Medicine')
	symptoms_ids = fields.Many2many('health.symptoms',string='Symptoms')