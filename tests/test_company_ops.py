import unittest
from decimal import Decimal
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from company_ops import brl, money, period_from_date, receipt_period


class CompanyOpsTest(unittest.TestCase):
    def test_money_accepts_brazilian_display(self):
        self.assertEqual(money("R$ 1.234,56"), Decimal("1234.56"))

    def test_brl_formats_at_output_boundary(self):
        self.assertEqual(brl("1234.56"), "R$ 1.234,56")

    def test_period_from_date(self):
        self.assertEqual(period_from_date("2026-07-03"), "2026-07")

    def test_receipt_period_falls_back_to_received_period(self):
        self.assertEqual(receipt_period({"date": None, "received_period": "2026-07"}), "2026-07")


if __name__ == "__main__":
    unittest.main()
