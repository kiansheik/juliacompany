# Monthly Cycle

1. Add source documents to `private/sources/YYYY/MM/`.
2. Run `python3 scripts/inventory.py`.
3. Update private state files from evidence.
4. Run `python3 scripts/check.py`.
5. Run `python3 scripts/month.py YYYY-MM`.
6. Read the relevant portal instructions under `docs/instructions/` before opening the portal.
7. Review generated values against source evidence before entering anything.
8. Work through the live portal one screen at a time. If the screen differs materially from the docs, stop and reconcile the difference instead of guessing.
9. After each portal action, save receipts/proofs under `private/sources/YYYY/MM/`.
10. If a screen taught us something new, save the screenshot/HTML/text privately and update the corresponding tracked instruction document with a sanitized description of the screen, field labels, and mapping rules.
11. Re-run inventory and update private state with submission/payment evidence.
12. Update `docs/agent/current-state.md`, `docs/agent/open-questions.md`, and a session handoff when significant work was completed.

Never transmit or pay from a script. Scripts prepare instructions and checks only.

## Portal-session rule

The goal is not merely to finish today's filing. Each live filing should reduce uncertainty for the next month.

For every recurring screen, capture enough knowledge that a future agent can answer:

- What menu path opens this screen?
- What exact field labels does the portal use?
- Which internal data maps to each field?
- Which values are current-period versus historical/lookback values?
- What must reconcile before continuing?
- What special selectors should normally remain blank?
- What receipt or proof should be downloaded afterward?
- Is declaration submission separate from document generation or payment?

Keep real identifiers and amounts in ignored private state. Tracked docs should describe the reusable workflow with variables or sanitized examples.
