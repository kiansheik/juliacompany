# PGDAS-D Workflow

Use `python3 scripts/pgdas.py YYYY-MM` before entering the portal.

Field mapping:

- PA: requested period, displayed as `MM/YYYY`.
- Regime de competencia, mercado interno: invoices with service competence in the PA.
- Regime de competencia, mercado externo: normally zero unless evidence shows export revenue.
- Regime de caixa, mercado interno: cash receipts received in the PA.
- Regime de caixa, mercado externo: normally zero unless evidence shows export revenue received.

Stop before transmission if:

- portal totals differ from source-backed values,
- activity segregation is unclear,
- previous cumulative values conflict with existing receipts,
- a prior period appears to need retification.

After submission, download the PGDAS-D receipt, generated DAS, and payment proof after payment. Store all under `private/sources/YYYY/MM/pgdas-d/`.
