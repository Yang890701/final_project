"""詐騙偵測 API：偵測模型 / 統計 / Google Gemini。"""
from fastapi import FastAPI

app = FastAPI(title="Scam Detection API")


@app.get("/health")
def health():
    return {"status": "ok", "service": "backend-api"}


# TODO Phase 2:
#   POST /api/detect  — 模型 + Gemini 判斷詐騙
#   GET  /api/stats   — 2021–2025 詐騙統計
