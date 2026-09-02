# Session Handoff: DCTFWeb and Long-Term Payroll Strategy

Date: 2026-09-02

## Goal

Finish the July payroll-tax recovery, learn the real eSocial/e-CAC/DCTFWeb UI path, and convert the emerging pró-labore / IRPF / Factor R approach into a durable strategy for future months and future agents.

## What was verified live

- July eSocial showed `Situação da Folha: Fechada`.
- The S-1299 XML/receipt showed successful direct DCTFWeb transmission.
- Searching DCTFWeb from the wrong e-CAC profile returned no declaration.
- After switching to the company/legal-representative context, the July DCTFWeb declaration appeared.
- The declaration row showed the expected company payroll declaration fields and an outstanding previdenciary balance.
- The page exposed controls for viewing the declaration, receipt, processing extract, retification, and DARF generation.
- The DARF was generated with automatic late-payment additions. User reports the DARF was paid; preserve/inventory the actual bank payment proof separately from the guide.

## Long-term strategy established

For 2026, the operating goal is to choose the highest sensible pró-labore while avoiding unnecessary personal IR and improving legitimate Factor R history.

Current verified planning guardrails:

- zero monthly IR reduction through R$ 5.000,00 taxable monthly income,
- zero annual IR reduction through R$ 60.000,00 taxable annual income for the 2027 adjustment of calendar year 2026,
- Factor R threshold 0,28 between Annex III and Annex V for qualifying services.

These are not permanent constants. Each month must recompute year-to-date/projected taxable income, current official rules, company cash, INSS, and Factor R impact.

## Critical timing lesson

Do not conflate remuneration competence and payment date.

If August remuneration is paid in September:

- S-1200 remains August remuneration,
- S-1210 belongs to September and references August,
- Factor R modeling must respect the regulation's use of amounts paid in the prior-12-month window.

## Documentation changed

- `AGENTS.md`
- `docs/agent/index.md`
- `docs/agent/current-state.md`
- `docs/agent/long-term-strategy.md`
- `docs/agent/open-questions.md`
- `docs/agent/log.md`
- `docs/instructions/esocial.md`
- `docs/instructions/dctfweb.md`
- `docs/lessons/factor-r.md`
- this handoff

## Next tasks

1. Save/inventory the July DCTFWeb bank payment proof.
2. Determine August gross pró-labore from the long-term strategy rather than copying July.
3. Enter/close August remuneration correctly in eSocial.
4. If the payment occurs in September, create the corresponding September S-1210 payment entry referencing August.
5. Process the pending new NFS-e request from its source evidence.
6. Continue to model rolling Factor R before each PGDAS filing.

## Suggested next prompt

`Load the repo context and help me set August pró-labore. Reconcile year-to-date taxable income and company cash from private evidence, verify current 2026 IR/INSS rules, model the Factor R effect, and then walk me through the live eSocial fields one screen at a time.`
