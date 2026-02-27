from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    disciplinary_action_ids = fields.One2many(
        comodel_name='hr.disciplinary.action',
        inverse_name='employee_id',
        string='Disciplinary Cases',
    )
    verbal_count = fields.Integer(string='Verbal Warnings', compute='_compute_decision_counts')
    written_count = fields.Integer(string='Second Written Warnings', compute='_compute_decision_counts')
    last_count = fields.Integer(string='Last Written Warnings', compute='_compute_decision_counts')

    disciplinary_action_count = fields.Integer(
        string='Disciplinary Cases Count',
        compute='_compute_decision_counts',
    )

    def _compute_decision_counts(self):
        # Initialize counts
        for employee in self:
            employee.verbal_count = 0
            employee.written_count = 0
            employee.last_count = 0
            employee.disciplinary_action_count = 0

        # Efficiently read counts grouped by employee and decision
        data = self.env['hr.disciplinary.action'].read_group(
            [('employee_id', 'in', self.ids)],
            ['employee_id', 'decision'],
            ['employee_id', 'decision'],
            lazy=False
        )

        # Map results to employees
        for row in data:
            employee = self.browse(row['employee_id'][0])
            decision = row['decision']
            count = row['__count']
            
            employee.disciplinary_action_count += count
            if decision == 'verbal':
                employee.verbal_count = count
            elif decision == 'written':
                employee.written_count = count
            elif decision == 'last':
                employee.last_count = count

    def action_open_disciplinary_actions(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Disciplinary Cases',
            'res_model': 'hr.disciplinary.action',
            'view_mode': 'list,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
        }
