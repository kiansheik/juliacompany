# Payments Workflow

Store payment source documents under the relevant private source period.

Record:

- obligation or receivable,
- period,
- amount,
- due date when applicable,
- actual payment/receipt date,
- payer/payee and account/reference only when needed privately,
- source inventory IDs.

Payment/receipt date is not the same as tax due date, payroll competence, service competence, or NFS-e issue date.

## Customer-receipt reconciliation

For recurring customer receipts, future agents should compare the bank receipt against the specific NFS-e before using the amount in PGDAS or other accounting state.

1. Confirm payer, receipt date, and exact bank amount from source evidence.
2. Match the receipt to the NFS-e competence, number, and gross amount.
3. If bank amount equals invoice amount, record the receipt normally.
4. If bank amount differs from invoice amount, stop and classify the difference. Do not silently change the NFS-e amount or treat the difference as service revenue.
5. A small excess may be a customer overpayment/credit, bank adjustment, or additional consideration; determine which from evidence. Record a receivable/payable/other classification as appropriate before filing PGDAS.
6. Under 2026 cash-basis Simples, PGDAS uses received service revenue for the monthly taxable base, but `receipt in bank` and `gross service revenue` are not automatically identical when part of a receipt is not consideration for the service. Preserve the reconciliation.
7. Save the bank statement or transaction proof privately. A chat message reporting a payment is useful provisional evidence but does not replace the bank proof.

For 2027 onward, do not reuse the 2026 cash-basis assumption: verify the then-current Simples revenue-recognition rule before filing.
