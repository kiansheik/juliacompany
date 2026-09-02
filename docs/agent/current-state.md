# Current State

As of 2026-09-02, this repository is a public-safe operational toolkit with ignored private state.

Tracked-safe material includes scripts, schemas, templates, sanitized docs, and tests. Private material is under `private/` and ignored by Git.

Current reconstruction from private evidence and the live portal session:

- Company setup/registration evidence exists in `private/sources/company-formation/`.
- NFS-e XML/PDF evidence exists for service periods spanning June through September 2026, including a cross-month competence/receipt case.
- PGDAS-D history was reviewed live against source evidence.
- May 2026 PGDAS-D was retified to remove competence revenue that did not belong in that period.
- June 2026 PGDAS-D was then retified so competence history reflects the source documents while the cash-basis taxable amount remains tied to actual June receipts.
- The June correction did not change the declared debt; the original June DAS was already recorded as paid, so no duplicate DAS was needed.
- July 2026 PGDAS-D was transmitted after the historical corrections. DAS generation was a separate step; the overdue DAS was generated and paid, with private declaration/receipt/DAS/payment evidence retained locally.
- August 2026 PGDAS-D was transmitted as an original declaration with source-backed August cash revenue. The DAS was generated and paid from the company account, with declaration receipt, DAS, and payment proof retained in ignored private evidence.
- The live PGDAS-D screen sequence and reconciliation rules are documented in `docs/instructions/pgdas-d.md`.
- July payroll/eSocial is closed. The S-1299 response showed successful DCTFWeb transmission and the DCTFWeb DARF was generated and paid.
- The live DCTFWeb declaration was found after switching e-CAC to the company/legal-representative profile. The DCTFWeb/e-CAC screen flow is documented in `docs/instructions/dctfweb.md`.
- The durable pró-labore / personal-IR / Factor R strategy is documented in `docs/agent/long-term-strategy.md`.
- For 2026 only, the current planning candidate is up to R$ 5.000,00 gross monthly pró-labore when the annual projection and company economics support it. This is a planning target, not a hardcoded payroll amount.
- August 2026 S-1200 remuneration was entered using the established working-partner setup with the planned gross pró-labore.
- August 2026 payroll was closed successfully. The closing result returned `202 - Sucesso com advertência`; warning code `1727` contained DCTFWeb message `446`, confirming successful immediate DCTFWeb transmission.
- The 08/2026 DCTFWeb DARF was generated and paid, and the net August pró-labore was paid to the working partner in September with private bank evidence retained.
- Because the August payment occurred in September, August correctly closed with remuneration information present and payment information absent. The corresponding S-1210 was subsequently entered in the September payment period referencing the August remuneration/demonstrative.
- August is fully closed from the recurring NFS-e/PGDAS/payroll/DCTFWeb workflow perspective.
- The September recurring NFS-e was issued successfully through the National NFS-e complete-emission flow. Final DANFSe and signed XML were reviewed and agree on the source-backed September competence, recurring dentistry service, Barretos service location, Itupeva ISS incidence, no ISS/federal withholding, no IBS/CBS amount, and the current billing-request additional text.
- The signed XML confirmed the carry-forward National NFS-e profile: ME/EPP Simples option, federal+municipal apuração through Simples, dentistry national service code, dentistry NBS, non-retained PIS/COFINS/CSLL, and the Simples approximate-tax-rate field. The exact rate must be recomputed rather than copied after a Factor R/Annex change.
- The full National NFS-e live workflow, recurring defaults, stop conditions, interaction lessons, and preferred future-agent response format are now documented in `docs/instructions/nfse.md`.
- September NFS-e evidence still needs to be copied/inventoried into the ignored local `private/sources/2026/09/nfse/` area if that has not already happened outside this connector session.
- September planning: re-run the R$ 5.000,00 gross pró-labore candidate against the annual taxable-income projection and company cash. If selected, prefer to pay the September remuneration within September rather than slipping payment into October, because Factor R uses payroll amounts paid in the 12 months before the PA.
- Conditional forecast only: if September service cash is received as expected and September gross pró-labore is R$ 5.000,00 and actually paid in September, the October Factor R lookback should include the July payroll payment plus both R$ 5.000,00 payments made in September. On the currently reconstructed revenue history this was projected above 0,28. The live PGDAS calculation remains authoritative; do not hardcode Annex III.
- `make credentials-pgdas` is available as a local clipboard helper for PGDAS-D login fields; it reads ignored private secrets and prints no credential values.

Do not treat any time-sensitive due date or threshold as permanently valid. Items marked `NEEDS CURRENT VERIFICATION` require current official-source review before live action.
