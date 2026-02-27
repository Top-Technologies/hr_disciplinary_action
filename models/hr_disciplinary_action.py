from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HrDisciplinaryAction(models.Model):
    _name = 'hr.disciplinary.action'
    _description = 'Disciplinary Action'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'name'
    _order = 'name desc'

    name = fields.Char(
        string='Reference',
        required=True,
        copy=False,
        readonly=True,
        default='New',
        tracking=True,
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Employee',
        required=True,
        tracking=True,
    )
    department_id = fields.Many2one(
        related='employee_id.department_id',
        string='Department',
        store=True,
        readonly=True,
    )
    incident_date = fields.Date(
        string='Incident Date',
        required=True,
        default=fields.Date.today,
        tracking=True,
    )
    # ── Incident Details Tab ──────────────────────────────────────────────────
    action_type = fields.Selection(
        selection=[
            ('misconduct', 'Misconduct'),
            ('absenteeism', 'Absenteeism'),
            ('insubordination', 'Insubordination'),
            ('negligence', 'Negligence'),
            ('other', 'Other'),
        ],
        string='Action Type',
        tracking=True,
    )
    severity = fields.Selection(
        selection=[
            ('minor', 'Minor'),
            ('major', 'Major'),
            ('critical', 'Critical'),
        ],
        string='Severity',
        tracking=True,
    )
    incident_description = fields.Text(string='Incident Description')

    # ── Investigation Tab ─────────────────────────────────────────────────────
    investigation_notes = fields.Text(string='Investigation Notes')
    attachment_ids = fields.Many2many(
        comodel_name='ir.attachment',
        relation='disciplinary_action_attachment_rel',
        column1='action_id',
        column2='attachment_id',
        string='Attachments',
    )

    # ── Employee Response Tab ─────────────────────────────────────────────────
    employee_response = fields.Text(string='Employee Response')
    response_date = fields.Date(string='Response Date')

    # ── Decision Tab ──────────────────────────────────────────────────────────
    decision = fields.Selection(
        selection=[
            ('verbal', 'Verbal  Written Warning'),
            ('written', 'Second Written Warning'),
            ('last', 'Last Written Warning'),
        ],
        string='Decision',
        tracking=True,
    )
    decision_date = fields.Date(string='Decision Date')
    decision_notes = fields.Text(string='Decision Notes')

    # ─────────────────────────────────────────────────────────────────────────
    # ORM Overrides
    # ─────────────────────────────────────────────────────────────────────────
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code(
                    'hr.disciplinary.action'
                ) or 'New'
        return super().create(vals_list)
