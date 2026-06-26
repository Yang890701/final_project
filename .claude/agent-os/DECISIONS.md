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

---

## D005 — 部署同時提供 render + AWS（2026-06-26，使用者：兩個都做）

- **Decision**: 主交付以 **render**（對齊作業評分，`render.yaml`）；另附完整 **AWS** 部署設定（Dockerfile + Elastic Beanstalk / Amplify + RDS 說明）作為「計畫書完整實現」佐證。
- **Rationale**: 作業 #2/#4 硬性要求 render，但計畫書原案是 AWS；使用者要兩邊都交代得過去。
- **Consequence**: 新增 `deploy/aws/` 與部署指南；維護成本上升但兩套並存，render 為預設、AWS 為備援/展示。

---

## D006 — 偵測改「訓練模型 + Gemini 並用」（2026-06-26，使用者：對齊計畫書）

- **Decision**: FastAPI 同時跑「自訓詐騙文字分類器（TF-IDF + LogisticRegression）」+ Gemini。模型負責分類與信心，Gemini 負責理由解釋與第二意見，RAG 提供 grounding。三者 ensemble。
- **Rationale**: 計畫書明寫「FastAPI hosts the scam detection model」，自訓模型最對齊字面、也增專題深度；保留 Gemini 兼顧解釋力。修正 D004 的「不訓練模型」。
- **Consequence**: 新增 `backend-api/model/`（train.py + 推論層）；requirements 增 scikit-learn/joblib；偵測 engine 標示為 `model+gemini+rag` / `model+rag` / `rule-fallback`（依可用資源降級）。

---

## D007 — 爬蟲鎖定台灣公開反詐來源（2026-06-26）

- **Decision**: 統計資料優先用政府開放資料（data.gov.tw 165 反詐騙統計，合法可重用）；詐騙話術案例爬「165 全民防騙網」等公開宣導頁（先檢查 robots.txt 與條款）。
- **Rationale**: 合法、可重用、貼近真實；同時滿足作業 #3「爬蟲」與資料真實性。
- **Consequence**: 建對應 source adapter；尊重 robots（D 基礎建設已做）；統計類來源以開放資料 CSV/JSON 為主、話術類以動態頁爬蟲為主。

---

## D008 — 先寫 Jetson Orin Nano 邊緣端程式（2026-06-26，加分 #7）

- **Decision**: 新增 `edge-jetson/`：攝像頭擷取 → 端側推論（OCR/影像或文字模型）→ 呼叫平台 `/api/detect`。先寫程式，待硬體再實跑。
- **Rationale**: 作業加分項；軟硬結合展示。先備好程式不阻塞主線。
- **Consequence**: 程式可在無 Jetson 時以 mock 攝像頭驗證流程；實機需 `playwright`/`jetson` 相依與硬體。

---

## D009 — 顧問藍圖驅動的品質提升（2026-06-26，多顧問 Workflow）

- **Decision**: 依 multi-consultant workflow（eval-designer / 產品評分 / permission-architect + 總顧問收斂）執行 6 大改善：①統計改真實官方數據+標出處（修「示意值卻標官方」的誠信地雷）②上線安全硬閘（CORS/限流/Gemini cap/出境揭露/detections 去個資）③held-out 模型評估（停用訓練集準確率，Recall 100%/FPR 7.7%）④資料分析升級（YoY+真實樣本文字分析→ANALYSIS.md）⑤敘事與人文（DEMO_SCRIPT/首頁鉤子/About 使命頁/UI 限制標註）⑥繳交完整性（REFLECTION/PROPOSAL_DRAFT/ARCHITECTURE/SUBMISSION_CHECKLIST）。
- **Rationale**: 顧問群一致指出技術骨架已成形，缺的是「可信度」與「故事」；最大單點風險為統計誠信。
- **Consequence**: 偵測 ensemble 改模型主導（規則僅強烈命中才加分）；新增 testset/evaluate；多份 docs 成為繳交物來源。剩部署執行（需帳號）與錄影/團隊釐清（需使用者）。
