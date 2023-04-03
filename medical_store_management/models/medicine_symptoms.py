from odoo import models, fields, api
from datetime import date,datetime


class MedicineSymptoms(models.Model):
	_name = "medicine.symptoms"
	_rec_name = 'medicines_id'
	current_date = datetime.now().date().strftime('%Y-%m-%d')


	medicines_id = fields.Many2one('medicine.information', domain=[('expiry_date','>',current_date)],string='Medicine')
	symptoms_ids = fields.Many2many('health.symptoms',string='Symptoms')
	



	# @api.onchange('medicines_id')
	# def onchange_name(self):
	#     current_date = datetime.now().date().strftime('%Y-%m-%d')
	#     records = self.env['medicine.information'].search([('expiry_date','<',current_date)])
	#     medicine.symptoms.medicines_id = records.medicines_id     
