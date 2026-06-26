"""資料存取層：有 DATABASE_URL 走 PostgreSQL，否則 fallback 用 db/fixtures.json。

讓整套不需任何 DB 也能 demo（D004 fallback 精神）。
"""
from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path

DATABASE_URL = os.getenv("DATABASE_URL")
_FIXTURES = Path(__file__).resolve().parents[2] / "db" / "fixtures.json"


_INGESTED = Path(__file__).resolve().parents[2] / "db" / "ingested.jsonl"


@lru_cache(maxsize=1)
def _fixtures() -> dict:
    return json.loads(_FIXTURES.read_text(encoding="utf-8"))


def _ingested_examples() -> list[dict]:
    """爬蟲收集的真實資料（無 DB 時的累積檔）。"""
    if not _INGESTED.exists():
        return []
    out = []
    for line in _INGESTED.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return out


@lru_cache(maxsize=1)
def _engine():
    """延遲建立 SQLAlchemy engine；失敗則回 None 觸發 fallback。"""
    if not DATABASE_URL:
        return None
    try:
        from sqlalchemy import create_engine

        url = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1)
        if url.startswith("postgresql://"):
            url = url.replace("postgresql://", "postgresql+psycopg://", 1)
        eng = create_engine(url, pool_pre_ping=True)
        with eng.connect():  # 連線測試
            pass
        return eng
    except Exception as e:  # noqa: BLE001 — DB 不可用時優雅退回 fixtures
        print(f"[data] DB unavailable, falling back to fixtures: {e}")
        return None


def using_db() -> bool:
    return _engine() is not None


def get_scam_examples() -> list[dict]:
    eng = _engine()
    if eng is None:
        return _fixtures()["scam_examples"] + _ingested_examples()
    from sqlalchemy import text

    with eng.connect() as c:
        rows = c.execute(text("SELECT label, scam_type, content FROM scam_examples")).mappings()
        return [dict(r) for r in rows]


def get_stats(year_from: int = 2021, year_to: int = 2025) -> dict:
    eng = _engine()
    if eng is None:
        rows = [r for r in _fixtures()["scam_reports"] if year_from <= r["year"] <= year_to]
    else:
        from sqlalchemy import text

        with eng.connect() as c:
            rows = [
                dict(r)
                for r in c.execute(
                    text(
                        "SELECT year, category, case_count, loss_amount FROM scam_reports "
                        "WHERE year BETWEEN :a AND :b"
                    ),
                    {"a": year_from, "b": year_to},
                ).mappings()
            ]

    by_year: dict[int, dict] = {}
    by_cat: dict[str, dict] = {}
    for r in rows:
        y = by_year.setdefault(r["year"], {"year": r["year"], "case_count": 0, "loss_amount": 0})
        y["case_count"] += r["case_count"]
        y["loss_amount"] += r["loss_amount"]
        c_ = by_cat.setdefault(r["category"], {"category": r["category"], "case_count": 0, "loss_amount": 0})
        c_["case_count"] += r["case_count"]
        c_["loss_amount"] += r["loss_amount"]
    return {
        "by_year": sorted(by_year.values(), key=lambda x: x["year"]),
        "by_category": sorted(by_cat.values(), key=lambda x: -x["case_count"]),
    }
