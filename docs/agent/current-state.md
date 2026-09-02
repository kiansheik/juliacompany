# Current State

As of 2026-09-02, this repository has been bootstrapped as a public-safe operational toolkit with ignored private state.

Tracked-safe material includes scripts, schemas, templates, sanitized docs, and tests. Private material is under `private/` and ignored by Git.

Current reconstruction from private evidence:

- Company setup/registration evidence exists in `private/sources/company-formation/`.
- NFS-e XML/PDF evidence exists for service periods spanning June through August 2026, including a cross-month competence/receipt case.
- PGDAS-D history was reviewed live against source evidence.
- May 2026 PGDAS-D was retified to remove competence revenue that did not belong in that period.
- June 2026 PGDAS-D was then retified so competence history reflects the source documents while the cash-basis taxable amount remains tied to actual June receipts.
- The June correction did not change the declared debt; the original June DAS was already recorded as paid, so no duplicate DAS was needed.
- July 2026 PGDAS-D was transmitted after the historical corrections. DAS generation was a separate step; the overdue DAS was generated and paid, with private declaration/receipt/DAS/payment evidence retained locally.
- The live PGDAS-D screen sequence and reconciliation rules are now documented in `docs/instructions/pgdas-d.md`.
- July payroll/eSocial evidence exists, including remuneration and closing XML.
- Direct DCTFWeb status and previdenciary DARF payment evidence for July remain the next unresolved tax task.
- A new service/NFS-e request is pending after the DCTFWeb check and should be processed from its source request rather than from memory.
- `make credentials-pgdas` is available as a local clipboard helper for PGDAS-D login fields; it reads ignored private secrets and prints no credential values.

Do not treat any time-sensitive due date as legally verified. Items marked `NEEDS CURRENT VERIFICATION` require current official-source review before live action.
