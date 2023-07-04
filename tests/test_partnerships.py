import unittest
from src import partnerships

class TestPartnerships(unittest.TestCase):

    def setUp(self):
        self.partnership_data = {
            "partner_id": "P123",
            "partner_type": "Real Estate Agency",
            "partnership_date": "2021-01-01"
        }
        self.partnership = partnerships.Partnership(self.partnership_data)

    def test_partner_id(self):
        self.assertEqual(self.partnership.partner_id, "P123")

    def test_partner_type(self):
        self.assertEqual(self.partnership.partner_type, "Real Estate Agency")

    def test_partnership_date(self):
        self.assertEqual(self.partnership.partnership_date, "2021-01-01")

    def test_create_partnership(self):
        new_partnership_data = {
            "partner_id": "P124",
            "partner_type": "Property Management Company",
            "partnership_date": "2021-02-01"
        }
        new_partnership = partnerships.Partnership(new_partnership_data)
        self.assertEqual(new_partnership.partner_id, "P124")
        self.assertEqual(new_partnership.partner_type, "Property Management Company")
        self.assertEqual(new_partnership.partnership_date, "2021-02-01")

if __name__ == '__main__':
    unittest.main()