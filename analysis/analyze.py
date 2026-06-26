"""資料分析：對 2021–2025 詐騙資料做趨勢/類型分析並輸出圖表。

資料來源：有 DATABASE_URL 讀 PostgreSQL，否則讀 db/fixtures.json。
輸出：analysis/output/*.png + 印出洞察。
    python analysis/analyze.py
"""
from __future__ import annotations

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "output"


def load_reports() -> "list[dict]":
    url = os.getenv("DATABASE_URL")
    if url:
        from sqlalchemy import create_engine, text

        u = url.replace("postgres://", "postgresql+psycopg://", 1).replace(
            "postgresql://", "postgresql+psycopg://", 1
        )
        eng = create_engine(u)
        with eng.connect() as c:
            return [
                dict(r)
                for r in c.execute(
                    text("SELECT year, category, case_count, loss_amount FROM scam_reports")
                ).mappings()
            ]
    return json.loads((ROOT / "db" / "fixtures.json").read_text(encoding="utf-8"))["scam_reports"]


def main() -> None:
    import pandas as pd

    df = pd.DataFrame(load_reports())
    OUT.mkdir(exist_ok=True)

    by_year = df.groupby("year")["case_count"].sum()
    by_cat = df.groupby("category")["case_count"].sum().sort_values(ascending=False)
    loss_by_year = df.groupby("year")["loss_amount"].sum()

    print("=== 年度案件數 ===")
    print(by_year.to_string())
    print("\n=== 類型占比 ===")
    print(by_cat.to_string())

    growth = (by_year.iloc[-1] / by_year.iloc[0] - 1) * 100
    top_cat = by_cat.index[0]
    print(f"\n洞察：{by_year.index[0]}→{by_year.index[-1]} 案件成長 {growth:.0f}%；"
          f"最大宗為「{top_cat}」（{by_cat.iloc[0]:,} 件）。")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei", "DejaVu Sans"]
        plt.rcParams["axes.unicode_minus"] = False

        ax = by_year.plot(kind="bar", title="年度詐騙案件數 2021-2025", color="#0f3460")
        ax.figure.tight_layout(); ax.figure.savefig(OUT / "by_year.png"); plt.close()

        ax = by_cat.plot(kind="barh", title="各類型詐騙案件數", color="#c0392b")
        ax.figure.tight_layout(); ax.figure.savefig(OUT / "by_category.png"); plt.close()

        ax = loss_by_year.div(1e8).plot(kind="line", marker="o", title="年度財損（億元）", color="#27ae60")
        ax.figure.tight_layout(); ax.figure.savefig(OUT / "loss_by_year.png"); plt.close()
        print(f"\n圖表已輸出至 {OUT}")
    except ImportError:
        print("\n（未安裝 matplotlib，略過圖表；pip install -r analysis/requirements.txt 後可產圖）")


if __name__ == "__main__":
    main()
