#!/usr/bin/env python3
from __future__ import annotations

import argparse
import mimetypes
import re
from pathlib import Path
from typing import Any

from company_ops import (
    ROOT,
    SOURCES,
    STATE,
    all_text,
    classify_path,
    looks_sensitive,
    money,
    parse_xml,
    period_from_date,
    read_json,
    sha256_file,
    text_at,
    write_json,
)


SKIP_DIRS = {".git", "docs", "scripts", "schemas", "tests", "config", "state", "generated", "__pycache__"}


def safe_doc_id(path: Path, digest: str) -> str:
    stem = re.sub(r"[^a-z0-9]+", "-", path.stem.lower()).strip("-")[:40] or "source"
    return f"src-{digest[:12]}-{stem}"


def iter_files(source_root: Path) -> list[Path]:
    files = []
    for path in source_root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name == ".gitignore":
            continue
        files.append(path)
    return sorted(files)


def infer_metadata(path: Path) -> dict[str, Any]:
    doc_type, portal, evidence_kind = classify_path(path)
    data: dict[str, Any] = {
        "document_type": doc_type,
        "portal_or_system": portal,
        "evidence_kind": evidence_kind,
        "apparent_period": None,
        "issue_date": None,
        "competence_date": None,
        "payment_date": None,
        "amount": None,
        "confidence": "low",
        "notes": [],
    }

    root = parse_xml(path) if path.suffix.lower() == ".xml" else None
    if root is not None:
        if text_at(root, "nNFSe"):
            issue = text_at(root, "dhEmi")
            competence = text_at(root, "dCompet")
            amount = money(text_at(root, "vServ") or text_at(root, "vLiq"))
            data.update(
                {
                    "document_type": "nfse",
                    "portal_or_system": "municipal_nfse",
                    "evidence_kind": "invoice",
                    "apparent_period": period_from_date(competence or issue),
                    "issue_date": issue[:10] if issue else None,
                    "competence_date": competence,
                    "amount": str(amount) if amount is not None else None,
                    "confidence": "high",
                    "nfse_number": text_at(root, "nNFSe"),
                    "service_description": text_at(root, "xDescServ"),
                    "municipality_code": text_at(root, "cLocPrestacao") or text_at(root, "cLocIncid"),
                    "iss_retained": text_at(root, "tpRetISSQN"),
                }
            )
            if issue and competence and period_from_date(issue) != period_from_date(competence):
                data["notes"].append("Issue month differs from service competence month.")
        elif text_at(root, "perApur") or text_at(root, "iniValid"):
            per_apur = text_at(root, "perApur") or text_at(root, "iniValid")
            receipt = text_at(root, "nrRecibo")
            amount = money(text_at(root, "vrPerRef") or text_at(root, "valor"))
            data.update(
                {
                    "document_type": "esocial",
                    "portal_or_system": "esocial",
                    "evidence_kind": "event_receipt",
                    "apparent_period": per_apur,
                    "amount": str(amount) if amount is not None else None,
                    "confidence": "medium" if amount is None else "high",
                    "esocial_receipt": receipt,
                    "submission_timestamp": text_at(root, "dhRecepcao"),
                    "response": text_at(root, "descResposta"),
                }
            )
            if text_at(root, "evtRemun") or text_at(root, "evtPgtos"):
                data["notes"].append("eSocial closing event indicates remuneration/payment events existed.")

    if path.suffix.lower() in {".txt", ".md"}:
        text = path.read_text(encoding="utf-8", errors="replace")
        if "Distribuição de lucros" in text or "Distribuicao de lucros" in text:
            data.update({"document_type": "profit_distribution", "evidence_kind": "distribution_note", "confidence": "medium"})
            period_match = re.search(r"referente a\s+(\d{2})/(\d{4})", text, re.I)
            if period_match:
                data["apparent_period"] = f"{period_match.group(2)}-{period_match.group(1)}"
            amount_match = re.search(r"Receita recebida.*?R\$\s*([\d\.\,]+)", text, re.I)
            if amount_match:
                amount = money(amount_match.group(1))
                data["amount"] = str(amount) if amount is not None else None
        if re.search(r"senha|c[oó]digo de acesso|cpf|cnpj", text, re.I):
            data["notes"].append("Contains credentials or private identifiers.")

    if data["apparent_period"] is None:
        match = re.search(r"20\d{2}[-_/ ]?(0[1-9]|1[0-2])|(?:jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez|janeiro|fevereiro|marco|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)", str(path).lower())
        if match:
            data["notes"].append("Period inferred weakly from filename/path.")

    return data


def build_inventory(source_root: Path, output: Path) -> list[dict[str, Any]]:
    existing = {item["sha256"]: item for item in read_json(output, []) if "sha256" in item}
    records = []
    for path in iter_files(source_root):
        digest = sha256_file(path)
        prior = existing.get(digest, {})
        rel = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        metadata = infer_metadata(path)
        record = {
            "id": prior.get("id") or safe_doc_id(path, digest),
            "original_path": prior.get("original_path") or rel,
            "current_path": rel,
            "original_filename": prior.get("original_filename") or path.name,
            "file_type": mimetypes.guess_type(path.name)[0] or path.suffix.lower().lstrip(".") or "unknown",
            "sha256": digest,
            "contains_sensitive_data": True if looks_sensitive(path) else None,
            **metadata,
        }
        records.append(record)
    write_json(output, records)
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventory private source evidence without network calls.")
    parser.add_argument("--source-root", default=str(SOURCES), help="Directory to scan, defaults to private/sources.")
    parser.add_argument("--output", default=str(STATE / "source_inventory.json"), help="Inventory JSON path.")
    args = parser.parse_args()
    records = build_inventory(Path(args.source_root).resolve(), Path(args.output).resolve())
    print(f"Inventoried {len(records)} files -> {Path(args.output)}")


if __name__ == "__main__":
    main()
