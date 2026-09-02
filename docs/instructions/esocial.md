# eSocial Workflow

Use private credentials only from `private/secrets/`.

Record payroll competence separately from payment date. For pró-labore, keep evidence for:

- S-1200 remuneration.
- S-1210 payment, if applicable.
- S-1299 closing.
- Closing response warnings.
- DCTFWeb transmission status.

Do not close payroll or submit events from a script. Use generated reports as entry instructions only.

## Start of a monthly payroll run

Observed in the live eSocial Web Geral Pessoa Jurídica flow in September 2026.

1. Enter eSocial under the company/employer profile, not merely the representative's personal profile.
2. Open **Folha de Pagamento > Gestão de Folha**.
3. Select the target competence.
4. Confirm whether the period is open or closed before editing anything.

For an open competence, the main `Eventos de Folha` section exposes at least:

- **Trabalhadores > Remuneração Devida**: S-1200 remuneration for the selected competence.
- **Trabalhadores > Pagamentos**: S-1210 payments whose payment event belongs to the selected period.

The underlying links include the selected competence, for example `Competencia=YYYYMM`, which is a useful sanity check that the operator is editing the intended month.

For ordinary pró-labore work, start with **Remuneração Devida**. Do not begin by entering a payment merely because the bank transfer is happening now. First establish the remuneration in the competence to which the work belongs.

The same Gestão de Folha page may also show unrelated event families such as production rural, avulsos, informações complementares, and contribuição sindical patronal. Do not populate these unless source evidence shows that they apply.

### What to capture from each live screen

Every time a recurring eSocial screen is encountered, document the following in this file or a linked runbook:

- exact menu path and screen title,
- exact field labels shown by the portal,
- which month/date concept each field represents,
- which internal/private source supplies the value,
- any default/blank fields that should normally remain untouched,
- validation messages or portal-calculated values,
- buttons used to save/advance/transmit,
- receipts/XML/downloads available afterward,
- any difference between the live UI and this documentation.

Tracked documentation must stay sanitized. Actual CPF/CNPJ, receipt numbers, bank details, real payment amounts, and source documents remain under ignored `private/` state.

## Remuneration versus payment month

The live workflow must preserve two different timelines:

- S-1200 belongs to the remuneration competence.
- S-1210 belongs to the month in which payment actually occurs and references the competence/demonstrative being paid.

If remuneration for one month is paid in the following month, do not move the remuneration competence merely to make the payment dates line up.

For S-1210, record at least:

- actual payment date,
- competence to which the payment refers,
- source S-1200 demonstrative/identifier,
- net amount actually paid,
- bank payment evidence.

The eSocial Manual Web Geral states that `Data do Pagamento` must fall within the selected payment event period and that `Competência a que se refere o pagamento` identifies the remuneration competence being paid.

Official source, last verified 2026-09-02:
https://www.gov.br/esocial/pt-br/empresas/manual-web-geral/manual-web-geral/

## Closing and DCTFWeb

On the Gestão de Folha page, a closed period displays `Situação da Folha: Fechada` and offers `Reabrir Folha`. Do not reopen a closed period merely to reach DCTFWeb.

The S-1299 closing XML/receipt can include `transDCTFWeb=S`. A successful closing response may explicitly say DCTFWeb transmission was completed and instruct the user to access e-CAC to generate the arrecadação document.

Treat these as separate facts:

1. eSocial period is closed.
2. DCTFWeb transmission succeeded.
3. DCTFWeb declaration is active.
4. DARF was generated.
5. DARF was actually paid.

Each step needs its own evidence when available.
