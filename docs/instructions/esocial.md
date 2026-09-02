# eSocial Workflow

Use private credentials only from `private/secrets/`.

Record payroll competence separately from payment date. For pró-labore, keep evidence for:

- S-1200 remuneration.
- S-1210 payment, if applicable.
- S-1299 closing.
- Closing response warnings.
- DCTFWeb transmission status.

Do not close payroll or submit events from a script. Use generated reports as entry instructions only.

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
