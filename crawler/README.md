# crawler — 動態網頁爬蟲

收集 2021–2025 詐騙案例資料 → 寫入 PostgreSQL（作業需求 #3）。

## 技術
Python + Selenium / Playwright（動態網頁）+ psycopg。

## 啟動
```bash
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium     # 若用 Playwright
python -m crawler.run
```

## 規範（Hard Rule #5）
- 只收公開資料，遵守 `robots.txt` 與來源站條款。
- 詐騙資料不得含個資。
- 可重複執行、有去重。

## 資料流
來源站 → 解析 → 正規化 → 寫入 `scam-db`（見 `analysis/` 與 `backend-api/` 共用 schema）。
