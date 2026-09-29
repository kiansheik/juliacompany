# DCTFWeb Workflow

DCTFWeb status must not be inferred solely from eSocial closing. Record direct DCTFWeb receipt/payment evidence when available.

For each period, track:

- period,
- source system,
- transmission status,
- generated DARF amount,
- due date,
- payment status,
- payment date,
- source inventory IDs.

Any current deadline or rule must be verified against official sources before live use.

## Exact entry links

When telling the operator to use DCTFWeb, always provide the exact clickable URL and the exact menu path. Do not make the operator search.

Preferred e-CAC login:
https://cav.receita.fazenda.gov.br/autenticacao/login/index

After login, switch to the company/legal-representative context, then:
**Declarações e Demonstrativos > Assinar e Transmitir DCTFWeb**

Direct DCTFWeb application URL after authentication:
https://dctfweb.cav.receita.fazenda.gov.br/aplicacoesweb/DCTFWeb/Default.aspx

If the direct application URL redirects or stops working, use the e-CAC login URL and the menu path above, then update this runbook if Receita changed the route.

## Access path observed in September 2026

1. Enter e-CAC using the exact link above.
2. Switch the e-CAC access profile to the company/legal-representative context before searching company DCTFWeb declarations.
3. Open **Declarações e Demonstrativos > Assinar e Transmitir DCTFWeb**.

If eSocial shows a successful DCTFWeb transmission but the DCTFWeb page returns no declaration, first verify the e-CAC profile. Searching from the representative's personal CPF context can produce an empty result even though the company declaration exists.

## Declaration-list filters

The observed page includes:

- `Período Apuração Inicial`
- `Período Apuração Final`
- `Data Transmissão Inicial`
- `Data Transmissão Final`
- `Categoria Declaração`
- `Situação Declaração`
- optional `Com saldo a pagar`

A direct eSocial transmission can occur before the date on which the operator later visits DCTFWeb, so do not use an overly recent `Data Transmissão Inicial` filter.

For normal company payroll, expect category `Geral`. A successfully transmitted current declaration can appear as `Ativa`.

## Declaration row

The observed result table includes:

- Período de Apuração
- Data Transmissão
- Categoria
- Origem
- Tipo
- Situação
- Débito Apurado
- Saldo a Pagar
- Serviços

For a direct payroll transmission, `Origem` can be `eSocial` and `Tipo` can be `Original`.

The service icons observed include:

- Visualizar
- Retificar
- Visualizar Recibo
- Visualizar Extrato de Processamento

Do not click `Retificar` unless a real correction is required.

## Generating the DARF

The checkbox next to `Saldo a Pagar` is labeled/tooled as `Emitir Darf`. Select the intended declaration and use the page's `Emitir DARF` control.

Before payment, save privately when available:

- declaration view/PDF,
- DCTFWeb receipt,
- processing extract,
- generated DARF.

For an overdue period, let DCTFWeb/SENDA calculate multa and juros. Do not manually alter the principal.

After payment, save the bank/PIX receipt separately. The generated DARF is evidence of the amount requested, not evidence that the bank payment settled.

Prefer payment from the company account so the bookkeeping trail remains clean. If a partner pays personally, flag the transaction for proper accounting treatment rather than pretending company cash paid it.

## Operator-response rule

Whenever a future agent tells the operator to open a recurring government portal, the response should include the exact clickable URL first and then the exact menu path. The purpose of this repository is to eliminate repeated portal searching and navigation rediscovery.


## Important: "Saldo a Pagar" in the declaration list is historical

Receita's official DCTFWeb Q&A states that the `Saldo a Pagar` displayed in the DCTFWeb portal is the historical balance at the moment the declaration was transmitted. It does **not** automatically decrease after a DARF is paid.

Therefore:

- a row that still shows `Saldo a Pagar` does **not** by itself mean the tax is unpaid;
- do not generate/pay a second DARF merely because the declaration list still shows the original balance;
- payment status must be checked from payment evidence and, when needed, the taxpayer's fiscal situation in Receita's service portal.

This behavior was encountered live in September 2026: PA 08/2026 still displayed the original R$ 550,00 balance even though a matching DARF for PA 08/2026 and a company-bank payment proof for R$ 550,00 dated 02/09/2026 had already been retained.

Official source, last verified 2026-09-29:
Receita Federal, Perguntas e Respostas da DCTFWeb, item 1.7 ("O saldo a pagar no Portal da DCTFWeb não diminui automaticamente após a quitação do DARF").
https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/declaracoes-e-demonstrativos/DCTFWeb/arquivos/perguntas-e-respostas-dctfweb-2025-09-23.pdf
