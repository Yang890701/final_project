<script setup>
import { RouterLink, RouterView } from "vue-router";

const tabs = [
  { to: "/", label: "首頁", icon: "🏠" },
  { to: "/detect", label: "詐騙偵測", icon: "🔍" },
  { to: "/game", label: "模擬遊戲", icon: "🎮" },
  { to: "/stats", label: "詐騙統計", icon: "📊" },
  { to: "/about", label: "關於我們", icon: "💙" },
];
</script>

<template>
  <div class="app">
    <header class="topbar">
      <div class="brand">
        <span class="logo">🛡️</span>
        <div>
          <div class="title">反詐平台</div>
          <div class="subtitle">偵測 · 教學 · 數據，三招遠離詐騙</div>
        </div>
      </div>
    </header>

    <nav class="tabs">
      <RouterLink
        v-for="t in tabs"
        :key="t.to"
        :to="t.to"
        class="tab"
        active-class="tab-active"
      >
        <span class="tab-icon">{{ t.icon }}</span>{{ t.label }}
      </RouterLink>
    </nav>

    <main class="content">
      <RouterView />
    </main>

    <footer class="footer">期末專題 · 詐騙偵測（自訓模型 + Gemini）／模擬遊戲／詐騙統計視覺化</footer>
  </div>
</template>

<style>
:root {
  --bg: #f4f6fb;
  --card: #ffffff;
  --ink: #1f2430;
  --muted: #6b7280;
  --brand: #1e4fd6;
  --brand-dark: #16213e;
  --danger: #d83a3a;
  --ok: #1f9d57;
  --warn: #e08a00;
  --line: #e6e9f0;
  --radius: 14px;
}
* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  font-family: "Microsoft JhengHei", "PingFang TC", "Segoe UI", system-ui, sans-serif;
  background: var(--bg);
  color: var(--ink);
  font-size: 17px;
  line-height: 1.7;
}
.app { min-height: 100vh; display: flex; flex-direction: column; }

/* 頂部 */
.topbar {
  background: linear-gradient(120deg, #16213e, #1e4fd6);
  color: #fff;
  padding: 1.1rem 1.25rem;
}
.brand { display: flex; align-items: center; gap: .85rem; max-width: 960px; margin: 0 auto; width: 100%; }
.logo { font-size: 2.2rem; }
.title { font-size: 1.5rem; font-weight: 800; letter-spacing: 1px; }
.subtitle { font-size: .95rem; opacity: .85; }

/* 頁簽 */
.tabs {
  display: flex;
  gap: .4rem;
  background: var(--brand-dark);
  padding: 0 1rem;
  justify-content: center;
  flex-wrap: wrap;
}
.tab {
  color: #c7d2fe;
  text-decoration: none;
  padding: .8rem 1.1rem;
  font-weight: 700;
  border-bottom: 3px solid transparent;
  transition: all .15s;
  white-space: nowrap;
}
.tab:hover { color: #fff; background: rgba(255,255,255,.08); }
.tab-active { color: #fff; border-bottom-color: #ffd166; background: rgba(255,255,255,.10); }
.tab-icon { margin-right: .35rem; }

/* 內容 */
.content { flex: 1; width: 100%; max-width: 820px; margin: 1.6rem auto; padding: 0 1rem; }
.footer { text-align: center; color: var(--muted); padding: 2rem 1rem; font-size: .85rem; }

/* 共用元件 */
.card {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 1.4rem 1.5rem;
  box-shadow: 0 4px 16px rgba(20,30,60,.06);
  margin-bottom: 1.2rem;
}
.card h2 { margin: 0 0 .4rem; font-size: 1.35rem; }
.card h3 { margin: 0 0 .6rem; }
.muted { color: var(--muted); }
.btn {
  cursor: pointer; border: none; border-radius: 10px;
  padding: .75rem 1.4rem; background: var(--brand); color: #fff;
  font-size: 1.05rem; font-weight: 700; transition: filter .15s;
}
.btn:hover:not(:disabled) { filter: brightness(1.08); }
.btn:disabled { opacity: .5; cursor: default; }
textarea {
  width: 100%; min-height: 110px; padding: .8rem 1rem;
  border: 1.5px solid var(--line); border-radius: 10px;
  font-size: 1.05rem; font-family: inherit; resize: vertical;
}
textarea:focus { outline: none; border-color: var(--brand); }
.chip {
  display: inline-block; cursor: pointer; user-select: none;
  background: #eef2ff; color: #3147b8; border: 1px solid #d9e0ff;
  border-radius: 999px; padding: .35rem .8rem; margin: .25rem .3rem 0 0;
  font-size: .9rem;
}
.chip:hover { background: #e0e7ff; }
</style>
