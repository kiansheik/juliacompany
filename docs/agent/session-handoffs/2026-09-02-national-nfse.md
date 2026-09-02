# Session Handoff: National NFS-e Live Run

Date: 2026-09-02

## Goal

Issue the next recurring dentistry NFS-e through the National NFS-e complete-emission UI, validate the final document, and turn the live session into a reusable low-copy/paste runbook.

## Source material inspected

Private/source material supplied during the session included:

- the current recurring-customer billing request;
- live National NFS-e page HTML for Pessoas, Tomador, Serviço, Valores/Tributação, and the final review page;
- the final DANFSe PDF;
- the final signed NFS-e XML;
- prior successful NFS-e evidence and reconstructed invoice/payment history already available in the working context.

Do not commit those real source documents or identifiers to the public repository. Copy/inventory the final PDF/XML under ignored `private/sources/2026/09/nfse/` locally if not already done.

## Result

The NFS-e was successfully issued.

The final PDF/XML agreed on the source-backed September competence, recurring dentistry service, Barretos service location, Itupeva ISS incidence, no ISS retention, no federal contribution withholding, and the billing-request additional text.

The signed XML also confirmed several machine-readable carry-forward values for future National NFS-e runs:

- ME/EPP Simples option;
- federal and municipal apuração through Simples Nacional;
- dentistry national service code;
- dentistry NBS;
- PIS/COFINS CST `00`;
- PIS/COFINS/CSLL non-retained;
- the Simples approximate-tax-rate field (`pTotTribSN`) when selected.

## What worked

- Starting from the actual current billing request to obtain current-period variable data.
- Reusing the established monthly invoice history to resolve the monthly sequence instead of treating the current request as isolated.
- Inspecting live HTML to identify exact options and hidden/underlying values.
- Using the prior successful NFS-e as the comparison point for federal/municipal withholding treatment.
- Selecting NBS `123012300 - Serviços odontológicos`, which is now explicitly required by the portal.
- Stopping at the review page before final emission.
- Using the signed XML after emission to confirm the actual machine-readable submission rather than relying only on the preview/PDF.

## What added unnecessary operator work

- Asking the operator to decide the competence month before first reconciling the recurring history.
- Repeating long lists of readonly/default fields instead of identifying only editable selections and anomalies.
- Requiring multiple copy/pastes of large HTML option lists when a supplied page/file could be parsed directly.
- Treating the visible `Opção no Simples Nacional: NENHUM` label as potentially blocking before inspecting the underlying value/final XML.
- Spending too much attention on the IBS/CBS recipient prompt while IBS/CBS was disabled for the current workflow and no separate recipient existed.

## Important non-carry-forward fields

Future agents must not blindly copy:

- competence day/month;
- gross amount;
- billing-request additional-information text;
- approximate Simples rate.

The monthly sequence should be reconstructed first; exact competence comes from current evidence. The approximate Simples rate must be recomputed when Factor R/Annex treatment changes.

## Files changed

- `docs/instructions/nfse.md`: expanded into the full National NFS-e runbook, recurring profile, stop conditions, review/evidence steps, and interaction lessons.
- `docs/agent/current-state.md`: marks the September NFS-e issued and records the final XML/PDF validation.
- `docs/agent/open-questions.md`: removes stale NFS-e work and moves focus to private evidence inventory, cash receipt, September payroll, and Factor R.
- `docs/agent/log.md`: logs the successful National NFS-e run and documentation work.
- this handoff.

## Commands/tools

No local checkout was available in this connector-only session, so no local shell commands or `git status` were run. Repository reads/writes were performed through the GitHub connector. The human operator performed all government-portal actions.

## Remaining next actions

1. Ensure the final September PDF/XML and current request are stored/inventoried in ignored private evidence.
2. Wait for/confirm the actual September customer cash receipt and record its date separately from competence/issue date.
3. Re-run the September pró-labore decision from current cash, annual taxable-income projection, and Factor R strategy.
4. If the current September pró-labore candidate remains appropriate, prefer payment within September when cash permits so it enters the Factor R lookback earlier.
5. Recompute the NFS-e approximate Simples rate before the next invoice if Factor R/Annex treatment changes.

## Suggested next prompt

`Read the current state, the NFS-e runbook, and the long-term strategy. Reconcile the latest bank receipt and tell me exactly what September payroll/eSocial action is next, including whether the current pró-labore candidate still makes sense for Factor R.`
