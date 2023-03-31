from odoo import models, fields


class HealthSymptoms(models.Model):
	_name = "health.symptoms"

	name = fields.Char(string="Name")




	# def action_medicine_count_info(self):
	#     medicine = self.env['medicine.information'].search_count([])
	#     print(":::::::::",medicine)
	#     return {
	#         "type": "ir.actions.act_window",
	#         "res_model": "medicine.information",
	#         "name":("medicine"),
	#         'view_mode': 'tree,form'
	#     }
        

	

