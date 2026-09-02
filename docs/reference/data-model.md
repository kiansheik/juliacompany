# Data Model

Private state is JSON under `private/state/`.

Core entities:

- Invoice/service event: issue date, competence date, gross amount, NFS-e number, payer, municipality, source IDs.
- Cash receipt: date if known, received period, amount, payer, bank reference, linked invoices, source IDs.
- Payroll: competence, payment date, gross pro-labore, INSS, IRRF, net, eSocial status, source IDs.
- Filing: system, period, declaration type, original/retificadora status, submitted flag, tax generated, due date, payment status, source IDs.
- Payment: obligation, period, amount, payment date, status, source IDs.
- Obligation: period, obligation, status, due date, overdue state, dependencies, next action.

Corrections are additive. A retificadora is a new filing record, not a rewrite of the original.
