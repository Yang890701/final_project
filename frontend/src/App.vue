<script setup>
import { RouterLink, RouterView } from "vue-router";
import Icon from "./components/Icon.vue";

const tabs = [
  { to: "/", label: "首頁", icon: "home" },
  { to: "/detect", label: "偵測中心", icon: "detect" },
  { to: "/chat", label: "AI問答", icon: "chat" },
  { to: "/game", label: "防詐練習", icon: "game" },
  { to: "/intel", label: "詐騙情報", icon: "intel" },
  { to: "/help", label: "我被騙了", icon: "help" },
  { to: "/about", label: "關於我們", icon: "heart" },
];
</script>

<template>
  <div class="app">
    <header class="topbar">
      <RouterLink to="/" class="brand">
        <!-- 品牌標誌：盾牌+心，與插畫同一套線條語言 -->
        <svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3Z" fill="rgba(255,255,255,.15)" />
          <path d="M12 16s-3.2-2-3.2-4.2A1.8 1.8 0 0 1 12 10.4a1.8 1.8 0 0 1 3.2 1.4C15.2 14 12 16 12 16Z" fill="#fff" stroke="#fff" />
        </svg>
        <div>
          <div class="title">安心盾 <span class="tw">·防詐夥伴</span></div>
          <div class="subtitle">在按下匯款前，先讓我陪你看一眼</div>
        </div>
      </RouterLink>
    </header>

    <nav class="tabs">
      <div class="tabs-inner">
        <RouterLink v-for="t in tabs" :key="t.to" :to="t.to" class="tab" active-class="on">
          <Icon :name="t.icon" :size="19" /><span>{{ t.label }}</span>
        </RouterLink>
      </div>
    </nav>

    <main class="content"><RouterView /></main>

    <footer class="footer">
      <p>安心盾 · 反詐夥伴 — 偵測、學習、求助，陪你遠離詐騙</p>
      <p class="fnote">資料來源：內政部警政署 165 反詐騙開放資料　·　遇詐請撥 165</p>
    </footer>
  </div>
</template>

<style>
:root {
  /* 暖人文色票（rubric #2：暖橘 × 米白，禁藍色冷調）*/
  --cream: #fbf6ee;
  --cream-2: #fffaf3;
  --card: #ffffff;
  --ink: #3a2c20;          /* 暖棕文字 */
  --ink-soft: #7a6a5b;
  --line: #efe3d3;
  --brand: #e8743b;        /* 暖橘 */
  --brand-deep: #c85a28;
  --brand-soft: #fde9dc;
  --accent: #2f8f76;       /* 安定綠（輔色）*/
  --danger: #d2452f;
  --warn: #e0982a;
  --ok: #2f8f76;
  --radius: 18px;
  --shadow: 0 10px 30px rgba(140,90,50,.10);
}
* { box-sizing: border-box; }
html, body { margin: 0; }
body {
  font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", system-ui, sans-serif;
  background: var(--cream);
  color: var(--ink);
  font-size: 17px;
  line-height: 1.75;
}
.app { min-height: 100vh; display: flex; flex-direction: column; }

/* 頂部：暖橘，非藍漸層 */
.topbar { background: linear-gradient(120deg, #e8743b, #f2994a); color: #fff; padding: 1.05rem 1.25rem; }
.brand { display: flex; align-items: center; gap: .8rem; max-width: 960px; margin: 0 auto; width: 100%; color: #fff; text-decoration: none; }
.title { font-size: 1.4rem; font-weight: 800; letter-spacing: .5px; }
.title .tw { font-size: .9rem; font-weight: 600; opacity: .9; }
.subtitle { font-size: .9rem; opacity: .92; }

/* 頁簽：米白底、暖橘選中，icon+字 */
.tabs { background: var(--cream-2); border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 10; }
.tabs-inner { max-width: 960px; margin: 0 auto; display: flex; gap: .2rem; flex-wrap: wrap; padding: .35rem .5rem; }
.tab { display: inline-flex; align-items: center; gap: .35rem; color: var(--ink-soft); text-decoration: none;
  padding: .5rem .75rem; border-radius: 999px; font-weight: 600; font-size: .95rem; transition: all .15s; white-space: nowrap; }
.tab:hover { background: var(--brand-soft); color: var(--brand-deep); }
.tab.on { background: var(--brand); color: #fff; }

.content { flex: 1; width: 100%; max-width: 820px; margin: 1.6rem auto; padding: 0 1rem; }
.footer { text-align: center; color: var(--ink-soft); padding: 2rem 1rem; font-size: .85rem; background: var(--cream-2); border-top: 1px solid var(--line); }
.footer p { margin: .2rem 0; }
.fnote { font-size: .78rem; opacity: .8; }

/* 共用元件 */
.card { background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); padding: 1.4rem 1.5rem; box-shadow: var(--shadow); margin-bottom: 1.2rem; }
.card h2 { margin: 0 0 .5rem; font-size: 1.35rem; }
.card h3 { margin: 0 0 .6rem; }
.muted { color: var(--ink-soft); }
.btn { cursor: pointer; border: none; border-radius: 999px; padding: .72rem 1.5rem; background: var(--brand); color: #fff; font-size: 1.05rem; font-weight: 700; transition: filter .15s, transform .1s; box-shadow: 0 6px 16px rgba(232,116,59,.3); }
.btn:hover:not(:disabled) { filter: brightness(1.05); transform: translateY(-1px); }
.btn:disabled { opacity: .5; cursor: default; box-shadow: none; }
.btn.ghost { background: #fff; color: var(--brand-deep); border: 1.6px solid var(--brand); box-shadow: none; }
textarea, .inp { width: 100%; padding: .8rem 1rem; border: 1.6px solid var(--line); border-radius: 14px; font-size: 1.05rem; font-family: inherit; background: var(--cream-2); }
textarea { min-height: 110px; resize: vertical; }
textarea:focus, .inp:focus { outline: none; border-color: var(--brand); background: #fff; }
.chip { display: inline-block; cursor: pointer; user-select: none; background: var(--brand-soft); color: var(--brand-deep); border: 1px solid #f6d6c1; border-radius: 999px; padding: .35rem .8rem; margin: .25rem .3rem 0 0; font-size: .88rem; transition: background .12s; }
.chip:hover { background: #fbdcca; }

/* 官方資源連結卡（rubric #5）*/
.gov-card { display: flex; align-items: center; gap: .8rem; background: var(--cream-2); border: 1px solid var(--line); border-left: 4px solid var(--accent); border-radius: 12px; padding: .8rem 1rem; text-decoration: none; color: var(--ink); transition: transform .12s, box-shadow .12s; }
.gov-card:hover { transform: translateY(-2px); box-shadow: var(--shadow); }
.gov-card .g-emoji { font-size: 1.6rem; }
.gov-card .g-t { font-weight: 700; }
.gov-card .g-s { font-size: .82rem; color: var(--ink-soft); }
</style>
