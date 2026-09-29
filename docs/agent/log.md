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
- Fetched and fast-forwarded local `main` from `0aac65b` to `1f3ab01`, preserving the unstaged local `Makefile` change.
- Researched the 2027 pure-Simples versus regular-regime IBS/CBS election using current Receita/Fazenda guidance, LC 214/2025, the 2027-2028 Annex III partition, health-service rate reduction, credit rules, and the announced end of monthly Simples cash-basis apuração.
- Recorded the current 2027 decision in `docs/agent/2027-ibs-cbs-decision.md`: do not elect regular IBS/CBS for Jan-Jun 2027 under the existing business model; re-evaluate in March 2027 for Jul-Dec using the final CBS rate, actual credits, Factor R and customer pricing/tax treatment.


## 2026-09-29

- Completed the September eSocial payroll cycle through S-1299 after September remuneration and payment information had been recorded.
- Reviewed the downloaded S-1299 XML/receipt for PA 09/2026.
- Confirmed remuneration and payment information were both present and immediate DCTFWeb transmission was requested.
- Confirmed processing result `202 - Sucesso com advertência`; warning code `1727` contained DCTFWeb message `446`, explicitly confirming successful DCTFWeb transmission.
- Recorded the important evidence boundary: S-1299 proves eSocial closing and DCTFWeb transmission status, but does not prove DARF generation or payment.
- Updated the eSocial runbook for a month where remuneration and payment occur in the same PA.
- Raw eSocial closing files remain private evidence and are intentionally not committed to public `main`.
- Next live action is e-CAC / DCTFWeb for PA 09/2026, then DARF generation and payment evidence.

- Generated the 09/2026 DCTFWeb DARF for R$ 550,00, code 1099 (contribuinte individual - 11%), due 20/10/2026; payment proof is still pending and must be retained separately.
- Received evidence of the 29/09/2026 net September pró-labore payment for R$ 4.450,00 from the company account.
- Received company-bank payment proof for the 09/2026 DCTFWeb DARF of R$ 550,00 on 29/09/2026; September payroll/DCTFWeb is now paid.
- Researched expense-reimbursement treatment for personally paid transportation. Recorded that genuine documented work travel/expense reimbursements can retain indemnity character, but ordinary residence-to-regular-workplace Uber commuting for the working partner should not be treated as tax-free reimbursement.
