# Portals

Keep credentials in `private/secrets/` only.

## Simples Nacional / PGDAS-D

- Official source: Receita Federal / Simples Nacional portal.
- Use for monthly PGDAS-D apuração and DAS generation.
- Internal source: `private/state/invoices.json` and `private/state/receipts.json`.
- Local clipboard helper: `make credentials-pgdas` copies CPF, CNPJ, and access code from `private/secrets/` one at a time without printing values.

## Municipal NFS-e

- Official source: municipality/NFS-e issuing portal shown by the source evidence.
- Use for issuing/downloading NFS-e XML/PDF.
- Internal source: `private/state/invoices.json`.

## eSocial Web Geral

- Official source: eSocial portal.
- Use for remuneration/payment events and monthly closing.
- Internal source: `private/state/payroll.json`.

## DCTFWeb

- Official source: Receita Federal DCTFWeb portal.
- Use for federal declaration/payment evidence after payroll-related events.
- Internal source: `private/state/filings.json` and `private/state/payments.json`.
