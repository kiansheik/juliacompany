# Handoff: 2026-09-02 Bootstrap

## Goal

Turn a messy local folder into a public-safe operational repository with ignored private evidence/state and reusable scripts/docs.

## Files Inspected

- Git status and tracked files.
- Root source PDFs/XMLs/JPGs/text.
- NFS-e XML files.
- eSocial XML files.
- PGDAS-D PDFs via limited local stream extraction.
- Existing credential notes.

## Files Changed

- Added public docs, scripts, schemas, tests, templates, `README.md`, `AGENTS.md`, `.gitignore`, and `Makefile`.
- Moved real source evidence into `private/sources/`.
- Moved credential notes into `private/secrets/portal-notes/`.
- Added private structured state and generated reports under `private/`.

## Commands Run

- `git status --short`
- `git ls-files`
- `find ...`
- `file ...`
- `python3 scripts/inventory.py --source-root . --output private/state/source_inventory.json`
- `python3 scripts/inventory.py --source-root private --output private/state/source_inventory.json`
- `python3 scripts/month.py 2026-07`
- `python3 scripts/month.py 2026-06`
- `python3 scripts/month.py 2026-08`
- `python3 scripts/pgdas.py 2026-07`
- `python3 scripts/reconcile.py`
- `make check`

## What Worked

- No tracked private files were found at start.
- `.gitignore` protects `private/` and common secret/database/key formats.
- XML evidence gave high-confidence invoice and eSocial facts.
- Private state models issue date, competence date, receipt period, payroll competence, filing period, due date, and payment date separately.

## What Failed

- No `docs/agent/` files existed initially.
- `pdftotext` and Python PDF libraries were unavailable.
- PDF extraction was partial; exact PGDAS submission/payment timestamps and some payment dates remain unknown.

## Remaining Questions

- Verify current legal due dates/rules.
- Confirm July PGDAS-D and DCTFWeb/DARF status.
- Find bank statement evidence for exact service receipt and tax payment dates.
- Explain May PGDAS-D retification.

## Suggested Next Prompt

Review `private/generated/current-status.md`, gather missing bank/DCTFWeb/PGDAS evidence, then ask the agent to update private state and produce the next portal instruction sheet.
