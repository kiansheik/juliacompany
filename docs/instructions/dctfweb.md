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

## Access path observed in September 2026

1. Enter e-CAC.
2. Switch the e-CAC access profile to the company/legal-representative context before searching company DCTFWeb declarations.
3. Open `Declarações e Demonstrativos > Assinar e Transmitir DCTFWeb`.

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
