from odoo import models,fields,api
from datetime import date,datetime
import calendar
from odoo.exceptions import ValidationError

class MedicineInformation(models.Model):
    _name = "medicine.information"
    _rec_name = "medicine_name"

    medicine_id = fields.Char(string="Medicine Id", readonly=True)
    medicine_name = fields.Char(string="Medicine Name")
    reference_no = fields.Char(string="Reference Number")
    company_name = fields.Char(string="Company Name",required=True)
    is_major = fields.Boolean(string="Is Major?")
    expiry_date = fields.Date(string="Expiry Date")
    manufacture_date = fields.Date(string="Manufacture Date")
    # symptoms_information_id = fields.Many2one('health.symptoms',string='symptoms')
    remaining_month = fields.Integer(string="Remaining Motnth" ,compute="_compute_remaining_month")
    dosage_form = fields.Selection([('tablet','Tablet'),('capsule','Capsule'),('liquid','Liquid')],string="Dosage form")

    # symtops_id = fields.Many2one('health.symptoms',string="Symptoms Id")

    
    @api.onchange("medicine_name")
    def onchange_name(self):
        if not self.medicine_name:
            return
        self.company_name = "Zydus"

    # @api.onchange('medicine_name')
    # def onchange_name(self):
    #     current_date = datetime.now().date().strftime('%Y-%m-%d')
    #     records = self.env['medicine.information'].search([('expiry_date','<',current_date)])
    #     self.medicine_name = records.medicine_name     


    @api.depends("expiry_date")
    def _compute_remaining_month(self):
        for rec in self:
            rec.remaining_month = 0
            if rec.manufacture_date:
                today_date =date.today()
                rec.remaining_month=today_date.month - rec.manufacture_date.month


    # def action_symptoms_info(self):
    #     return {
    #         "type": "ir.actions.act_window",
    #         "res_model": "health.symptoms",
    #         "name":("Symptoms"),
    #         'view_mode': 'tree,form'
    #     }


    def action_view_medicine_symptoms(self):
        symptoms = self.env['medicine.symptoms'].search(
            [('medicines_id', '=', self.id)])
        action =  {
            "type": "ir.actions.act_window",
            "res_model": "medicine.symptoms",
            "domain": [('medicines_id', '=', self.id)],
            "name": ("Symptoms"),
            'view_mode': 'tree,form'
        }
        return action


    

    @api.model
    def create(self, vals):
        if not vals.get('medicine_id'):
            month = calendar.month_name[date.today().month]
            current_date = datetime.now().date().strftime('%Y-%m-%d')
            print(current_date)
            print(type(current_date))
            # print(":::::::::::::",vals["expiry_date"])
            # print(type(vals["expiry_date"]))
            records = self.env['medicine.information'].search([('expiry_date','>',current_date)])
            print(":::::::::::::",records)
            for rec in records:
                print(":::::::",rec.medicine_name)
            # seq = self.env["ir.sequence"].next_by_code('medicine.information')
            # vals['medicine_id'] = seq[0:3]+'/'+month[0:3]+'/'+seq[6:]
            
        return super(MedicineInformation,self).create(vals)

    def write(self,vals):
        if 'expiry_date' in vals:
            current_date = datetime.now().date().strftime('%Y-%m-%d')
            # expiry_date_format = datetime.strptime(vals['expiry_date'], '%Y-%m-%d')
            if vals.get('expiry_date')< current_date:
                raise ValidationError("You Can't Change Expiry Date")
        return super(MedicineInformation, self).write(vals)

    def name_get(self):
        result = []
        for medicine in self:
            if medicine.expiry_date:
                name = medicine.medicine_name + ' [ '+str(medicine.expiry_date) + ' ]'
                result.append((medicine.id,name))
            else:
                name = medicine.medicine_name
                result.append((medicine.id,name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        if name:
            args = ['|',('medicine_name',operator,name),('reference_no',operator,name)]+args
        return self._search(args,limit=limit,access_rights_uid=name_get_uid)

    @api.model
    def default_get(self,fields):
        res = super(MedicineInformation,self).default_get(fields)
        if 'company_name' in fields:
            res['company_name']='Aktiv'
        return res

    # def search(self, vals):
    #     records = self.env['medicine.information'].search([('expiry_date','<','current_date')])
    #     print("::::::::::::::::::",records)
    #     return records

