# Architectural Decisions

> Decision log for this project. Each entry: ID, date, decision, rationale.
> 備註(中):重大決策歷史紀錄,每筆都帶日期跟理由。

---

## D001 — 採用專題計畫書架構為基線，作業需求為硬性約束（2026-06-26）

- **Decision**: 以 `D:\project\專題計畫書.docx` 的系統架構（Vue 前端 / 後端 / PostgreSQL / Gemini / 四大功能）為開發基線；作業說明圖的 9 條需求視為硬性驗收約束。兩份在「要做什麼」上對齊，僅在兩個平台選擇上衝突 → 拆成 OQ-1（後端框架）與 OQ-2（部署平台）待決。
- **Rationale**: 計畫書內容比作業最低要求更完整（多了 Gemini、模擬遊戲、統計視覺化），這些作業未禁止、反而是加分；不需推翻計畫書，只需把 Flask/render 兩個字面要求對齊。
- **Consequence**: 建立 7 階段 ROADMAP；後端框架與部署平台暫掛起，不阻塞 Phase 0 文件工作，但阻塞 repo 骨架定型。

---

## D002 — 後端採 Node.js + Python FastAPI 雙後端（2026-06-26，結 OQ-1）

- **Decision**: 照計畫書，後端分兩個服務：**Node.js microservice**（模擬遊戲路由 + 問答對查詢）+ **Python FastAPI**（詐騙偵測模型、詐騙統計、Google Gemini 串接）。
- **Rationale**: 功能切分清楚；FastAPI 適合 ML/Gemini，Node 適合輕量遊戲路由；與計畫書架構一致。作業字面寫 Flask，但作業未禁止其他框架，且本案功能比最低要求更完整。
- **Consequence**: repo 採 monorepo，含 `backend-node/` 與 `backend-api/` 兩個後端目錄；全員需協調 JS 與 Python 兩種語言的分工（Hard Rule #1）。render 上以兩個獨立 service 部署。

---

## D003 — 部署平台採 render（2026-06-26，結 OQ-2）

- **Decision**: 前端、兩個後端、PostgreSQL 全部部署於 **render**；資料庫用 render 的 PostgreSQL。
- **Rationale**: 直接滿足作業 #2/#4 評分要求、免費額度足夠專題、設定簡單。計畫書的 AWS 架構封存於 ROADMAP「Parked Ideas」，未來作品集落地再啟用。
- **Consequence**: Phase 1 的 DB 連線指向 render PostgreSQL；Phase 5 以 render（Static Site + 2× Web Service + PostgreSQL）部署；用 `render.yaml` 管理服務。

---

## D004 — 詐騙偵測採「Gemini 一發 + 輕量 RAG」，不 fine-tune（2026-06-26，workflow-decomposer 建議）

- **Decision**: 偵測核心用 Gemini 單次 prompt 判定（是否詐騙 + 信心 + 理由）；以 PostgreSQL 歷史案例做 RAG grounding。遊戲批改與統計走 SQL/查表（非 LLM）。不微調、不 multi-agent。
- **Rationale**: workflow-decomposer 拆解結論——詐騙話術易變、無標註訓練集、專題情境 → 微調是最脆最貴的一層；一發是 MVP，RAG 提升可解釋性與信心校準；deterministic 任務走規則零幻覺。
- **Consequence**: schema 必須含「話術原文/特徵文本」欄位供 RAG 向量化（不能只存統計數字）；先做純一發原型，用失敗案例決定是否加 RAG；偵測端點留 Gemini-key 環境變數 + 無 key 時的規則化 fallback，確保本機可跑。
