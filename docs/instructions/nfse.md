# NFS-e Workflow

Use the National NFS-e issuer at `https://www.nfse.gov.br/EmissorNacional/` and choose the complete-emission flow.

Source evidence belongs in `private/sources/YYYY/MM/nfse/`. Never commit the real billing request, DANFSe, XML, CNPJ, access key, bank/account reference, or other source identifiers to the public repository.

## Goal for future sessions

A future agent should make this a short confirmation workflow, not a field-discovery exercise.

Before the operator opens the portal, the agent should read:

1. the current billing request/source evidence;
2. the latest successful NFS-e XML;
3. `private/state/invoices.json` and the current monthly reconstruction;
4. `docs/agent/long-term-strategy.md` when a tax-rate disclosure may depend on the current Simples/Factor R strategy.

Then produce a compact per-screen answer sheet containing only:

- fields the operator must actively fill or select;
- values that differ from the last successful invoice;
- any stop condition requiring review.

Do not ask the operator to rediscover a value that can be reconstructed from source evidence plus the established recurring history.

## Current recurring profile

These are stable carry-forward defaults observed in the successful National NFS-e workflow. Reconfirm them against the latest successful XML, but do not ask the operator about them every month unless something changed.

| Portal field | Carry-forward rule |
| --- | --- |
| Emitente | `Prestador/Fornecedor` |
| Município do prestador | Itupeva/SP, portal-derived |
| Simples Nacional | Optante ME/EPP; underlying National NFS-e value observed as `opSimpNac=3` |
| Regime de apuração SN | `Regime de apuração dos tributos federais e municipal pelo Simples Nacional`; XML value observed as `regApTribSN=1` |
| Tomador | Use the recurring hospital/foundation customer from private state; search by CNPJ rather than retyping its full profile |
| Intermediário | Não informado |
| Local da prestação | Barretos/SP |
| Código de Tributação Nacional | `04.12.01 - Odontologia` |
| NBS | `123012300 - Serviços odontológicos` |
| Descrição do serviço | `Prestação de serviços odontológicos` |
| Imunidade/exportação/não incidência | `Não` |
| ISSQN | Operação Tributável |
| Regime Especial de Tributação | Nenhum |
| Suspensão do ISSQN | Não |
| Retenção do ISSQN | Não |
| Benefício municipal | Não |
| Dedução/redução da base | Não |
| PIS/COFINS CST | `00 - Nenhum` |
| Retenção PIS/COFINS/CSLL | `0 - PIS/COFINS/CSLL Não Retidos` |
| IRRF / CP retida | zero/blank unless current source evidence or law says otherwise |
| IBS/CBS | For the observed 2026 workflow, `Preencher as informações IBS/CBS = NÃO`; this is time-sensitive and must be rechecked when the rules/company treatment change |

The final successful XML is the best machine-readable source for these carry-forward values. The PDF is useful for human review, but some portal choices are clearer in the XML than in the DANFSe.

## Values that must not be blindly carried forward

### Competence

Do not assume issue date equals service competence, and do not hardcode the day of month.

For the recurring monthly hospital billing, first reconstruct the sequence from prior invoices and the current billing request. The month can usually be inferred from the established one-request/one-service-period cadence without asking the operator. Only ask when there is evidence of a catch-up, duplicate, cross-month service period, or another conflict.

The exact competence date should follow the current request/service evidence. Past startup months included irregular and cross-month dates, so `01/MM/YYYY` is not a universal rule.

### Gross service amount

Read from the current billing request/private state. The recurring amount may be stable, but public docs must not hardcode the real amount.

### Informações complementares

Copy exactly from the current billing request. Do not silently copy last month's funding agreement/account/reference text merely because it repeated previously.

### `Alíquota no Simples Nacional` for approximate-tax disclosure

The National issuer offers `Informar alíquota do Simples Nacional` under `Valor aproximado dos tributos` for ME/EPP.

Use the currently supported effective Simples rate from the active tax strategy / most recent authoritative PGDAS result. Do not permanently hardcode the rate observed in one invoice. A Factor R move between Annex V and Annex III can change the rate that should be disclosed.

The successful XML stores this choice as `pTotTribSN`. The DANFSe may still render the approximate federal/state/municipal totals as dashes, so absence of numeric totals on the PDF does not by itself prove the rate was lost.

## Screen-by-screen workflow

### 1. Pessoas / Informações Gerais

Actively set or verify:

- `Preencher as informações IBS/CBS`: current-period answer from the rule check; observed 2026 workflow used `NÃO`.
- `Data de Competência`: source-backed competence date.
- leave DPS série/número automatic unless there is a specific reason not to.
- emit as `Prestador/Fornecedor`.

The portal may display a confusing visible `Opção no Simples Nacional: NENHUM` while the underlying submitted value indicates ME/EPP. When HTML or final XML is available, inspect the underlying value before treating this as an error. In the successful workflow, final XML confirmed ME/EPP and the normal Simples regime.

Select `Regime de apuração dos tributos federais e municipal pelo Simples Nacional`.

### 2. Tomador/Adquirente

- location: Brasil;
- search the recurring customer by CNPJ from private state;
- let the lookup populate legal name/address;
- do not overwrite correct lookup data manually;
- phone/e-mail can remain blank if not supplied;
- intermediary remains not informed.

If asked `Para fins de apuração do IBS/CBS, o destinatário é o próprio adquirente?`, the observed relationship is yes: there is no distinct third-party recipient. With IBS/CBS not being filled in the observed 2026 workflow, this had no separate tax amount on the resulting document. Do not spend extra operator time on it unless IBS/CBS treatment changes.

### 3. Serviço

Verify:

- Brasil;
- Barretos/SP as local da prestação;
- `04.12.01 - Odontologia`;
- `Não` for imunidade/exportação/não incidência;
- municipality of ISS incidence resolves to Itupeva/SP;
- NBS `123012300 - Serviços odontológicos`;
- description `Prestação de serviços odontológicos`.

Leave construction/property and foreign-commerce sections unused.

Under `Informações Complementares`, leave responsibility-technical-document/reference/order fields blank unless the current source explicitly supplies them. Put the current request's additional text in `Informações complementares` exactly as supplied.

### 4. Valores / Tributação

Enter the current gross service amount.

Normally keep:

- no intermediary value;
- no conditional/unconditional discount;
- Operação Tributável;
- no special tax regime;
- no ISS suspension;
- no ISS retention;
- no municipal benefit;
- no deduction/reduction;
- PIS/COFINS CST `00 - Nenhum`;
- `0 - PIS/COFINS/CSLL Não Retidos`;
- IRRF and contribuição previdenciária retida blank/zero.

Do not confuse a portal municipal ISS parameter (for example a hidden parametrized minimum rate) with the Simples rate. When ISS is being apportioned by Simples Nacional, the portal itself may leave ISS base, applied rate, and ISS amount blank on the preview/DANFSe.

Under `Valor aproximado dos tributos`, use `Informar alíquota do Simples Nacional` and enter the current supported rate from the tax strategy. Recompute this when Factor R/Annex treatment changes.

### 5. Review page before emission

Always stop once at the review page before the final `Emitir NFS-e` action.

Reconcile at minimum:

- competence;
- issuer and recurring customer;
- service code and NBS;
- Barretos service location and Itupeva ISS incidence;
- exact service description;
- exact current additional-information text;
- gross amount;
- no discounts/retentions unless specifically expected;
- PIS/COFINS treatment;
- net amount equals gross amount when there are no retentions/discounts.

It is expected in the observed Simples workflow that the preview can show `Base de cálculo`, `Alíquota aplicada`, and `ISSQN` as `-` while the NFS-e remains correct.

The human operator, not an agent/script, performs the final emission.

### 6. Evidence after emission

Download/save both:

- DANFSe PDF;
- signed NFS-e XML.

The XML should be used to validate the actual submitted values, including competence, Simples option/regime, customer, service location/code/NBS, description, amount, ISS retention, PIS/COFINS treatment, additional text, and `pTotTribSN` when used.

Record in `private/state/invoices.json`:

- NFS-e number;
- issue date/time;
- service competence date;
- gross amount;
- service and ISS-incidence municipalities;
- service code/NBS;
- ISS retention flag;
- payer reference;
- source inventory IDs for PDF/XML and current request.

Keep issue date, competence, and later cash-receipt date separate so PGDAS can use competence history and cash-basis revenue correctly.

## Interaction lessons from the 2026-09-02 live run

### Questions/checks that were useful

- requesting the current billing request before emission, because it supplied the current amount, customer, description, and exact additional-information text;
- checking the live HTML when the visible Simples label looked inconsistent;
- identifying the new required NBS field from the actual portal options;
- checking the editable federal-tax section and mapping it to the prior successful NFS-e treatment;
- stopping on the final review page before emission;
- validating the issued PDF and XML afterward.

### Questions/checks that added unnecessary work

- reflexively asking the operator to decide the competence month when the recurring history plus current request already resolved the monthly sequence; future agents should reconstruct first and ask only on conflict;
- repeating every readonly or already-populated field instead of returning only active selections and anomalies;
- asking for separate copy/pastes of giant option lists when the operator has supplied the page HTML/file; parse the supplied page and identify the exact option directly;
- over-focusing on the visible `NENHUM` Simples label without first inspecting the underlying form value/final XML;
- treating the IBS/CBS recipient question as a major decision when the current workflow had IBS/CBS disabled and no separate recipient.

## Preferred future-agent response format

For each portal page, answer in this compact form:

```text
Fill/select:
- <field>: <value>
- <field>: <value>

Leave alone:
- <readonly/default fields that are already correct>

Stop only if:
- <specific mismatch that would change the invoice>
```

If all recurring defaults are already populated correctly, say so and list only the one or two fields the operator must touch. The objective is progressively less copy/paste every month.
