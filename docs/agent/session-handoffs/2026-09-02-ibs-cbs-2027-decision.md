# Session Handoff: 2027 IBS/CBS Decision

Date: 2026-09-02

## Goal

Research whether the company should remain in ordinary Simples treatment for IBS/CBS or elect the regular IBS/CBS regime for Jan-Jun 2027, assuming the current dentistry-service business model continues without material change.

## Result

Recorded decision: **do not elect regular-regime IBS/CBS in September 2026 for Jan-Jun 2027. Remain in pure Simples and re-evaluate in March 2027 for Jul-Dec.**

Primary decision record: `docs/agent/2027-ibs-cbs-decision.md`.

## Main reasons

- Under the current projection, Factor R should keep dentistry in Annex III; the 2027-2028 first bracket remains 6% through R$ 180.000 RBT12.
- The statutory first-bracket partition makes CBS+IBS inside the pure-Simples DAS approximately 0,936% of revenue.
- Dentistry is a health service receiving a 60% reduction from regular IBS/CBS rates.
- Even with that reduction, hybrid must overcome the low pure-Simples CBS+IBS baseline plus extra compliance burden.
- The business is payroll-heavy rather than input-heavy. Working-partner remuneration is outside IBS/CBS and does not create a regular-regime input credit.
- There is currently no evidence of enough creditable taxed purchases to offset hybrid's likely extra gross burden.
- There is no current agreement that the customer would pay regular IBS/CBS on top of the existing monthly service fee.
- The final 2027 CBS reference rate was not yet available at this research date, so an exact hybrid tax bill must not be invented.

## Important official sources

- Ministério da Fazenda, September 2026 election guidance:
  https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/setembro/comecou-nesta-terca-1o-09-o-prazo-para-opcao-pelo-simples-nacional-e-para-a-escolha-do-modelo-de-recolhimento-do-ibs-e-da-cbs-em-2027/
- Receita Federal, CGSN reform guidance:
  https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/agosto/cgsn-atualiza-regras-do-simples-nacional-para-adequacao-a-reforma-tributaria-do-consumo/
- LC 214/2025 compiled text, including regular-regime option, credits, non-incidence on employment/administrator services, transition and tax-base rules:
  https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm
- 2027-2028 Annex III table:
  https://legis.senado.gov.br/norma/40180341/publicacao/40181117
- Receita Federal transition overview:
  https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/reforma-tributaria-do-consumo/entenda
- Receita Federal announcement ending monthly Simples cash-basis apuração from 2027:
  https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/agosto/regime-de-caixa-deixa-de-ser-utilizado-na-apuracao-do-simples-nacional

## What changed in the repo

- Created `docs/agent/2027-ibs-cbs-decision.md` with sourced analysis, assumptions, break-even logic, pros/cons, stop conditions, and March re-evaluation checklist.
- Linked the decision record from `docs/agent/index.md`.
- Added the decision to `docs/agent/long-term-strategy.md`.
- Updated `docs/agent/current-state.md`.
- Updated `docs/agent/open-questions.md` to schedule a March 2027 re-analysis and 2027 cash-basis runbook change.
- Updated `docs/agent/log.md`.

## Next prompt for a future agent

If asked about 2027 IBS/CBS, start by reading `docs/agent/2027-ibs-cbs-decision.md`. Do not redo the analysis from scratch unless a law, rate, business assumption, customer arrangement, Factor R result, or credit profile has changed.

In March 2027, explicitly verify the final CBS rate, current IBS rule, actual Jan-Mar creditable invoices, current RBT12/Factor R, customer credit/pricing position, and then-current election deadlines before recommending Jul-Dec treatment.
