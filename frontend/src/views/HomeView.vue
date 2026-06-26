<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
const features = [
  { icon: "🔍", title: "詐騙偵測", desc: "貼上可疑訊息或網址，AI（自訓模型 + Gemini）判斷是否詐騙並解釋理由。", to: "/detect" },
  { icon: "🎮", title: "模擬遊戲", desc: "情境問答，邊玩邊學會辨識常見詐騙手法。", to: "/game" },
  { icon: "📊", title: "詐騙統計", desc: "2021–2025 詐騙趨勢與類型分布，數據一目了然。", to: "/stats" },
];
</script>

<template>
  <div class="card hero">
    <h2>🛡️ 守護你，不被詐騙</h2>
    <p class="muted">
      本平台用真實的官方詐騙資料訓練偵測模型，並提供互動教學與數據視覺化，
      幫你看穿詐騙話術。資料來源：警政署 165 反詐騙開放資料。
    </p>
  </div>

  <div class="grid">
    <div v-for="f in features" :key="f.to" class="card feature" @click="router.push(f.to)">
      <div class="f-icon">{{ f.icon }}</div>
      <h3>{{ f.title }}</h3>
      <p class="muted">{{ f.desc }}</p>
      <span class="go">立即使用 →</span>
    </div>
  </div>
</template>

<style scoped>
.hero h2 { font-size: 1.6rem; }
.grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
@media (min-width: 680px) { .grid { grid-template-columns: repeat(3, 1fr); } }
.feature { cursor: pointer; transition: transform .15s, box-shadow .15s; margin: 0; }
.feature:hover { transform: translateY(-4px); box-shadow: 0 10px 24px rgba(20,30,60,.12); }
.f-icon { font-size: 2.4rem; }
.feature h3 { margin: .4rem 0; }
.go { color: var(--brand); font-weight: 700; }
</style>
