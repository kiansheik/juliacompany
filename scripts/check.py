#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

from company_ops import ROOT, STATE, period_from_date, read_json


def err(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> None:
    errors: list[str] = []
    invoices = read_json(STATE / "invoices.json", [])
    receipts = read_json(STATE / "receipts.json", [])
    filings = read_json(STATE / "filings.json", [])
    payments = read_json(STATE / "payments.json", [])
    obligations = read_json(STATE / "obligations.json", [])

    invoice_ids = {i["id"] for i in invoices}
    for receipt in receipts:
        if receipt.get("kind") == "service_receipt" and not receipt.get("linked_invoice_ids"):
            err(errors, f"cash receipt without invoice link: {receipt['id']}")
        for invoice_id in receipt.get("linked_invoice_ids", []):
            if invoice_id not in invoice_ids:
                err(errors, f"receipt {receipt['id']} links missing invoice {invoice_id}")

    paid_periods = {(p.get("system"), p.get("period")) for p in payments}
    def positive_amount(value: object) -> bool:
        try:
            return Decimal(str(value or "0")) > 0
        except (InvalidOperation, ValueError):
            return False

    for filing in filings:
        if not positive_amount(filing.get("calculated_tax")):
            continue
        if filing.get("payment_status") == "paid":
            continue
        if (filing.get("system"), filing.get("period")) not in paid_periods:
            print(f"WARN tax generated but no payment evidence link: {filing.get('id')}")

    for obligation in obligations:
        if obligation.get("status") == "completed" and not obligation.get("source_ids"):
            print(f"WARN completed obligation lacks source evidence: {obligation.get('id')}")

    status = subprocess.run(["git", "ls-files", "private", "secrets"], cwd=ROOT, text=True, capture_output=True, check=False)
    if status.stdout.strip():
        err(errors, "private or secrets files are tracked by Git")

    if errors:
        for message in errors:
            print(f"ERROR {message}")
        sys.exit(1)
    print("check passed")


if __name__ == "__main__":
    main()
