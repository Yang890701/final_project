# 反詐平台（Scam Detection Platform）

A web platform that detects scams (model + Google Gemini), teaches users via simulation games, and visualises historical scam statistics (2021–2025). 期末專題。
備註(中):偵測詐騙（模型＋Gemini）＋模擬遊戲教學＋詐騙統計視覺化的網站。資料用爬蟲收集入庫。

---

<!-- WAKE-SUMMARY:START — the only part of PROJECT.md auto-injected each session; the full file is on-demand. Keep this block short (~600 tokens). -->
## Wake Summary (always-injected)

- **Project:** 反詐平台 — 偵測詐騙 + 模擬遊戲教學 + 詐騙統計視覺化的網站（期末專題）。
- **Phase:** Phase 1–4 + 6 程式完成並驗證；自訓模型 + 真實官方資料 + Jetson 端 + AWS/render 雙部署設定皆就緒。剩部署執行（5）與繳交物（7）需使用者。
- **Next action:** 使用者執行部署（render 主、AWS 備）+ 填 Gemini key；錄製 1080p 影片、寫心得。
- **Blocker:** 僅外部資源（render/AWS 帳號、Gemini key、Jetson 硬體、錄影）；程式無 blocker。
- **Stack:** Vue + Node + FastAPI(自訓模型+Gemini ensemble) + PostgreSQL；資料接 165 官方開放資料；部署 render+AWS。決策 D001–D008。
- **On-demand (read only when the task needs it):** `ROADMAP.md` (plan + anti-drift) · `DECISIONS.md` · `OPEN_QUESTIONS.md` · full `PROJECT.md` · latest `SESSION_LOG` · `memory/brain-routing-log.md`.
<!-- WAKE-SUMMARY:END -->

## Current Phase

**Phase 0 — 立案 / 環境與決策。** 引擎已接上（D:\weapons agent-os）。計畫書與作業需求已匯入。等兩個架構決策定案（OQ-1 後端框架、OQ-2 部署平台）後即可建 repo 開工。

## Last Checkpoint

| Field | Value |
|---|---|
| Session | 2026-06-26 — 立案→全棧→顧問藍圖品質提升 |
| Completed | Phase 0–4+6 + 顧問藍圖6項(D009)：統計真實化(官方數據+誠信標示)、上線安全硬閘、held-out模型評估(Recall100%/FPR7.7%)、分析升級(ANALYSIS.md)、敘事人文(DEMO_SCRIPT/About/首頁鉤子)、繳交docs(REFLECTION/PROPOSAL_DRAFT/ARCHITECTURE/SUBMISSION_CHECKLIST)。決策D001–D009。 |
| Next action | 使用者：部署render+填key、錄1080p、回填計畫書、釐清團隊(#8) |
| Blocker | 僅外部資源（帳號/錄影/硬體/團隊）；程式無 blocker |

## How To Resume This Project

The SessionStart hook auto-injects **only the lean set**: `BRAIN.md` (the full Dispatcher protocol) + this file's **WAKE-SUMMARY block** + any **active handoff ticket**. You do NOT need to type "read PROJECT.md" or any wake-up command.

Everything else is **on-demand** — read only when the task needs it, in this order:

1. `ROADMAP.md` — phase plan + anti-drift protocol
2. `DECISIONS.md` — architectural choices and why
3. `OPEN_QUESTIONS.md` — pending decisions
4. Latest file in `SESSION_LOG/`
5. `memory/brain-routing-log.md` — the Brain greps this for recall

## Hard Rules (Never Violate)

1. **每個成員都必須貢獻功能程式碼**（作業硬性要求 #8）—— 分工表要留得清楚、可追溯。
2. **部署與資料庫平台一旦定案（OQ-2），全專案統一**，不可前端/後端各自為政。
3. NEVER delete entries marked TREASURE without explicit user consent.
4. ALWAYS log architectural decisions to `DECISIONS.md` before changing direction.
5. 爬蟲只收公開資料、遵守 robots.txt 與來源站條款；詐騙資料不得含個資。

## 來源文件（D:\project）

| 檔案 | 內容 |
|---|---|
| `專題計畫書.docx` | 你們的專題計畫書：研究動機/目的、系統架構、技術棧、功能設計、分工、未來期望。 |
| `S__82812995.jpg` | 課程系統的作業需求說明（9 條）。 |

## 系統架構（照計畫書）

| 元件 | 角色 |
|---|---|
| **Vue.js 前端** | 動態多頁應用（MPA）；使用者互動、發請求給後端、呈現結果。 |
| **Node.js Microservice 後端** | 模擬遊戲的路由邏輯；查詢問答對（Q&A）清單回傳前端。 |
| **Python FastAPI 後端** | 內部：跑詐騙偵測模型 + 詐騙統計（預測 / 資料視覺化）。外部：呼叫 Google Gemini 並處理回應。 |
| **PostgreSQL 資料庫** | 模型訓練資料、模擬遊戲問答字典、2021–2025 歷史詐騙資料。 |
| **部署** | **render**（D003）：前端 Static Site + Node/FastAPI 各一 Web Service + render PostgreSQL，以 `render.yaml` 管理。AWS 原案封存。 |

## 功能設計

1. **詐騙偵測** — 輸入訊息/網址，模型 + Gemini 判斷是否為詐騙並解釋。
2. **模擬遊戲** — 問答互動，教使用者辨識詐騙手法。
3. **詐騙統計** — 2021–2025 歷史資料的視覺化（趨勢、類型分布等）。
4. **資料收集** — 動態網頁爬蟲（Selenium / Playwright）收集詐騙案例入庫。

## 作業硬性需求對照（圖片 9 條）

1. GitHub repo + 專題計畫書 + 專案架構 ✅（架構已定，repo 待建）
2. 資料庫用 render 的 PostgreSQL → **OQ-2**
3. 爬蟲收動態網頁資料入庫 ✅ 已規劃
4. 資料分析（π型人）+ 部署在 render → **OQ-2**
5. 繳交：GitHub 連結、1080p mp4 錄影、動機、講解（PM 表達力）、程式碼、人文氣息、心得、說故事/賣產品（系上有錄影設備）
6. AI 是能力放大器；作品集未來可落地
7. 加分：串 Nvidia Jetson Orin Nano + 攝像頭（軟硬結合）
8. **每個成員都要貢獻功能程式碼**（→ Hard Rule #1）
9. 想到再補充

## File Map (D020 engine/data split)

### Data (this project — lives in `.claude/agent-os/`)

| Path | Purpose |
|---|---|
| `PROJECT.md` | This file. Snapshot + wake-summary. |
| `DECISIONS.md` | Architectural decisions D001-DNNN with rationale. |
| `OPEN_QUESTIONS.md` | Pending decisions requiring user input. |
| `ROADMAP.md` | Phase plan + anti-drift protocol. |
| `SESSION_LOG/*.md` | Per-session work logs (YAML frontmatter required). |
| `memory/brain-handoff.md` | Live cross-session handoff ticket. |
| `memory/brain-routing-log.md` | Append-only routing log; the Brain recalls from it. |
| `memory/TREASURE/*.md` | Project-specific permanent memories (never auto-deleted). |

### Engine (shared, at `D:/weapons/agent-os/`)

**`BRAIN.md`** (the Dispatcher protocol), agents, hooks, CLIs, slash commands all live in the engine, auto-discovered via `~/.claude/` mirrors / injected by the SessionStart hook. Do not manage engine files from inside this project.

## Token Budget Note

Keep the Wake Summary + Last Checkpoint tight (~600 tokens). Other files load on demand.
