import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from credentials_pgdas import load_credentials


class CredentialsPgdasTest(unittest.TestCase):
    def test_load_credentials_in_paste_order(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "secrets.md"
            path.write_text(
                "CNPJ: 00000000000000\nCPF: 11111111111\nCódigo de Acesso: 222222222222\n",
                encoding="utf-8",
            )
            self.assertEqual(
                load_credentials(path),
                [
                    ("CPF", "11111111111"),
                    ("CNPJ", "00000000000000"),
                    ("Codigo de Acesso", "222222222222"),
                ],
            )


if __name__ == "__main__":
    unittest.main()
