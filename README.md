# Julia Company Operations Toolkit

This repository is an operational toolkit for recurring administration of a small Brazilian company. It is designed to be safe for a public GitHub repository while consuming private local evidence kept outside Git.

## Public vs Private

- Public files: docs, workflows, schemas, scripts, templates, sanitized examples, and tests with fictional data.
- Private files: source PDFs/XMLs, statements, receipts, credentials, real identifiers, real values, reconstructed state, generated monthly reports, and portal session notes.

Everything under `private/` is ignored by Git.

## Initialize Local State

```bash
mkdir -p private/{sources,state,generated,secrets}
cp config/company.example.yaml private/state/company.yaml
```

Add monthly source documents under `private/sources/YYYY/MM/` and keep source evidence immutable after organization.

## Common Commands

```bash
python3 scripts/inventory.py
python3 scripts/reconcile.py
python3 scripts/month.py 2026-07
python3 scripts/pgdas.py 2026-07
python3 scripts/payroll.py 2026-08 --gross 5000
python3 scripts/check.py
make check
make credentials-pgdas
```

## Monthly Agent Start

1. Read `AGENTS.md`.
2. Run `git status --short` and confirm private material is ignored.
3. Run `python3 scripts/inventory.py`.
4. Run `python3 scripts/month.py YYYY-MM`.
5. Update private state from source evidence, not memory.
6. After the filing session, update generic docs and private state with what changed.

Generated checklists are written to `private/generated/`.
