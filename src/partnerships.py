```python
class Partnership:
    def __init__(self, partner_id, partner_type, partnership_date):
        self.partner_id = partner_id
        self.partner_type = partner_type
        self.partnership_date = partnership_date

    def get_partner_details(self):
        return {
            "partner_id": self.partner_id,
            "partner_type": self.partner_type,
            "partnership_date": self.partnership_date
        }

class Partnerships:
    def __init__(self):
        self.partnerships = []

    def add_partnership(self, partner_id, partner_type, partnership_date):
        new_partnership = Partnership(partner_id, partner_type, partnership_date)
        self.partnerships.append(new_partnership)

    def get_all_partnerships(self):
        return [partnership.get_partner_details() for partnership in self.partnerships]

    def find_partnership(self, partner_id):
        for partnership in self.partnerships:
            if partnership.partner_id == partner_id:
                return partnership.get_partner_details()
        return None
```