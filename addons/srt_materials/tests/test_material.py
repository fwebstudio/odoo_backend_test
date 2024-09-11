from odoo.tests.common import TransactionCase


class TestMaterial(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestMaterial, self).setUp()

        self.supplier = self.env['res.partner'].create({
            'name': 'Kazuki Takagawa'
        })
        self.res_material = self.env['res.material'].create({
            'code': 'TEST001',
            'name': 'Testing Materials',
            'type': 'cotton',
            'price': 140,
            'supplier': self.supplier.id,
        })

    def test_field_values(self):
        # Test the values of fields
        res_material = self.res_material
        self.assertRecordValues(res_material,[{
            'code': 'TEST001',
            'name': 'Testing Materials',
            'type': 'cotton',
            'price': 140,
            'supplier': self.supplier.id
        }])

    def test_field_price_greater_than_100(self):
        self.assertGreaterEqual(self.res_material.price, 100,
                         "Material type value is incorrect")