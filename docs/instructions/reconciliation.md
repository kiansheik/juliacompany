# Reconciliation Workflow

Run:

```bash
python3 scripts/reconcile.py
python3 scripts/check.py
```

Expected checks include:

- invoice without linked receipt,
- cash receipt without linked invoice,
- cross-month competence vs cash receipt,
- tax generated without payment evidence,
- payroll closed without payment proof,
- completed obligation without evidence,
- private files accidentally tracked by Git.

Cross-month service competence and cash receipt is not an error under cash-basis PGDAS-D; it is a fact to preserve.
