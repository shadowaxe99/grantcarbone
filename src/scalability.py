```python
from src.partnerships import Partnership
from src.user import InvestmentAdvisor, CustomerSupport

class Scalability:
    def __init__(self):
        self.investment_offerings = []
        self.partnerships = []
        self.team = []

    def expand_offerings(self, offering):
        self.investment_offerings.append(offering)
        print(f"New offering {offering} added.")

    def hire_personnel(self, role):
        if role == "Investment Advisor":
            new_member = InvestmentAdvisor()
        elif role == "Customer Support":
            new_member = CustomerSupport()
        else:
            print("Invalid role.")
            return
        self.team.append(new_member)
        print(f"New {role} hired.")

    def establish_partnership(self, partner_id, partner_type, partnership_date):
        new_partnership = Partnership(partner_id, partner_type, partnership_date)
        self.partnerships.append(new_partnership)
        print(f"New partnership with {partner_type} established.")
```