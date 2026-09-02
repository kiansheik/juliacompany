#!/usr/bin/env python3
from __future__ import annotations

import argparse
from decimal import Decimal

from company_ops import STATE, brl, period_from_date, read_json, receipt_period


def total(values: list[str | int | Decimal | None]) -> Decimal:
    return sum((Decimal(str(v)) for v in values if v is not None), Decimal("0.00"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a PGDAS-D instruction sheet. Does not submit anything.")
    parser.add_argument("period", help="YYYY-MM")
    args = parser.parse_args()

    invoices = read_json(STATE / "invoices.json", [])
    receipts = read_json(STATE / "receipts.json", [])
    comp = total([i.get("gross_amount") for i in invoices if period_from_date(i.get("competence_date")) == args.period])
    cash = total([r.get("amount") for r in receipts if receipt_period(r) == args.period and r.get("kind") == "service_receipt"])

    print(f"PGDAS-D INSTRUCTIONS: {args.period}")
    print("Competencia")
    print(f"  mercado interno: {brl(comp)}")
    print("  mercado externo: R$ 0,00")
    print("Caixa")
    print(f"  mercado interno: {brl(cash)}")
    print("  mercado externo: R$ 0,00")
    print("Checks")
    print("- Confirm regime de caixa is selected where applicable.")
    print("- Confirm previous cumulative values against already submitted receipts.")
    print("- Stop before transmission if the portal differs from the source-backed values.")


if __name__ == "__main__":
    main()
