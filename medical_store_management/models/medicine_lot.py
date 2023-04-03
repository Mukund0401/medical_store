from odoo import models, fields, api


class MedicineLot(models.Model):
	_name = 'medicine.lot'

	name = fields.Char(string='Medicine Lot',readonly=True)
	medicine_id = fields.Many2one("medicine.information",string="Medicine Name")
	manufacture_date = fields.Date(string="Manufacture Date")
	expiry_date = fields.Date(string="Expiry Date")
	quantity = fields.Integer(string="Quatity")
	state_lot = fields.Selection(selection=[('draft', 'Expired'),('done', 'Not Expired'),], string='Status', required=True, readonly=True, copy=False, tracking=True, default='draft')




	@api.model
	def create(self, vals):
		if not vals.get('name'):
			seq = self.env["ir.sequence"].next_by_code('medicine.lot')
			vals['name'] = seq
			
		return super(MedicineLot,self).create(vals)