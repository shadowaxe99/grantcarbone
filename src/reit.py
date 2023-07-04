```python
class REIT:
    def __init__(self, reit_id, reit_name, reit_value):
        self.reit_id = reit_id
        self.reit_name = reit_name
        self.reit_value = reit_value

    def get_reit_details(self):
        return {
            "reit_id": self.reit_id,
            "reit_name": self.reit_name,
            "reit_value": self.reit_value
        }

    def update_reit_value(self, new_value):
        self.reit_value = new_value

    def __str__(self):
        return f"REIT ID: {self.reit_id}, Name: {self.reit_name}, Value: {self.reit_value}"
```