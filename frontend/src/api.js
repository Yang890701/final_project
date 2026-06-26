// 兩個後端的 fetch 封裝
const API = import.meta.env.VITE_API_URL || "http://localhost:8000"; // FastAPI
const NODE = import.meta.env.VITE_NODE_URL || "http://localhost:3000"; // Express

async function jget(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
  return r.json();
}
async function jpost(url, body) {
  const r = await fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!r.ok) throw new Error(`${r.status} ${await r.text()}`);
  return r.json();
}

export const detect = (text) => jpost(`${API}/api/detect`, { text });
export const getStats = (from = 2021, to = 2025) =>
  jget(`${API}/api/stats?from=${from}&to=${to}`);
export const getQuestions = (limit = 5) =>
  jget(`${NODE}/api/games/questions?limit=${limit}`);
export const answer = (question_id, choice_idx) =>
  jpost(`${NODE}/api/games/answer`, { question_id, choice_idx });
