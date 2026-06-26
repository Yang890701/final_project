// 模擬遊戲路由 + 問答對查詢 microservice
// TODO: 接 PostgreSQL（pg），實作 /api/games/* 端點。
import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

app.get("/health", (_req, res) => res.json({ status: "ok", service: "backend-node" }));

// TODO Phase 2: GET /api/games/questions, POST /api/games/answer

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`backend-node listening on ${port}`));
