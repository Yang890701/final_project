<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
const features = [
  { icon: "🔍", title: "偵測中心", desc: "訊息 / 網址 / 電話 / 截圖四合一檢測，AI + 官方黑名單判斷是否詐騙。", to: "/detect" },
  { icon: "💬", title: "AI 問答助手", desc: "用聊天的方式問任何防詐問題，可以追問。", to: "/chat" },
  { icon: "🎮", title: "模擬遊戲", desc: "情境問答，邊玩邊學會辨識常見詐騙手法。", to: "/game" },
  { icon: "📊", title: "詐騙情報", desc: "最新手法警示牆、官方統計趨勢、手法圖鑑。", to: "/intel" },
  { icon: "🆘", title: "我被騙了", desc: "受害當下的即時行動步驟與求助管道。", to: "/help" },
  { icon: "💙", title: "關於我們", desc: "我們為什麼做、怎麼做、資料來源與限制。", to: "/about" },
];
</script>

<template>
  <!-- 問題鉤子（賣產品 / 說故事的開場）-->
  <div class="card hook">
    <h2>每天 336 件詐騙，一年捲走超過 500 億</h2>
    <p>2024 年全台詐騙案件 <strong>122,805 件</strong>、財損 <strong>502 億元</strong>，五年成長逾四倍。
       受害的可能是想多賺一點的上班族、渴望陪伴的長輩、第一次網購的學生。</p>
    <p class="mission">我們相信：<strong>少一個人被騙，就少一個破碎的家。</strong>
       這個平台，就是想把「看穿詐騙」這件事，變成每個人都做得到。</p>
    <div class="cta">
      <button class="btn" @click="router.push('/detect')">立即偵測可疑訊息</button>
      <button class="btn ghost" @click="router.push('/about')">我們為什麼做這個 →</button>
    </div>
    <p class="src">數據來源：內政部刑事警察局 / 165 打詐儀錶板</p>
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
.hook h2 { font-size: 1.7rem; color: #16213e; line-height: 1.4; }
.hook strong { color: var(--danger); }
.mission { background: #f0f5ff; border-left: 4px solid var(--brand); padding: .7rem .9rem; border-radius: 0 8px 8px 0; }
.mission strong { color: var(--brand); }
.cta { display: flex; gap: .7rem; flex-wrap: wrap; margin-top: 1rem; }
.btn.ghost { background: #fff; color: var(--brand); border: 1.5px solid var(--brand); }
.src { font-size: .8rem; color: var(--muted); margin-top: .8rem; }
.grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
@media (min-width: 680px) { .grid { grid-template-columns: repeat(3, 1fr); } }
.feature { cursor: pointer; transition: transform .15s, box-shadow .15s; margin: 0; }
.feature:hover { transform: translateY(-4px); box-shadow: 0 10px 24px rgba(20,30,60,.12); }
.f-icon { font-size: 2.4rem; }
.feature h3 { margin: .4rem 0; }
.go { color: var(--brand); font-weight: 700; }
</style>
