import unittest
from calculations import compute_financials

class TestIntegration(unittest.TestCase):
    def test_integration_calculation_and_visualization_data(self):
        financials = compute_financials(100000, 100000, 50000, 50000, 15000, 50, 40000, 25, 65)
        total_financial_wealth = 100000 + 100000 + 50000
        human_capital = 50000 * (65 - 25)
        expected_net_worth = total_financial_wealth + human_capital - (human_capital * 0.5)
        self.assertAlmostEqual(financials["Estimated Net Worth"], expected_net_worth, places=2)

if __name__ == "__main__":
    unittest.main()
