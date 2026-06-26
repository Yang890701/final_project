<script setup>
import { ref, onMounted } from "vue";
import { getQuestions, answer } from "../api.js";
import GameSpot from "./games/GameSpot.vue";
import GameTrueFalse from "./games/GameTrueFalse.vue";
import GameStory from "./games/GameStory.vue";
import GameMatch from "./games/GameMatch.vue";

const mode = ref(null);
const modes = [
  { k: "tf", emoji: "⚡", title: "真假對決", desc: "限時二選一，連對衝高分", c: GameTrueFalse },
  { k: "spot", emoji: "🔎", title: "找碴遊戲", desc: "點出訊息裡的可疑字句", c: GameSpot },
  { k: "story", emoji: "🎭", title: "劇情選擇", desc: "看你會不會一路被騙到匯款", c: GameStory },
  { k: "match", emoji: "🧩", title: "類型配對", desc: "把話術配到正確詐騙類型", c: GameMatch },
  { k: "quiz", emoji: "📝", title: "情境問答", desc: "經典單選題，附解說", c: null },
];

// 經典問答（原本的）
const qs = ref([]); const qi = ref(0); const fb = ref(null); const sc = ref(0); const qdone = ref(false); const qerr = ref("");
async function loadQuiz() { qdone.value = false; qi.value = 0; sc.value = 0; fb.value = null; try { qs.value = await getQuestions(5); } catch (e) { qerr.value = "載入失敗：" + e.message; } }
async function choose(idx) { if (fb.value) return; try { fb.value = await answer(qs.value[qi.value].id, idx); if (fb.value.correct) sc.value++; } catch (e) { qerr.value = e.message; } }
function qnext() { if (qi.value + 1 >= qs.value.length) { qdone.value = true; return; } qi.value++; fb.value = null; }
function open(m) { mode.value = m; if (m.k === "quiz") loadQuiz(); }
</script>

<template>
  <div v-if="!mode" class="card">
    <h2>🎮 防詐練習</h2>
    <p class="muted">選一種玩法，邊玩邊練出辨識詐騙的直覺：</p>
    <div class="modes">
      <button v-for="m in modes" :key="m.k" class="mode" @click="open(m)">
        <span class="me">{{ m.emoji }}</span>
        <span><strong>{{ m.title }}</strong><br /><span class="muted">{{ m.desc }}</span></span>
      </button>
    </div>
  </div>

  <div v-else class="card">
    <button class="back" @click="mode = null">← 換玩法</button>
    <h2 style="margin-top:.4rem">{{ mode.emoji }} {{ mode.title }}</h2>

    <component :is="mode.c" v-if="mode.c" />

    <!-- 經典問答 -->
    <template v-else>
      <div v-if="qerr" style="color:var(--danger)">{{ qerr }}</div>
      <div v-else-if="qdone" class="qfin">
        <p class="big">{{ sc }} / {{ qs.length }}</p>
        <button class="btn" @click="loadQuiz">再玩一次</button>
      </div>
      <div v-else-if="qs.length">
        <p class="muted">第 {{ qi + 1 }}/{{ qs.length }} 題 · 得分 {{ sc }}</p>
        <h3>{{ qs[qi].prompt }}</h3>
        <button v-for="(o, i) in qs[qi].options" :key="i" class="opt"
          :class="fb && i === fb.correct_idx ? 'okc' : (fb && i !== fb.correct_idx ? 'dim' : '')"
          :disabled="!!fb" @click="choose(i)">{{ o }}</button>
        <div v-if="fb" class="fb">
          <p :style="{ color: fb.correct ? 'var(--ok)' : 'var(--danger)', fontWeight: 800 }">{{ fb.correct ? "✅ 答對" : "❌ 答錯" }}</p>
          <p>{{ fb.explanation }}</p>
          <button class="btn" @click="qnext">{{ qi + 1 >= qs.length ? "看結果" : "下一題" }}</button>
        </div>
      </div>
      <p v-else class="muted">載入中…</p>
    </template>
  </div>
</template>

<style scoped>
.modes { display: grid; grid-template-columns: 1fr; gap: .7rem; }
@media (min-width: 560px) { .modes { grid-template-columns: 1fr 1fr; } }
.mode { display: flex; align-items: center; gap: .8rem; text-align: left; cursor: pointer; background: var(--cream-2); border: 1.5px solid var(--line); border-radius: 16px; padding: 1rem; transition: all .14s; }
.mode:hover { transform: translateY(-3px); box-shadow: var(--shadow); border-color: #f4cdb6; }
.me { font-size: 1.8rem; }
.back { background: none; border: none; color: var(--brand-deep); cursor: pointer; font-weight: 700; font-size: .95rem; padding: 0; }
.opt { display: block; width: 100%; text-align: left; cursor: pointer; background: var(--cream-2); border: 1.5px solid var(--line); border-radius: 12px; padding: .8rem 1rem; margin: .5rem 0; font-size: 1.05rem; }
.opt:hover:not(:disabled) { border-color: var(--brand); background: var(--brand-soft); }
.opt.okc { border-color: var(--ok); background: #e9f7f2; }
.opt.dim { opacity: .5; }
.fb { margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--line); }
.qfin { text-align: center; } .big { font-size: 2.4rem; font-weight: 800; color: var(--brand); }
</style>
