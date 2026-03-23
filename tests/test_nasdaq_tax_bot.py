import unittest
from unittest.mock import patch

from nasdaq_tax_bot import (
    CalculationInput,
    _calculate_tcs,
    calculate_investment_breakdown,
    list_us_market_companies,
    main,
)


class NasdaqTaxBotTests(unittest.TestCase):
    def test_tcs_applies_only_incremental_above_threshold(self):
        tcs = _calculate_tcs(
            remittance_so_far_inr=650000,
            amount_inr=100000,
            threshold_inr=700000,
            tcs_rate=0.20,
        )
        self.assertEqual(tcs, 10000.0)

    def test_calculate_breakdown_contains_expected_keys(self):
        payload = calculate_investment_breakdown(
            CalculationInput(
                amount_inr=100000,
                platform="vested",
                expected_return_pct=0.10,
                dividend_yield_pct=0.01,
                holding_period_years=1.0,
                indian_income_tax_rate=0.30,
                remittance_so_far_inr=0,
            ),
            usd_inr_rate=83.0,
        )
        self.assertEqual(payload["platform"], "vested")
        self.assertAlmostEqual(payload["amount_inr"], 100000.0)
        self.assertIn("fees", payload)
        self.assertIn("taxes", payload)
        self.assertGreater(payload["investable"]["net_invested_usd"], 0)
        self.assertGreaterEqual(payload["estimated_total_cost_inr"], 0)

    @patch("nasdaq_tax_bot._fetch_json")
    def test_list_companies_sorted_and_limited(self, mock_fetch_json):
        mock_fetch_json.return_value = {
            "0": {"ticker": "MSFT", "title": "Microsoft Corp."},
            "1": {"ticker": "AAPL", "title": "Apple Inc."},
            "2": {"ticker": "GOOGL", "title": "Alphabet Inc."},
        }
        companies = list_us_market_companies(limit=2)
        self.assertEqual(len(companies), 2)
        self.assertEqual(companies[0]["ticker"], "AAPL")
        self.assertEqual(companies[1]["ticker"], "GOOGL")

    @patch("sys.argv", ["nasdaq_tax_bot.py", "calculate", "--amount-inr", "100000", "--platform", "vested", "--usd-inr-rate", "83"])
    def test_cli_calculate_with_manual_fx_succeeds(self):
        exit_code = main()
        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
