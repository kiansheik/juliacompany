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

## Live S-1200 pró-labore entry pattern

Observed for a working partner already registered as a worker without employment bond.

1. Open **Trabalhadores > Remuneração Devida** for the intended competence.
2. Click **Incluir Rubrica**.
3. Keep the existing demonstrative identifier when reusing the normal payroll setup, commonly `001` in the observed setup.
4. Do not mark the FGTS notification/confession checkbox unless source evidence specifically requires it.
5. Select the existing worker contract rather than creating a new category. The observed working-partner contract is category `723 - Contribuinte individual - Empresário, sócio e membro de conselho de administração ou fiscal`.
6. Select the existing tax allocation/lotação from autocomplete. Do not invent a new lotação because the field looks blank on initial load.
7. Select `1 - CNPJ` for establishment type and choose the company establishment from autocomplete.
8. For ordinary current-month remuneration, choose **No período de apuração (MM/AAAA)**, not **Em período anterior**.
9. Use the existing payroll rubrics table and pró-labore rubric from the prior successful month. In the observed setup these are table `001` and code `PROLABORE`.
10. `Quantidade` and `Fator Rubrica` are normally blank for this pró-labore rubric.
11. Enter the planned gross pró-labore in **Valor Total**.
12. Use `0 - Normal (apuração sob a folha de pagamento declarada no eSocial)` for **Indicativo de tipo de apuração de IR**, unless there is a documented special case.
13. Click **Incluir**. This only adds the rubric to the on-screen remuneration form.
14. Verify the resulting `Relação de Rubricas`: table, code, type `Vencimento`, description, gross value, and `IndIR=0`.
15. Scroll to the bottom and click **Salvar**. This is the action that saves/transmits the S-1200 remuneration event.

Do not populate **Remunerações em Outras Empresas/Atividades** merely because the accordion appears. It is relevant only when the worker personally has contributory remuneration from another employer/activity that must be considered for the period. Company revenue paid by a customer to the company is not another personal remuneration for this purpose.

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

### Live S-1299 closing screen

After the S-1200 remuneration has been saved, return to the target competence and click **Encerrar Folha**. The screen title is **Encerramento da Folha** and should still show the intended `Período de Apuração` and `Situação da Folha: Aberta` before submission.

For the ordinary single-partner pró-labore situation observed in 2026, with remuneration in the competence but no payment event occurring in that same month, the expected answers are:

- **Possui informações relativas a remuneração de trabalhadores ou provento/pensão de beneficiários no período de apuração?** → `Sim`.
- **Possui informações de pagamento de rendimentos do trabalho no período de apuração?** → `Não` when the pró-labore will actually be paid in the following month and therefore its S-1210 belongs to that later payment month.
- **Possui informações de comercialização de produção?** → `Não` unless actually applicable.
- **Contratou, por intermédio de sindicato, serviços de trabalhadores avulsos não portuários?** → `Não` unless actually applicable.
- **Possui informações de desoneração de folha de pagamento ou, sendo empresa enquadrada no Simples, possui informações sobre receita de atividades com contribuição previdenciária concomitantemente substituída e não substituída?** → `Não` for the observed ordinary dentistry-only setup; re-evaluate if activities or tax treatment change.
- **Indicativo de exclusão de apuração das aquisições de produção rural (S-1250)** → `Não` in the observed setup.
- **Indicativo de não validação das regras de fechamento** → `Não`; do not bypass validations merely to force a closing.

Mark **Solicitação de transmissão imediata da DCTFWeb** when the intent is to have the accepted S-1299 automatically transmit the resulting DCTFWeb. The official eSocial Web Geral manual states that this checkbox requests automatic DCTFWeb transmission and that the S-1299 return reports whether the request was accepted.

Then click **Salvar**. Closing is asynchronous in Web Geral: return to **Gestão de Folha**, expand **Resultado do processamento - Fechamentos solicitados pela web**, and refresh until a processed result appears. Verify that the period becomes `Fechada` before treating the closing as complete.

After successful processing, retain private evidence when available:

- S-1299 XML/event data,
- S-1299 processing/receipt response,
- any warning/error text,
- whether immediate DCTFWeb transmission was accepted,
- later DCTFWeb declaration and DARF evidence.

Official source, last verified 2026-09-02:
https://www.gov.br/esocial/pt-br/empresas/manual-web-geral/

The S-1299 closing XML/receipt can include `transDCTFWeb=S`. A successful closing response may explicitly say DCTFWeb transmission was completed and instruct the user to access e-CAC to generate the arrecadação document.

Treat these as separate facts:

1. eSocial period is closed.
2. DCTFWeb transmission succeeded.
3. DCTFWeb declaration is active.
4. DARF was generated.
5. DARF was actually paid.

Each step needs its own evidence when available.
