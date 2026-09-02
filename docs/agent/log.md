# Agent Log

## 2026-09-02

- Bootstrapped public-safe repository structure.
- Added `.gitignore` before reorganizing private material.
- Built initial inventory before moving source files.
- Moved private source evidence and secrets under ignored `private/`.
- Reconstructed initial 2026 state from NFS-e XML, eSocial XML, PGDAS PDF text snippets, and local notes.
- Added scripts for inventory, monthly reports, PGDAS instructions, reconciliation, payroll scenarios, and checks.
- Generated private reports for 2026-06, 2026-07, 2026-08, and current recovery status.
- Added `make credentials-pgdas` to copy PGDAS-D login fields from ignored private notes into `pbcopy` one at a time.
- Recovered and documented the live PGDAS-D correction/declaration/DAS flow.
- Verified July eSocial closing and successful DCTFWeb transmission from the S-1299 response.
- Identified that DCTFWeb must be searched under the e-CAC company/legal-representative profile; the personal CPF profile returned no company declaration.
- Documented the DCTFWeb filters, declaration row, receipt/extract controls, and DARF-generation flow.
- Generated the overdue July DCTFWeb DARF and subsequently confirmed private payment evidence during the recovery session.
- Added a durable long-term strategy for monthly pró-labore, 2026 personal-IR limits, eSocial payment timing, and Factor R optimization.
- Closed the August recurring cycle: August PGDAS/DAS, DCTFWeb/DARF, payroll payment, and September S-1210 referencing August remuneration were completed.
- Issued the September recurring NFS-e through the National NFS-e complete-emission UI and reviewed the final DANFSe plus signed XML.
- Confirmed from the signed XML the recurring National NFS-e profile for the current company/service: ME/EPP Simples option, federal+municipal apuração through Simples, dentistry service code/NBS, non-retained ISS and federal contributions, and the Simples approximate-tax-rate field.
- Expanded `docs/instructions/nfse.md` into a live portal runbook with stable carry-forward defaults, period-specific fields, stop conditions, review checks, evidence requirements, and interaction lessons aimed at reducing future copy/paste.
- Recorded that the approximate Simples rate on NFS-e must be recomputed when Factor R/Annex treatment changes rather than blindly copied from the last invoice.
