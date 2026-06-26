<script setup>
import { useRouter } from "vue-router";
import Icon from "../components/Icon.vue";
import HeroArt from "../components/HeroArt.vue";
const router = useRouter();

const features = [
  { icon: "detect", title: "偵測中心", desc: "訊息・網址・電話・截圖，四合一幫你看一眼。", to: "/detect" },
  { icon: "chat", title: "AI 問答助手", desc: "像聊天一樣問防詐問題，可以一直追問。", to: "/chat" },
  { icon: "game", title: "防詐練習", desc: "找碴、真假對決、劇情選擇，玩中學。", to: "/game" },
  { icon: "intel", title: "詐騙情報", desc: "最新手法、官方數據、手法圖鑑。", to: "/intel" },
  { icon: "help", title: "我被騙了", desc: "受害當下，這裡有即時行動步驟。", to: "/help" },
  { icon: "heart", title: "關於我們", desc: "我們為什麼做、資料怎麼來。", to: "/about" },
];
const govs = [
  { emoji: "📞", t: "165 反詐騙專線", s: "諮詢・檢舉・查證，24 小時", href: "https://165.npa.gov.tw/" },
  { emoji: "📊", t: "165 打詐儀錶板", s: "官方即時詐騙數據", href: "https://165dashboard.tw/" },
];
</script>

<template>
  <!-- Hero：左文右圖，暖色，同理開場 -->
  <section class="hero">
    <div class="hero-text">
      <p class="eyebrow">每天 336 件詐騙，一年捲走超過 500 億</p>
      <h1>在按下匯款前，<br />先讓我陪你看一眼。</h1>
      <p class="lead">受害的，可能是想多賺一點的上班族、渴望陪伴的長輩、第一次網購的學生。
        我們把「看穿詐騙」變成每個人都做得到的事。</p>
      <div class="cta">
        <button class="btn" @click="router.push('/detect')">立即檢查可疑訊息</button>
        <button class="btn ghost" @click="router.push('/about')">我們為什麼做 →</button>
      </div>
    </div>
    <div class="hero-img"><HeroArt /></div>
  </section>

  <!-- 功能（不同節奏：兩欄卡片 + icon，非罐頭一排）-->
  <section class="feat-grid">
    <button v-for="f in features" :key="f.to" class="feat" @click="router.push(f.to)">
      <span class="fic"><Icon :name="f.icon" :size="24" /></span>
      <span class="ft">
        <strong>{{ f.title }}</strong>
        <span class="muted">{{ f.desc }}</span>
      </span>
    </button>
  </section>

  <!-- 官方資源連結卡（rubric #5）-->
  <section class="card govs">
    <h3>遇到狀況，這些官方管道能幫你</h3>
    <div class="gov-row">
      <a v-for="g in govs" :key="g.href" class="gov-card" :href="g.href" target="_blank" rel="noopener">
        <span class="g-emoji">{{ g.emoji }}</span>
        <span><span class="g-t">{{ g.t }}</span><br /><span class="g-s">{{ g.s }} ↗</span></span>
      </a>
    </div>
  </section>
</template>

<style scoped>
.hero { display: flex; align-items: center; gap: 1.5rem; background: linear-gradient(135deg, #fffaf3, #fde9dc); border: 1px solid var(--line); border-radius: 22px; padding: 1.8rem; margin-bottom: 1.4rem; box-shadow: var(--shadow); }
.eyebrow { color: var(--danger); font-weight: 700; font-size: .92rem; margin: 0 0 .4rem; }
.hero h1 { font-size: 1.9rem; line-height: 1.4; margin: 0 0 .6rem; color: var(--ink); }
.lead { color: var(--ink-soft); margin: 0 0 1.2rem; }
.cta { display: flex; gap: .7rem; flex-wrap: wrap; }
.hero-img { flex-shrink: 0; }
@media (max-width: 640px) { .hero { flex-direction: column-reverse; text-align: center; } .cta { justify-content: center; } .hero h1 { font-size: 1.55rem; } }

.feat-grid { display: grid; grid-template-columns: 1fr; gap: .8rem; margin-bottom: 1.4rem; }
@media (min-width: 640px) { .feat-grid { grid-template-columns: 1fr 1fr; } }
.feat { display: flex; align-items: flex-start; gap: .9rem; text-align: left; background: var(--card); border: 1px solid var(--line); border-radius: 16px; padding: 1rem 1.15rem; cursor: pointer; transition: transform .14s, box-shadow .14s, border-color .14s; }
.feat:hover { transform: translateY(-3px); box-shadow: var(--shadow); border-color: #f4cdb6; }
.fic { flex-shrink: 0; width: 44px; height: 44px; border-radius: 13px; background: var(--brand-soft); color: var(--brand-deep); display: grid; place-items: center; }
.ft { display: flex; flex-direction: column; gap: .15rem; }
.ft strong { font-size: 1.08rem; }
.ft .muted { font-size: .9rem; }

.govs h3 { margin-top: 0; }
.gov-row { display: grid; grid-template-columns: 1fr; gap: .7rem; }
@media (min-width: 560px) { .gov-row { grid-template-columns: 1fr 1fr; } }
</style>
