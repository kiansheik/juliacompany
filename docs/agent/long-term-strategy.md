# Long-Term Payroll and Tax Strategy

This document is the durable operating strategy for choosing pró-labore and coordinating eSocial, DCTFWeb, IRPF, and Simples Nacional / Factor R. It is a planning framework, not a substitute for current legal verification.

## Objectives

1. Keep payroll and tax filings source-backed and internally consistent.
2. Pay a real, defensible pró-labore for work actually performed.
3. For 2026, maximize pró-labore without creating unnecessary personal IR while preserving company cash.
4. Use legitimate payroll history to improve Factor R when economically beneficial.
5. Keep monthly IRRF, annual IR due, and DIRPF filing obligation as separate questions.

## 2026 personal-IR guardrails

Current official rules, last verified 2026-09-02:

- Receita Federal's 2026 monthly reduction makes IR due zero for monthly taxable income up to R$ 5.000,00.
- For the 2027 annual adjustment covering calendar year 2026, Receita's annual reduction makes IR due zero for annual taxable income up to R$ 60.000,00.
- These thresholds do not establish whether a DIRPF filing will be mandatory. Filing-obligation rules must be checked separately when Receita publishes the applicable exercise rules.

Operational consequence for 2026:

- R$ 5.000,00 gross monthly pró-labore is the default upper target when the goal is zero monthly IRRF, provided the payment is economically supportable and the annual projection remains safe.
- Do not blindly pay R$ 5.000,00 every month. Before each payroll, project all known taxable income Julia may receive from every source during 2026. If the projected annual taxable total would exceed R$ 60.000,00, reduce or reconsider the target.
- Other taxable income can change the annual result even if J&L itself withholds zero IRRF.
- Never carry the R$ 5.000,00 / R$ 60.000,00 thresholds into another calendar year without re-verifying current official rules.

Official source: Receita Federal, `Tributação de 2026`.
https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026

## Monthly pró-labore decision process

Before creating each month's remuneration:

1. Reconcile company cash and expected near-term obligations.
2. Confirm the remuneration corresponds to real work and is supportable by the company.
3. Calculate taxable pró-labore already recognized in the calendar year.
4. Add known/projected taxable income from other sources.
5. Project the year-end taxable total under the proposed pró-labore.
6. Check the current monthly IRRF threshold/reduction.
7. Check the current annual IR threshold/reduction.
8. Model the effect on Factor R for future PGDAS periods.
9. Choose the gross pró-labore only after those checks.
10. Recalculate INSS using the current year's contribution rules and ceiling; do not hardcode an old contribution amount.
11. Decide the actual payment month deliberately. If company cash allows, paying a remuneration in its own competence month may improve Factor R sooner than letting the payment slip into the next month.

For the current 2026 plan, use R$ 5.000,00 gross as the default candidate, not an unconditional rule.

## Factor R strategy

Dentistry is subject to Factor R. Under the currently verified Simples rules:

- Factor R >= 0,28 routes qualifying service revenue to Annex III.
- Factor R < 0,28 routes it to Annex V.
- Factor R is based on payroll, including pró-labore and applicable charges, versus gross revenue over the relevant prior-12-month window.
- For a company with less than 13 months of activity, the special proportionalization rules in Resolução CGSN 140/2018 apply.

Important timing rule: the regulation refers to the amount **paid** in the 12 months before the PA. Therefore payroll competence and cash payment date are not interchangeable for Factor R.

Example: if August remuneration is actually paid in September, it is still August remuneration for eSocial S-1200, but the cash payment occurs in September. That timing must be considered when determining which later PGDAS Factor R lookback windows include the payment.

### Payment-timing strategy

When there is sufficient company cash and no other reason to delay payment, prefer paying the current month's pró-labore before that month ends. This does not change the S-1200 competence, but it can cause the payment to enter a Factor R lookback one PA earlier.

For the September 2026 planning case observed in the live workflow:

- the July pró-labore was paid in July;
- the August pró-labore was paid in September;
- if a September pró-labore is also paid in September, both the August and September payments can be part of the payroll amounts paid during September for a later lookback;
- under the then-current recurring revenue projection, that timing was expected to be enough to move the rough ratio above 0,28 for the October PA.

This is a forecast, not an annex election. Recompute from actual source-backed revenue/payroll and trust the live PGDAS Factor R result.

Do not choose payroll solely to manufacture a tax result. Compare:

- additional INSS/payroll cost,
- company cash needs,
- projected Factor R,
- projected Annex III versus Annex V tax,
- personal IR consequences.

Official source: Resolução CGSN nº 140/2018, art. 26, compiled text.
https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=92278&naoPublicado=&visao=compilado

## 2027 IBS/CBS election

A dedicated sourced decision record is maintained in `docs/agent/2027-ibs-cbs-decision.md`.

Current decision as of 2026-09-02: **do not elect the regular IBS/CBS regime in September 2026 for Jan-Jun 2027; remain in pure Simples and re-evaluate in March 2027 for Jul-Dec.**

The decision assumes the current small dentistry-service model continues: recurring revenue around the existing level, payroll-heavy costs, no large creditable supply chain, and no agreement for the customer to pay regular-regime IBS/CBS on top of the existing service fee.

Do not treat this as permanent. Re-open the decision if the final CBS rate, Factor R, creditable purchases, customer pricing/tax treatment, or option deadlines change.

Also note that the 2026 cash-basis PGDAS workflow must not be carried into 2027. Receita has announced the end of the monthly Simples cash-basis option from 1 January 2027. See the sourced decision document for the operational impact.

## eSocial timing model

Keep remuneration competence and payment month separate.

- S-1200 records remuneration for the payroll competence.
- S-1210 records the actual payment in the month in which payment occurs and references the competence/demonstrative being paid.
- S-1299 closes the payroll period and can transmit DCTFWeb.

If an August pró-labore is created after August ends and the net amount is paid in September:

- remuneration remains associated with 08/2026,
- the payment event belongs to 09/2026,
- the S-1210 must reference the August remuneration,
- bank proof must show the actual payment date.

Official source: eSocial Manual Web Geral, section S-1210.
https://www.gov.br/esocial/pt-br/empresas/manual-web-geral/manual-web-geral/

## DCTFWeb operating rule

After S-1299, do not infer the tax is paid merely because eSocial says DCTFWeb transmission succeeded.

For each payroll period:

1. Preserve the S-1299 XML/receipt privately.
2. Enter e-CAC using the company/legal-representative profile.
3. Locate the DCTFWeb period and verify `Origem`, `Tipo`, `Situação`, `Débito Apurado`, and `Saldo a Pagar`.
4. Save the declaration, receipt, and processing extract when available.
5. Generate the DARF from the active declaration.
6. For overdue periods, let DCTFWeb/SENDA calculate multa and juros.
7. Pay from the company bank account when practical.
8. Save bank payment proof separately from the DARF itself.
9. Do not mark the period paid in private state until payment evidence exists or the portal later confirms payment.

## Profit distributions are separate

Do not treat distributions of profit as pró-labore and do not count them toward Factor R payroll. Any distribution needs its own accounting support and tax analysis.

## Re-evaluation triggers

Re-run the strategy immediately if any of these happen:

- Julia begins receiving another taxable income source.
- Company monthly revenue materially changes.
- Projected 2026 taxable personal income approaches R$ 60.000,00.
- A proposed monthly payment exceeds the verified zero-IRRF range.
- Factor R approaches the 0,28 boundary.
- Company cash becomes tight.
- INSS, IRPF, Simples, IBS/CBS, or eSocial rules change.
- The calendar year changes.

## What future agents must do

Do not inherit the last month's gross pró-labore as a constant. Read current private state, project the year, verify current official rules, calculate the Factor R effect, and then recommend that month's amount and payment timing.

For 2027 IBS/CBS questions, read `docs/agent/2027-ibs-cbs-decision.md` before redoing the analysis. Preserve the recorded decision unless a documented assumption or legal rule has changed.
