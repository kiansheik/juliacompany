#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from company_ops import GENERATED, STATE, brl, period_from_date, read_json, receipt_period


def lines_for_period(period: str) -> list[str]:
    inventory = read_json(STATE / "source_inventory.json", [])
    invoices = read_json(STATE / "invoices.json", [])
    receipts = read_json(STATE / "receipts.json", [])
    payroll = read_json(STATE / "payroll.json", [])
    filings = read_json(STATE / "filings.json", [])
    obligations = read_json(STATE / "obligations.json", [])
    payments = read_json(STATE / "payments.json", [])

    source_hits = [
        item for item in inventory
        if item.get("apparent_period") == period or f"/{period[:4]}/{period[5:]}/" in item.get("current_path", "")
    ]
    period_invoices = [i for i in invoices if period_from_date(i.get("competence_date")) == period or period_from_date(i.get("issue_date")) == period]
    period_receipts = [r for r in receipts if receipt_period(r) == period]
    period_payroll = [p for p in payroll if p.get("competence") == period]
    period_filings = [f for f in filings if f.get("period") == period]
    period_obligations = [o for o in obligations if o.get("period") == period]
    period_payments = [p for p in payments if p.get("period") == period or period_from_date(p.get("payment_date")) == period]

    out = [f"PERIOD: {period}", "", "CURRENT STATE"]
    out.append(f"- Source documents found: {len(source_hits)}")
    out.append(f"- Invoices/services: {len(period_invoices)}")
    out.append(f"- Cash receipts: {len(period_receipts)}")
    out.append(f"- Payroll records: {len(period_payroll)}")
    out.append(f"- Filings: {len(period_filings)}")
    out.append(f"- Payments: {len(period_payments)}")
    out.append("")

    out.append("SOURCE DOCUMENTS")
    for item in source_hits or []:
        out.append(f"- {item['id']}: {item.get('document_type')} | {item.get('current_path')}")
    if not source_hits:
        out.append("- none indexed")
    out.append("")

    out.append("INVOICES / SERVICES")
    for inv in period_invoices:
        out.append(
            f"- {inv['id']}: NFS-e {inv.get('nfse_number', 'unknown')}, issue {inv.get('issue_date')}, "
            f"competence {inv.get('competence_date')}, gross {brl(inv.get('gross_amount'))}, source {', '.join(inv.get('source_ids', []))}"
        )
    if not period_invoices:
        out.append("- none recorded")
    out.append("")

    out.append("CASH RECEIPTS")
    for receipt in period_receipts:
        out.append(
            f"- {receipt['id']}: date {receipt.get('date') or 'unknown'} / period {receipt_period(receipt)}, {brl(receipt.get('amount'))}, "
            f"linked invoices {receipt.get('linked_invoice_ids', [])}, status {receipt.get('reconciliation_status')}"
        )
    if not period_receipts:
        out.append("- none recorded")
    out.append("")

    out.append("PGDAS-D")
    comp_total = sum(float(i.get("gross_amount", 0)) for i in invoices if period_from_date(i.get("competence_date")) == period)
    cash_total = sum(float(r.get("amount", 0)) for r in receipts if receipt_period(r) == period and r.get("kind") == "service_receipt")
    out.extend(
        [
            "1. Open the Simples Nacional PGDAS-D portal from `docs/reference/portals.md`.",
            "2. Select the company profile using private credentials from `private/secrets/`.",
            f"3. PA = {period[5:]}/{period[:4]}.",
            f"4. Competencia, mercado interno = {brl(str(comp_total))}.",
            "5. Competencia, mercado externo = R$ 0,00 unless source evidence says otherwise.",
            f"6. Caixa, mercado interno = {brl(str(cash_total))}.",
            "7. Caixa, mercado externo = R$ 0,00 unless source evidence says otherwise.",
            "8. Stop if portal totals, activity segregation, or accumulated values differ from the evidence.",
        ]
    )
    out.append("")

    out.append("PAYROLL / ESOCIAL / DCTFWEB")
    for pay in period_payroll:
        out.append(
            f"- Payroll {pay['id']}: competence {pay.get('competence')}, payment {pay.get('payment_date')}, "
            f"gross {brl(pay.get('gross_pro_labore'))}, INSS {brl(pay.get('inss'))}, IRRF {brl(pay.get('irrf'))}, net {brl(pay.get('net'))}."
        )
    if not period_payroll:
        out.append("- No payroll record for this period. Check whether pro-labore was required or paid.")
    out.append("- DCTFWeb status must be supported by receipt/source evidence before treating it as completed.")
    out.append("")

    out.append("OBLIGATIONS")
    for obligation in period_obligations:
        out.append(
            f"- {obligation['obligation']}: {obligation.get('status')} | due {obligation.get('due_date', 'unknown')} | "
            f"overdue {obligation.get('overdue', 'unknown')} | next {obligation.get('next_action', 'unknown')}"
        )
    if not period_obligations:
        out.append("- none recorded; run checks and update private/state/obligations.json")
    out.append("")

    out.append("WARNINGS")
    for inv in period_invoices:
        issue_period = period_from_date(inv.get("issue_date"))
        comp_period = period_from_date(inv.get("competence_date"))
        if issue_period and comp_period and issue_period != comp_period:
            out.append(f"- {inv['id']} crosses issue period {issue_period} and competence period {comp_period}. Do not conflate with cash-basis receipt month.")
    if not any(line.startswith("-") for line in out[out.index("WARNINGS") + 1:]):
        out.append("- No scripted warnings for this period.")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a private monthly operating report.")
    parser.add_argument("period", help="YYYY-MM")
    parser.add_argument("--output-dir", default=str(GENERATED / "monthly"))
    args = parser.parse_args()
    out = "\n".join(lines_for_period(args.period)) + "\n"
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{args.period}.md"
    path.write_text(out, encoding="utf-8")
    print(out)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
