import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pgdas


class PgdasReportTest(unittest.TestCase):
    def test_total_uses_decimal(self):
        self.assertEqual(pgdas.total(["1.10", "2.20"]), pgdas.Decimal("3.30"))


if __name__ == "__main__":
    unittest.main()
