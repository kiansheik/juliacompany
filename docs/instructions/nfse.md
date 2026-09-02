# NFS-e Workflow

Source evidence belongs in `private/sources/YYYY/MM/nfse/`.

Record these fields in `private/state/invoices.json`:

- NFS-e number.
- Issue date.
- Service competence date.
- Gross amount.
- Municipality and service location.
- Service category.
- ISS retention flag as shown by the source.
- Payer reference.
- Source inventory IDs.

Do not assume issue date equals service competence. When they differ, keep both dates and let PGDAS-D use the correct competence and cash-basis receipt period separately.
