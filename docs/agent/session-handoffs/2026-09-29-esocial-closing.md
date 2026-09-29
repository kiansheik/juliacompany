# Session Handoff: September 2026 eSocial Closing

Date: 2026-09-29

## Goal

Finish the September working-partner payroll flow in eSocial, close PA 09/2026, verify automatic DCTFWeb transmission, and preserve the reusable portal behavior for future months.

## Result

The operator completed the September payroll flow and downloaded the S-1299 event/receipt XML.

The reviewed XML confirms:

- period: 09/2026;
- remuneration information present;
- payment information present;
- immediate DCTFWeb transmission requested;
- processing response: `202 - Sucesso com advertência`;
- warning code `1727`;
- DCTFWeb message `446`, confirming successful transmission.

This is a successful close/transmission result.

## Evidence handling

The raw XML and result PDF contain real identifiers, receipt/protocol values and other private filing evidence. They belong under the ignored local September payroll/eSocial source tree and must not be committed to the public repository.

Tracked `main` stores only sanitized workflow/results.

## Durable lesson

When remuneration and payment both occur in the same PA, S-1299 should report both categories as present. A `202 - Sucesso com advertência` result with warning `1727` and DCTFWeb message `446` can represent a successful close and successful automatic DCTFWeb transmission.

After that result:

1. enter e-CAC in company/legal-representative context;
2. locate PA 09/2026 in DCTFWeb;
3. verify the declaration directly;
4. save receipt/extract;
5. generate the DARF;
6. pay separately;
7. save bank proof separately.

Do not treat a generated DARF as proof of payment.

## What waits

PGDAS-D PA 09/2026 should be handled after September ends. Reconcile competence and cash from source evidence and trust the live Factor R result rather than assuming Annex III.

## Files changed

- `docs/agent/current-state.md`
- `docs/agent/open-questions.md`
- `docs/agent/log.md`
- `docs/instructions/esocial.md`
- this handoff

## Suggested next prompt

`I am in e-CAC after the successful September S-1299/DCTFWeb transmission. Walk me through finding PA 09/2026, verifying the declaration, generating the DARF, and checking the amount before I pay it.`
