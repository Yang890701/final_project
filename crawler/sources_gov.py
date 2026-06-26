"""政府開放資料來源（D007）。

警政署 165「詐騙闢謠專區」開放資料（政府資料開放授權條款-第1版，免費）。
資料集：https://data.gov.tw/dataset/38262
欄位：編號 / 標題 / 發佈時間 / 發佈內容

這些是官方對真實詐騙手法的描述/闢謠，作為偵測模型的「詐騙樣態」參考與 RAG grounding。
（屬開放資料下載，非網頁爬蟲；動態頁爬蟲見 sources.py 的 Playwright 路徑。）
"""
from __future__ import annotations

import csv
import io
import urllib.request

from .base import scrub_pii

# 165 詐騙闢謠專區 CSV
GOV_DEBUNK_CSV = (
    "https://opdadm.moi.gov.tw/api/v1/no-auth/resource/api/dataset/"
    "4F4DF9A5-DF4C-4EE8-A50D-869347D38D9E/resource/"
    "0180F4A7-335D-4D69-A8D8-16E3EDEE617D/download"
)
UA = "ScamPlatformBot/0.1 (academic project)"


def _classify_type(title: str) -> str | None:
    """從標題粗略歸類詐騙類型。"""
    rules = [
        ("假投資", ["投資", "飆股", "帶單", "虛擬貨幣", "博弈"]),
        ("假網拍", ["購物", "網拍", "賣家", "拍賣", "電商"]),
        ("假冒公務機關", ["檢警", "地檢", "公務", "健保", "監理", "稅"]),
        ("解除分期付款", ["分期", "ATM", "解除"]),
        ("假交友", ["交友", "愛情", "感情"]),
        ("釣魚簡訊", ["簡訊", "連結", "包裹", "物流", "釣魚", "個資"]),
    ]
    for label, kws in rules:
        if any(k in title for k in kws):
            return label
    return None


def fetch_gov_debunk(limit: int | None = None) -> list[dict]:
    """下載並解析 165 闢謠開放資料，回傳標準化 scam_examples 列。"""
    req = urllib.request.Request(GOV_DEBUNK_CSV, headers={"User-Agent": UA})
    raw = urllib.request.urlopen(req, timeout=60).read()
    text = raw.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))

    rows: list[dict] = []
    for i, rec in enumerate(reader):
        if limit and i >= limit:
            break
        title = (rec.get("標題") or "").strip()
        body = (rec.get("發佈內容") or "").strip()
        content = scrub_pii(f"{title}：{body}" if title else body)
        if len(content) < 10:
            continue
        rows.append(
            {
                "label": "scam",  # 官方詐騙樣態描述，作為詐騙參考文本
                "scam_type": _classify_type(title),
                "content": content,
                "features": "官方闢謠/詐騙手法描述",
                "source": "data.gov.tw/dataset/38262 (165闢謠)",
            }
        )
    return rows
