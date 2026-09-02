# Agent Instructions

This repository is public-safe by design. Treat anything private as permanently unsafe to commit.

## Start Every Session

1. Run `git status --short`.
2. Read `docs/agent/index.md`, `docs/agent/current-state.md`, `docs/agent/repo-map.md`, and `docs/agent/open-questions.md`.
3. Do not run `git add -A`.
4. Do not commit or push unless explicitly asked.
5. Stop and report immediately if any private source document, credential, CPF/CNPJ, access code, bank identifier, or real source file is tracked.

## Evidence First

Never infer a filing from memory when source documents exist. Distinguish:

- fact from source evidence,
- calculated value,
- legal or tax rule,
- assumption,
- unresolved question.

When reconciling a month, cite the local source filename or inventory ID supporting every important fact.

## No Blind Tax Automation

Scripts may calculate, reconcile, validate, and generate instructions. They must not automatically transmit declarations, close payroll, submit eSocial events, issue DAS/DARF, pay anything, alter a government filing, or destructively interact with a portal without explicit human authorization.

Normal output should be human-readable instructions telling the operator what to enter and where.

## Portal and Rule Drift

Government websites and tax rules change. When a portal screen differs from documentation, trust the current screen, record what changed, and update the workflow afterward.

Any rule that can change must carry a source, effective date, and date last verified. A future agent with web access should verify time-sensitive rules before using them for a new period.

## Do Not Conflate Dates

Keep these independent: NFS-e issue date, service competence, cash receipt date, PGDAS assessment period, payroll competence, payroll payment date, eSocial event period, DCTFWeb period, tax due date, and actual tax payment date.

## Do Not Conflate IR Concepts

Keep separate monthly IRRF, annual taxable income, whether tax is ultimately owed, and whether DIRPF filing is mandatory. Zero monthly IRRF does not prove that no annual return is required.

## After Significant Work

Update `docs/agent/current-state.md`, `docs/agent/log.md`, and add a new file under `docs/agent/session-handoffs/` with goal, files inspected, files changed, commands run, what worked, what failed, remaining questions, and suggested next prompt.
