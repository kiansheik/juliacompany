# Cash vs Competence

The repository must preserve at least three separate facts for service revenue:

- NFS-e issue date,
- service competence date,
- cash receipt date or receipt period.

Under PGDAS-D cash basis, a service with one competence month and payment in the next month is not automatically an error. It must be represented as cross-month evidence and fed into the correct PGDAS-D fields.

## Practical PGDAS mapping

For a target PA:

- **Competência, mercado interno** = domestic service revenue whose competence falls in the PA.
- **Caixa, mercado interno** = domestic revenue actually received in the PA.
- On the later activity-revenue screen, the observed cash-basis workflow uses the amount being taxed on receipt, so activity revenue should reconcile to the PA cash total.

A valid pattern can therefore look like:

```text
Month A
  competence revenue: X
  cash received: Y

Month B
  competence revenue: Z
  cash received: X
```

where `X` was earned in Month A but paid in Month B.

## Use cumulative portal values as diagnostics

The PGDAS values displayed after the first screen can reveal historical allocation mistakes.

- `RBA` should be explainable from competence revenue in the current calendar year.
- `RBT12` should be explainable from competence revenue in periods preceding the current PA.
- `RBT12p` may be shown for a newly opened company while PGDAS proportionalizes the revenue history.
- `Receita do PA` under regime de caixa should reconcile to the period's taxable cash receipts.

If a displayed cumulative figure mathematically implies revenue in a period where evidence says there was none, inspect that earlier declaration before transmitting the current one.

## Evidence priority

For competence, prefer source evidence establishing when the service belongs economically/tax-wise to the period. For cash, use actual receipt evidence such as the company bank statement/payment record.

Do not use NFS-e issue date as a substitute for either field when the documents establish different competence or payment dates.
