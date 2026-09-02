# Current State

As of 2026-09-02, this repository is a public-safe operational toolkit with ignored private state.

Tracked-safe material includes scripts, schemas, templates, sanitized docs, and tests. Private material is under `private/` and ignored by Git.

Current reconstruction from private evidence and the live portal session:

- Company setup/registration evidence exists in `private/sources/company-formation/`.
- NFS-e XML/PDF evidence exists for service periods spanning June through August 2026, including a cross-month competence/receipt case.
- PGDAS-D history was reviewed live against source evidence.
- May 2026 PGDAS-D was retified to remove competence revenue that did not belong in that period.
- June 2026 PGDAS-D was then retified so competence history reflects the source documents while the cash-basis taxable amount remains tied to actual June receipts.
- The June correction did not change the declared debt; the original June DAS was already recorded as paid, so no duplicate DAS was needed.
- July 2026 PGDAS-D was transmitted after the historical corrections. DAS generation was a separate step; the overdue DAS was generated and paid, with private declaration/receipt/DAS/payment evidence retained locally.
- The live PGDAS-D screen sequence and reconciliation rules are documented in `docs/instructions/pgdas-d.md`.
- July payroll/eSocial is closed. The S-1299 response showed successful DCTFWeb transmission.
- The live DCTFWeb declaration was found after switching e-CAC to the company/legal-representative profile. The July declaration appeared as active, originated from eSocial, with an outstanding previdenciary balance.
- The July DCTFWeb DARF was generated and paid; payment evidence was supplied in the live session and should be retained in ignored private evidence.
- The DCTFWeb/e-CAC screen flow is documented in `docs/instructions/dctfweb.md`.
- The durable pró-labore / personal-IR / Factor R strategy is documented in `docs/agent/long-term-strategy.md`.
- For 2026 only, the current planning candidate is up to R$ 5.000,00 gross monthly pró-labore when the annual projection and company economics support it. This is a planning target, not a hardcoded payroll amount.
- August 2026 S-1200 remuneration was entered using the established working-partner setup, with a gross pró-labore of R$ 5.000,00.
- August 2026 payroll was closed successfully. The closing result returned `202 - Sucesso com advertência`; warning code `1727` contained DCTFWeb message `446`, confirming successful immediate DCTFWeb transmission.
- The 08/2026 DCTFWeb DARF was generated and paid, and payment evidence was supplied in the live session and retained in ignored private evidence.
- The net August pró-labore was paid to the working partner in September, with the bank transfer explicitly described as referring to 08/2026; payment evidence was supplied and retained in ignored private evidence.
- Because that payment occurred in September, August correctly closed with remuneration information present and payment information absent. The corresponding S-1210 must be entered in the September payment period and reference the August remuneration/demonstrative.
- Remaining August-cycle work: (1) enter the September S-1210 for the August remuneration using the actual September payment date and saved bank evidence; and (2) complete PGDAS-D for PA 08/2026, reconciling August competence/cash revenue and the Factor R payroll window from source evidence before transmission/payment.
- A new service/NFS-e request is pending and should be processed from its source request rather than from memory.
- `make credentials-pgdas` is available as a local clipboard helper for PGDAS-D login fields; it reads ignored private secrets and prints no credential values.

Do not treat any time-sensitive due date or threshold as permanently valid. Items marked `NEEDS CURRENT VERIFICATION` require current official-source review before live action.
