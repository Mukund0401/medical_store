from odoo import models, fields


class MadicineInformation(models.Model):
	_name = "madicine.information"

	madicine_name = fields.Char(string="Name")
	madicine_stock = fields.Char(string='Madicine Stock')
	reference_no = fields.Char(string="Reference Number")
	company_name = fields.Char(string="Company Name")
	is_major = fields.Boolean(string="Is Major?")
	expiry_month = fields.Integer(string="Expiry Month")
	manufacture_date = fields.Date(string="Manufacture Date")
	symptoms_information_id = fields.Many2one('health.symptoms',string='symptoms')
	remaining_month = fields.Integer(string="Remaining Motnth" ,compute="_compute_remaining_month")
	dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")

	def _compute_remaining_month(self):
		for rec in self:
			rec.remaining_month = 10

	def action_view_madicine_stock(self):
			stock = self.env['health.symptoms'].search(["health.symptoms",'=',self.madicine_stock])
			action =  {
			    "type": "ir.actions.act_window",
			    "res_model": "health.symptoms",
			    "domain": [('name', '=', self.name)],
			    "name": ("Stock"),
			    'view_mode': 'tree,form'
			}
			return action


			



