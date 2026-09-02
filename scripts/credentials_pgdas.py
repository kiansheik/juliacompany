#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from company_ops import PRIVATE


DEFAULT_SECRET_NOTE = PRIVATE / "secrets" / "portal-notes" / "pgdas-esocial-access-notes.md"
FIELDS = [
    ("CPF", re.compile(r"^\s*CPF\s*:\s*(\S+)\s*$", re.IGNORECASE | re.MULTILINE)),
    ("CNPJ", re.compile(r"^\s*CNPJ\s*:\s*(\S+)\s*$", re.IGNORECASE | re.MULTILINE)),
    (
        "Codigo de Acesso",
        re.compile(r"^\s*C[oó]digo\s+de\s+Acesso\s*:\s*(\S+)\s*$", re.IGNORECASE | re.MULTILINE),
    ),
]


def load_credentials(path: Path) -> list[tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    credentials: list[tuple[str, str]] = []
    missing: list[str] = []
    for label, pattern in FIELDS:
        match = pattern.search(text)
        if match:
            credentials.append((label, match.group(1)))
        else:
            missing.append(label)
    if missing:
        raise ValueError(f"missing fields in {path}: {', '.join(missing)}")
    return credentials


def copy_to_clipboard(value: str, *, dry_run: bool = False) -> None:
    if dry_run:
        return
    try:
        subprocess.run(["pbcopy"], input=value, text=True, check=True)
    except FileNotFoundError as exc:
        raise RuntimeError("pbcopy was not found; this helper currently expects macOS.") from exc
    except subprocess.CalledProcessError as exc:
        raise RuntimeError("pbcopy failed.") from exc


def run_sequence(credentials: list[tuple[str, str]], *, dry_run: bool = False, clear_at_end: bool = True) -> None:
    for index, (label, value) in enumerate(credentials):
        copy_to_clipboard(value, dry_run=dry_run)
        if dry_run:
            print(f"Validated {label}.")
            continue
        if index < len(credentials) - 1:
            next_label = credentials[index + 1][0]
            input(f"Copied {label}. Paste it in the portal, then press Enter for {next_label}.")
        else:
            if clear_at_end:
                input(f"Copied {label}. Paste it in the portal, then press Enter to clear the clipboard.")
                copy_to_clipboard("", dry_run=False)
                print("Clipboard cleared.")
            else:
                print(f"Copied {label}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Copy PGDAS-D login fields to the macOS clipboard one at a time without printing values."
    )
    parser.add_argument("--secret-note", default=str(DEFAULT_SECRET_NOTE), help="Private note containing CPF, CNPJ, and access code.")
    parser.add_argument("--dry-run", action="store_true", help="Validate the private note without copying values.")
    parser.add_argument("--no-clear", action="store_true", help="Leave the final value on the clipboard.")
    args = parser.parse_args()

    try:
        credentials = load_credentials(Path(args.secret_note))
        run_sequence(credentials, dry_run=args.dry_run, clear_at_end=not args.no_clear)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
