```python
import unittest
from src.scalability import expand_offerings, hire_personnel, establish_partnership

class TestScalability(unittest.TestCase):

    def setUp(self):
        self.partner_id = 1
        self.role = "Investment Advisor"

    def test_expand_offerings(self):
        result = expand_offerings()
        self.assertTrue(result)

    def test_hire_personnel(self):
        result = hire_personnel(self.role)
        self.assertEqual(result, f"{self.role} has been hired.")

    def test_establish_partnership(self):
        result = establish_partnership(self.partner_id)
        self.assertEqual(result, f"Partnership with partner {self.partner_id} has been established.")

if __name__ == '__main__':
    unittest.main()
```