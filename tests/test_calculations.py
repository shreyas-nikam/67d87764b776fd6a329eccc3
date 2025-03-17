import unittest
from calculations import compute_financials

class TestCalculations(unittest.TestCase):
    def test_compute_financials(self):
        result = compute_financials(100000, 100000, 50000, 50000, 15000, 50, 40000, 25, 65)
        self.assertIn("Total Financial Wealth", result)
        self.assertIn("Estimated Value of Human Capital", result)
        self.assertIn("Estimated Value of Liabilities", result)
        self.assertIn("Estimated Net Worth", result)
        self.assertIn("Initial Consumption", result)
        self.assertIn("Bequest", result)
        self.assertIn("Current / Implied Allocations", result)
        self.assertIn("Quasi-Recommended Allocations", result)

if __name__ == "__main__":
    unittest.main()
