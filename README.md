# 反詐平台（Scam Detection Platform）

偵測詐騙（模型 + Google Gemini）＋模擬遊戲教學＋詐騙統計視覺化（2021–2025）的網站。期末專題。

## 系統架構

```
[ Vue.js 前端 (MPA) ]
        │
        ├──────────────► [ Node.js Microservice ]  模擬遊戲路由 / 問答對查詢
        │
        └──────────────► [ Python FastAPI ]        詐騙偵測模型 / 統計 / Google Gemini
                                   │
                          [ PostgreSQL ]            訓練資料 / 問答字典 / 歷史詐騙資料 2021–2025
```

全部部署於 **render**（前端 Static Site + Node/FastAPI 各一 Web Service + render PostgreSQL）。

## 目錄結構（monorepo）

| 目錄 | 內容 | 技術 |
|---|---|---|
| `frontend/` | Vue.js 多頁前端 | Vue 3 + Vite |
| `backend-node/` | 模擬遊戲路由 + 問答對 API | Node.js + Express |
| `backend-api/` | 偵測模型 / 統計 / Gemini | Python + FastAPI |
| `crawler/` | 動態網頁爬蟲收集詐騙資料 | Python + Selenium/Playwright |
| `analysis/` | 資料分析與視覺化 | Python (pandas/matplotlib) |
| `docs/` | 專題計畫書、架構圖、繳交物 | — |

## 功能

1. **詐騙偵測** — 輸入訊息/網址，模型 + Gemini 判斷並解釋。
2. **模擬遊戲** — 問答互動，教辨識詐騙手法。
3. **詐騙統計** — 2021–2025 歷史資料視覺化。
4. **資料收集** — 爬蟲收集詐騙案例入庫。

## 開發

各子專案的啟動方式見各自的 `README.md`。本專案以 agent-os 管理（`.claude/agent-os/`）—— 規劃、決策、分工見該目錄。

## 文件

- 專題計畫書：`docs/`（原始檔 `專題計畫書.docx`）
- 架構決策：`.claude/agent-os/DECISIONS.md`
- 開發計畫：`.claude/agent-os/ROADMAP.md`
- 成員分工：`TEAM.md`
