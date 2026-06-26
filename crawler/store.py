"""入庫：有 DATABASE_URL 寫 PostgreSQL，否則寫 output/scam_examples.jsonl。"""
from __future__ import annotations

import json
import os
from pathlib import Path

DATABASE_URL = os.getenv("DATABASE_URL")
OUT = Path(__file__).resolve().parent / "output"


def save_examples(rows: list[dict]) -> int:
    """rows: [{label, scam_type, content, features, source}]"""
    if not rows:
        return 0
    if not DATABASE_URL:
        OUT.mkdir(exist_ok=True)
        f = OUT / "scam_examples.jsonl"
        with f.open("a", encoding="utf-8") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"[store] no DB → appended {len(rows)} rows to {f}")
        return len(rows)

    from sqlalchemy import create_engine, text

    url = DATABASE_URL.replace("postgres://", "postgresql+psycopg://", 1).replace(
        "postgresql://", "postgresql+psycopg://", 1
    )
    eng = create_engine(url)
    with eng.begin() as c:
        for r in rows:
            c.execute(
                text(
                    "INSERT INTO scam_examples (label, scam_type, content, features, source) "
                    "VALUES (:label, :scam_type, :content, :features, :source)"
                ),
                {
                    "label": r.get("label", "scam"),
                    "scam_type": r.get("scam_type"),
                    "content": r["content"],
                    "features": r.get("features"),
                    "source": r.get("source", "crawler"),
                },
            )
    print(f"[store] inserted {len(rows)} rows into PostgreSQL")
    return len(rows)
