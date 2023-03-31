from odoo import models,fields,api
from datetime import date,datetime
import calendar
from odoo.exceptions import ValidationError

class MedicineInformation(models.Model):
    _name = "medicine.information"

    medicine_id = fields.Char(string="Medicine Id", readonly=True)
    medicine_name = fields.Char(string="Medicine Name")
    reference_no = fields.Char(string="Reference Number")
    company_name = fields.Char(string="Company Name",required=True)
    is_major = fields.Boolean(string="Is Major?")
    expiry_date = fields.Date(string="Expiry Date")
    manufacture_date = fields.Date(string="Manufacture Date")
    symptoms_information_id = fields.Many2one('health.symptoms',string='symptoms')
    remaining_month = fields.Integer(string="Remaining Motnth" ,compute="_compute_remaining_month")
    dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")
    symtops_id = fields.Many2one('health.symptoms',string="Symptoms Id")

    
    @api.onchange("medicine_name")
    def onchange_name(self):
        if not self.medicine_name:
            return
        self.company_name = "Zydus"

    @api.depends("expiry_date")
    def _compute_remaining_month(self):
        for rec in self:
            rec.remaining_month = 0
            if rec.manufacture_date:
                today_date =date.today()
                rec.remaining_month=today_date.month - rec.manufacture_date.month


    def action_symptoms_info(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "health.symptoms",
            "name":("symptoms"),
            'view_mode': 'tree,form'
        }

    @api.model
    def create(self, vals):
        if not vals.get('medicine_id'):
            month = calendar.month_name[date.today().month]
            current_date = datetime.now().date().strftime('%Y-%m-%d')
            print(current_date)
            records = self.env['medicine.information'].search([('expiry_date','>',current_date)])
            print("::::::::::::::::::",records)
            seq = self.env["ir.sequence"].next_by_code('medicine.information')
            vals['medicine_id'] = seq[0:3]+'/'+month[0:3]+'/'+seq[6:]
        return super(MedicineInformation,self).create(vals)

    def write(self,vals):
        if 'expiry_date' in vals:
            current_date = datetime.now().date().strftime('%Y-%m-%d')
            # expiry_date_format = datetime.strptime(vals['expiry_date'], '%Y-%m-%d')
            if vals.get('expiry_date')< current_date:
                raise ValidationError("You Can't Change Expiry Date")
        return super(MedicineInformation, self).write(vals)


    # def search(self, vals):
    #     records = self.env['medicine.information'].search([('expiry_date','<','current_date')])
    #     print("::::::::::::::::::",records)
    #     return records

