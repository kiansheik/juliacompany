#!/usr/bin/env python3
from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_HALF_UP

from company_ops import brl


def q(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a payroll scenario. Does not submit eSocial or DCTFWeb.")
    parser.add_argument("period", help="YYYY-MM")
    parser.add_argument("--gross", required=True, help="Gross pro-labore amount")
    args = parser.parse_args()
    gross = q(Decimal(args.gross.replace(",", ".")))

    print(f"PAYROLL SCENARIO: {args.period}")
    print(f"Gross pro-labore: {brl(gross)}")
    print("INSS: NEEDS CURRENT VERIFICATION before use for a live period")
    print("IRRF: NEEDS CURRENT VERIFICATION before use for a live period")
    print("Net transfer: cannot be determined until verified tax tables are configured")
    print("Factor R: include this payroll in Factor R analysis only after payment/eSocial evidence is recorded")
    print("Tax table version/source: none configured")


if __name__ == "__main__":
    main()
