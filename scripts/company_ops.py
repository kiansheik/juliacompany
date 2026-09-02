from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PRIVATE = ROOT / "private"
STATE = PRIVATE / "state"
GENERATED = PRIVATE / "generated"
SOURCES = PRIVATE / "sources"


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def money(value: str | int | Decimal | None) -> Decimal | None:
    if value is None:
        return None
    if isinstance(value, Decimal):
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    text = str(value).strip().replace("R$", "").replace(" ", "")
    if "," in text:
        text = text.replace(".", "").replace(",", ".")
    try:
        return Decimal(text).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError):
        return None


def brl(value: str | int | Decimal | None) -> str:
    amount = money(value)
    if amount is None:
        return "unknown"
    whole, cents = f"{amount:.2f}".split(".")
    groups: list[str] = []
    while whole:
        groups.append(whole[-3:])
        whole = whole[:-3]
    return "R$ " + ".".join(reversed(groups)) + "," + cents


def period_from_date(date_text: str | None) -> str | None:
    if not date_text or len(date_text) < 7:
        return None
    return date_text[:7]


def receipt_period(receipt: dict[str, Any]) -> str | None:
    return period_from_date(receipt.get("date")) or receipt.get("received_period")


def text_at(root: ET.Element, tag: str) -> str | None:
    for elem in root.iter():
        if elem.tag.split("}")[-1] == tag:
            text = (elem.text or "").strip()
            if text:
                return text
    return None


def all_text(root: ET.Element, tag: str) -> list[str]:
    values = []
    for elem in root.iter():
        if elem.tag.split("}")[-1] == tag:
            text = (elem.text or "").strip()
            if text:
                values.append(text)
    return values


def parse_xml(path: Path) -> ET.Element | None:
    try:
        return ET.fromstring(path.read_bytes())
    except ET.ParseError:
        return None


def looks_sensitive(path: Path) -> bool:
    low = str(path).lower()
    sensitive_words = [
        "pass",
        "rg",
        "login",
        "senha",
        "recibo",
        "comprovante",
        "contrato",
        "cnpj",
        "qsa",
        "esocial",
        "pgdas",
        "nfse",
        "nfs-e",
        "prolabore",
        "lucros",
        "darf",
        "das",
    ]
    return path.suffix.lower() in {".pdf", ".xml", ".jpg", ".jpeg"} or any(word in low for word in sensitive_words)


def classify_path(path: Path) -> tuple[str, str | None, str]:
    low = str(path).lower()
    if "nfs-e" in low or "nfse" in low:
        return "nfse", "municipal_nfse", "invoice"
    if "pgdas" in low:
        if "das" in low and "recibo" not in low:
            return "simples_das", "pgdas_d", "tax_payment_or_bill"
        return "pgdas_receipt", "pgdas_d", "declaration_receipt"
    if "esocial" in low or "prolabore" in low:
        return "esocial_or_payroll", "esocial", "payroll_evidence"
    if "lucros" in low:
        return "profit_distribution", "bank_or_internal_note", "distribution_evidence"
    if "login" in low or "pass" in low:
        return "credential_note", "portal", "secret"
    if any(word in low for word in ["contrato", "redesim", "qsa", "constit", "cadastro", "regime", "simples", "cnpj", "deferimento"]):
        return "company_registration", "registration_portal", "registration_evidence"
    return "unknown", None, "source"


@dataclass(frozen=True)
class SourceRef:
    inventory_id: str
    path: str


def source_ref_by_filename(inventory: list[dict[str, Any]], name_fragment: str) -> SourceRef | None:
    for item in inventory:
        if name_fragment in item.get("current_path", "") or name_fragment in item.get("original_path", ""):
            return SourceRef(item["id"], item.get("current_path") or item.get("original_path"))
    return None
