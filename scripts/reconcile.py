#!/usr/bin/env python3
from __future__ import annotations

from decimal import Decimal

from company_ops import STATE, brl, period_from_date, read_json, receipt_period


def main() -> None:
    invoices = read_json(STATE / "invoices.json", [])
    receipts = read_json(STATE / "receipts.json", [])
    by_invoice = {invoice["id"]: invoice for invoice in invoices}
    linked = {invoice_id for receipt in receipts for invoice_id in receipt.get("linked_invoice_ids", [])}

    print("RECONCILIATION")
    for invoice in invoices:
        related = [r for r in receipts if invoice["id"] in r.get("linked_invoice_ids", [])]
        if not related:
            print(f"- {invoice['id']}: no linked cash receipt evidence")
            continue
        for receipt in related:
            comp_period = period_from_date(invoice.get("competence_date"))
            cash_period = receipt_period(receipt)
            status = "cross-month" if comp_period != cash_period else "same-month"
            print(
                f"- {invoice['id']}: competence {comp_period}, cash {cash_period}, "
                f"{brl(invoice.get('gross_amount'))} -> {status}"
            )

    for receipt in receipts:
        for invoice_id in receipt.get("linked_invoice_ids", []):
            if invoice_id not in by_invoice:
                print(f"- receipt {receipt['id']}: links unknown invoice {invoice_id}")


if __name__ == "__main__":
    main()
