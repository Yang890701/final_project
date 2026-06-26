<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>
  <header>
    <h1>🛡️ 反詐平台</h1>
    <nav>
      <RouterLink to="/">首頁</RouterLink>
      <RouterLink to="/detect">詐騙偵測</RouterLink>
      <RouterLink to="/game">模擬遊戲</RouterLink>
      <RouterLink to="/stats">詐騙統計</RouterLink>
    </nav>
  </header>
  <main>
    <RouterView />
  </main>
  <footer>期末專題 · 偵測（Gemini + RAG）／教學遊戲／統計視覺化</footer>
</template>

<style>
* { box-sizing: border-box; }
body { margin: 0; font-family: "Segoe UI", "Microsoft JhengHei", sans-serif; color: #1a1a2e; background: #f5f6fa; }
header { background: #16213e; color: #fff; padding: 1rem 1.5rem; }
header h1 { margin: 0 0 .5rem; font-size: 1.3rem; }
nav { display: flex; gap: 1rem; flex-wrap: wrap; }
nav a { color: #c9d1ff; text-decoration: none; padding: .25rem .5rem; border-radius: 6px; }
nav a.router-link-active { background: #0f3460; color: #fff; }
main { max-width: 880px; margin: 1.5rem auto; padding: 0 1rem; }
footer { text-align: center; color: #888; padding: 2rem 1rem; font-size: .85rem; }
button { cursor: pointer; border: none; border-radius: 8px; padding: .6rem 1.1rem; background: #0f3460; color: #fff; font-size: 1rem; }
button:disabled { opacity: .5; cursor: default; }
.card { background: #fff; border-radius: 12px; padding: 1.25rem; box-shadow: 0 2px 8px rgba(0,0,0,.06); margin-bottom: 1rem; }
textarea { width: 100%; min-height: 90px; padding: .6rem; border: 1px solid #ccc; border-radius: 8px; font-size: 1rem; }
</style>
