# Session Handoff: PGDAS Recovery and UI Mapping

Date: 2026-09-02

## Goal

Recover the PGDAS-D history from source evidence, correct historical allocation mistakes in chronological order, finish the overdue July filing/payment, and document the live PGDAS-D screens so the next agent does not need to rediscover the workflow.

## What was learned

- The company uses PGDAS-D under regime de caixa, so competence revenue and actual cash receipts must be kept separate.
- A prior month had competence revenue recorded in the wrong period. A later PGDAS cumulative value exposed the inconsistency.
- The correct recovery order is to retify the earliest wrong period first, then reopen/recalculate later periods.
- The PGDAS first screen asks separately for competence/internal, competence/external, cash/internal, and cash/external revenue.
- The dentistry workflow selected a Factor R service activity with no ISS withholding and ISS due to the establishment municipality.
- On the activity revenue screen under cash basis, the entered activity amount reconciles to the PA cash amount, not the larger competence total.
- The special tax-treatment selectors should remain blank unless source evidence supports a suspension, assessment, immunity, or reduction.
- The Factor R payroll screen asks for prior-month payroll history. Do not force the current PA payroll into earlier-month fields.
- `RBA`, `RBT12`, and `RBT12p` are useful diagnostics for historical competence allocation.
- Declaration transmission and DAS generation are separate operations.
- A retificadora that changes historical competence data but leaves the cash-basis debt unchanged does not necessarily produce a replacement DAS. Verify the original payment before doing anything else.
- For an overdue PA, generate the DAS through PGDAS and let the portal calculate multa/juros rather than manually altering the principal.

## Completed in the live session

- Corrected the earlier zero-revenue period that had an incorrect competence value.
- Re-ran and transmitted the following period with corrected competence/cash history.
- Verified that the existing DAS for that corrected period was already paid and no duplicate payment was required.
- Filed the next overdue PGDAS period after the history was corrected.
- Generated its DAS separately and paid it; private proof should remain under the ignored source tree.

## Documentation changed

- `docs/instructions/pgdas-d.md`
- `docs/instructions/monthly-cycle.md`
- `docs/lessons/cash-vs-competence.md`
- `docs/lessons/corrections-and-retifications.md`
- `docs/agent/current-state.md`
- `docs/agent/open-questions.md`

## Next task

Open e-CAC/DCTFWeb for the July payroll period and determine the direct declaration/DARF status from the live DCTFWeb screen. Do not infer payment status merely from the eSocial closing event.

During that live flow, capture the exact menu path, status labels, DARF generation controls, expected values, and proof-download/payment steps, then update `docs/instructions/dctfweb.md` in the same sanitized style.
