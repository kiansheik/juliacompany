# PGDAS-D Workflow

Use `python3 scripts/pgdas.py YYYY-MM` before entering the portal. This document describes the live PGDAS-D 2018 flow observed in September 2026. Portal labels can change; if the live screen differs, trust the live screen, save the evidence privately, and update this document afterward.

## Before opening PGDAS-D

Reconcile the period from source evidence. At minimum determine:

- service/NFS-e competence by month,
- actual cash receipts by month,
- whether receipts are linked to services from a different competence month,
- payroll/pro-labore history for prior months,
- whether a prior PGDAS period needs correction before the target period,
- whether an existing DAS for the period has already been paid.

For a cash-basis company, never collapse competence and receipt into one date.

## Main menu

Under **Declaração Mensal**, the recurring options observed are:

- **Declarar/Retificar**: create an original declaration or retificadora.
- **Gerar DAS**: generate the payment document after a declaration exists.
- **Consultar Declarações**: inspect originals, retificadoras, generated DAS documents, extracts, and whether a DAS is marked paid.

Declaration transmission and DAS generation are separate operations. A declaration can be successfully transmitted while no DAS appears yet in the consultation table. In that case, use **Gerar DAS** for the PA rather than re-declaring the period.

## Screen 1: Receita Bruta Total do Período de Apuração

The first declaration screen asks for four values:

| Portal field | Internal meaning |
| --- | --- |
| Regime de COMPETÊNCIA - mercado interno | Sum of domestic service revenue whose competence falls in the PA |
| Regime de COMPETÊNCIA - mercado externo | Export revenue by competence, normally zero unless source evidence says otherwise |
| Regime de CAIXA - mercado interno | Sum of domestic cash receipts actually received in the PA |
| Regime de CAIXA - mercado externo | Export cash receipts actually received in the PA, normally zero unless evidence says otherwise |

For a cross-month service, it is valid for one period to contain competence revenue with no corresponding cash and the following period to contain cash revenue with no new competence revenue.

Do not derive the cash value from invoice issue date. Use bank/payment evidence.

### Cumulative sanity checks

After saving the first screen, PGDAS may display values such as `RBA`, `RBT12`, `RBT12p`, and `Receita do PA`.

Use them as diagnostic checks:

- `Receita do PA` should follow the taxable cash-basis amount for the PA when the company is under regime de caixa.
- `RBA` should be consistent with competence revenue accumulated in the current calendar year.
- `RBT12` reflects competence revenue in the months before the PA, not merely cash receipts.
- `RBT12p` can appear while the company is still in its initial months and PGDAS is proportionalizing the historical revenue base.

If a cumulative value implies revenue in a month where source evidence shows none, stop. Inspect and, if necessary, retify the earlier period before continuing the later one.

## Screen 2: Atividades Econômicas com Receita no Período de Apuração

For the currently documented dentistry workflow, the live option used is:

> Prestação de Serviços, exceto para o exterior > Sujeitos ao fator “r”, sem retenção/substituição tributária de ISS, com ISS devido ao próprio Município do estabelecimento

Do not select a different ISS treatment merely because the customer is in another municipality. The correct option must follow the actual service/ISS facts and current rules.

If the service category, Factor R treatment, ISS retention, or municipality is unclear, stop before continuing.

## Screen 3: Receitas / activity segregation

For the selected activity, the screen contains a `Receita (R$)` input and special-treatment selectors under taxes such as COFINS, CSLL, INSS/CPP, IRPJ, ISS, and PIS.

Under regime de caixa, the activity `Receita (R$)` used in the observed workflow is the cash revenue being taxed in that PA, not the larger competence total from Screen 1.

The activity rows across all selected activities must reconcile to the cash revenue for the period.

Leave special-treatment selectors blank unless source evidence and current rules establish a specific treatment such as:

- exigibilidade suspensa,
- lançamento de ofício,
- imunidade,
- redução.

Never choose a special treatment merely to make the calculated tax match an expectation.

## Screen 4: Folha de Salários

For a Factor R activity, PGDAS opens **Folha de Salários, incluídos encargos (até 12 meses anteriores ao Período de Apuração)**.

The portal lists the prior months relevant to the PA. Enter payroll/pro-labore values only for the months shown and only from source-backed payroll state.

Important: do not force payroll from the current PA into a field for a preceding month. If the screen for a PA only offers earlier months, the current month's payroll does not belong in those fields.

After entering the requested history, click **Calcular** and inspect the Factor R / annex result. Do not hardcode an annex from memory.

## Screen 5: Resumo da Declaração

The final summary shows tax due by component and a total. Before clicking **Transmitir**:

- verify that the taxable revenue matches the intended cash-basis amount,
- verify the selected activity,
- verify Factor R / annex result,
- verify that the total is plausible under the current official tax rules,
- stop if the portal unexpectedly taxes the competence total instead of the cash amount.

After transmission, save the declaration and receipt under the private source directory.

## DAS generation and payment

A transmitted declaration does not guarantee that a DAS has already been generated.

After transmission:

1. Check **Consultar Declarações** for the PA.
2. Confirm the declaration number and transmission timestamp.
3. If no DAS row exists, use **Declaração Mensal > Gerar DAS** for the PA.
4. For an overdue period, let PGDAS calculate multa and juros. Do not manually alter the principal.
5. Save the DAS PDF before payment.
6. After payment, save the bank/payment proof.
7. Revisit **Consultar Declarações** later if needed to confirm `Pago = Sim`.

## Retificadoras

Correct earlier periods before later periods when an earlier error changes cumulative revenue or Factor R inputs.

A retificadora may change historical competence data without changing the cash-basis debt for that PA. If the debt is unchanged and the original DAS was already paid, PGDAS may not generate a replacement DAS. Do not pay a duplicate merely because a retificadora was transmitted.

Use **Consultar Declarações** to preserve the chain:

- original declaration,
- original DAS,
- payment status,
- later retificadora,
- any new DAS only if an actual difference is due.

## Stop conditions

Stop before transmission or payment if:

- portal totals differ from source-backed values,
- activity segregation is unclear,
- cumulative values imply a historical month that contradicts evidence,
- Factor R inputs are uncertain,
- an earlier period appears to need retification,
- a DAS may already have been paid,
- the live UI differs materially from this documentation.

## Evidence to retain privately

For every PA, retain as available:

- PGDAS declaration PDF,
- delivery receipt,
- DAS PDF,
- payment proof,
- portal screenshot/HTML snippet when a screen teaches us something new,
- source invoices/NFS-e and bank receipts used to derive the inputs.

Store private evidence under `private/sources/YYYY/MM/pgdas-d/` or the equivalent private month structure.

## Official references

Time-sensitive rules must be reverified before live use. Start with official Simples Nacional / Receita Federal material, including the current PGDAS-D manual and the Simples Nacional legislation/FAQ. Record verification date in any calculation that depends on changing rates, thresholds, deadlines, or Factor R rules.
