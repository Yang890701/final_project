"""詐騙偵測 API：偵測 / 統計 / Gemini（D004）。"""
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from .data import get_stats, using_db
from .detect import detect

app = FastAPI(title="Scam Detection API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # demo 用全開；上線改成前端網域
    allow_methods=["*"],
    allow_headers=["*"],
)


class DetectIn(BaseModel):
    text: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "backend-api", "db": using_db()}


@app.post("/api/detect")
def api_detect(body: DetectIn):
    return detect(body.text)


@app.get("/api/stats")
def api_stats(year_from: int = Query(2021, alias="from"), to: int = 2025):
    return get_stats(year_from, to)
