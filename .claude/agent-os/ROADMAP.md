# ROADMAP

> Multi-phase build plan for this project. PROJECT.md `Next action` always points at the first non-completed item below.
> Drift = misalignment between PROJECT.md Next action and the current ROADMAP item.
> 備註(中):計畫表。PROJECT.md 的 Next action 永遠指這裡第一個未完成項目;對不上就是偏移。

---

## Anti-drift Protocol

1. **Session start** — SessionStart hook injects PROJECT.md + this file. Verify PROJECT.md `Next action` matches the first non-completed item below. If mismatch → stop and ask user.
2. **In session** — execute items from the current phase only. Off-roadmap requests trigger "this isn't on the roadmap, OK to add/swap?" before doing.
3. **Session end** — refresh PROJECT.md `Last Checkpoint` + `Next action` to point at the next pending item.
4. **Architecture-level changes** — must be logged in DECISIONS.md before editing this file.

備註(中):每次 session 開頭照這個流程對齊,沒對齊就停下來問。

---

## Phase Status

| Phase | Description | Status | Trigger |
|---|---|---|---|
| 0 | 立案 / 環境與決策 | 🟡 In progress（OQ-1/OQ-2 已定，建骨架中） | — |
| 1 | 資料層：爬蟲 + PostgreSQL schema | ⏳ Pending | Phase 0 完成 |
| 2 | 後端：偵測模型 + API + Gemini + 統計 | ⏳ Pending | OQ-1 定案 + Phase 1 |
| 3 | 前端：Vue.js MPA（偵測 / 遊戲 / 統計 / Gemini） | ⏳ Pending | Phase 2 API 可用 |
| 4 | 資料分析與視覺化 | ⏳ Pending | Phase 1 資料就緒 |
| 5 | 部署（render 或 AWS，見 OQ-2） | ⏳ Pending | Phase 2+3 可跑 |
| 6 | 加分：Nvidia Jetson Orin Nano + 攝像頭 | ⏳ Pending | 主功能完成且行有餘力 |
| 7 | 繳交：1080p 錄影 + 心得 + 收尾 | ⏳ Pending | 全功能上線 |

---

## Phase Detail

### Phase 0 — 立案 / 環境與決策
- **Goal**: 把專案規劃、架構、決策、分工定下來，環境就緒可開工。
- **Deliverables**: PROJECT/ROADMAP/DECISIONS/OPEN_QUESTIONS（本批）；OQ-1（後端框架）+ OQ-2（部署平台）定案；GitHub repo 建立 + 專案骨架（monorepo：`frontend/` `backend/` `crawler/` `analysis/` `docs/`）；成員分工表。
- **Completion**: repo 可 clone、骨架可跑 hello-world、分工表上每人都有認領項目。
- 備註(中):決策定案 + 建 repo + 骨架 + 分工。

### Phase 1 — 資料層
- **Goal**: 用爬蟲收集 2021–2025 詐騙資料入 PostgreSQL；建模擬遊戲問答字典。
- **Deliverables**: Selenium/Playwright 爬蟲；PostgreSQL schema（訓練資料 / Q&A 字典 / 歷史詐騙資料）；種子資料匯入腳本。
- **Completion**: DB 有可查詢的真實詐騙資料；爬蟲可重複執行且遵守 robots.txt。
- 備註(中):爬蟲 + 資料表 + 入庫。

### Phase 2 — 後端
- **Goal**: 詐騙偵測模型 + 對外 API + Gemini 串接 + 統計端點。
- **Deliverables**: 偵測模型（訓練 + 推論）；REST API（框架見 OQ-1）；Gemini 整合；統計查詢端點；模擬遊戲問答 API。
- **Completion**: 可用 API 對一段訊息回傳詐騙判斷 + 解釋；統計端點回傳可繪圖資料。
- 備註(中):模型 + API + Gemini + 統計。

### Phase 3 — 前端
- **Goal**: Vue.js MPA 串起全部功能。
- **Deliverables**: 偵測頁、模擬遊戲頁、統計視覺化頁、Gemini 問答頁；RWD。
- **Completion**: 使用者可在瀏覽器跑完整流程。
- 備註(中):Vue 前端串四大功能。

### Phase 4 — 資料分析與視覺化
- **Goal**: 對歷史詐騙資料做分析，產出洞察與圖表（呼應作業「資料分析 / π型人」）。
- **Deliverables**: 分析 notebook/腳本；趨勢/類型/地區等視覺化；前端統計頁的資料來源。
- **Completion**: 有可解讀的分析結論 + 圖表上站。
- 備註(中):分析 + 圖表。

### Phase 5 — 部署
- **Goal**: 上線。平台依 OQ-2 定案（作業要求 render；計畫書寫 AWS）。
- **Deliverables**: 前端 + 後端 + DB 部署；環境變數/密鑰管理；CI（選配）。
- **Completion**: 公開可訪問的 URL，功能正常。
- 備註(中):部署上線。

### Phase 6 — 加分（軟硬結合）
- **Goal**: 串 Nvidia Jetson Orin Nano + 攝像頭（作業加分項 #7）。
- **Deliverables**: Jetson 端推論 + 攝像頭擷取 + 與平台串接的 demo。
- **Completion**: 可現場展示的軟硬整合 demo。
- 備註(中):Jetson + 攝像頭 demo（行有餘力才做）。

### Phase 7 — 繳交
- **Goal**: 產出繳交物。
- **Deliverables**: 1080p mp4 錄影（動機 + 講解 + 說故事/賣產品）；心得（人文氣息）；README + 專題計畫書定稿；GitHub 連結。
- **Completion**: 全部繳交物備齊、連結可開。
- 備註(中):錄影 + 心得 + 收尾。

---

## Parked Ideas (revisit later)

- AWS 完整架構（計畫書原案）：若 OQ-2 選 render，AWS 版本先封存，未來作品集落地時再啟用。

---

## Change Log

| Date | Change | Reason | Decision Ref |
|---|---|---|---|
| 2026-06-26 | 建立 7 階段 roadmap | 依專題計畫書 + 作業需求立案 | D001 |
| 2026-06-26 | 後端定 Node+FastAPI、部署定 render | 結 OQ-1 / OQ-2 | D002 / D003 |
