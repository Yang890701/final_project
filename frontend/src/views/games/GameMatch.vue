<script setup>
import { ref } from "vue";
import { matchItems, matchTypes } from "../../data/games.js";

const picked = ref(null);          // 選中的話術卡 index
const matched = ref({});           // itemIndex -> true
const wrong = ref(null);           // 暫存錯誤動畫
const done = ref(false);

function pickItem(idx) { if (matched.value[idx]) return; picked.value = idx; }
function chooseType(t) {
  if (picked.value === null) return;
  const it = matchItems[picked.value];
  if (it.type === t) {
    matched.value = { ...matched.value, [picked.value]: true };
    picked.value = null;
    if (Object.keys(matched.value).length === matchItems.length) done.value = true;
  } else {
    wrong.value = t; setTimeout(() => (wrong.value = null), 400);
  }
}
function restart() { picked.value = null; matched.value = {}; done.value = false; }
</script>
<template>
  <div v-if="done" class="fin">
    <h3>🧩 全部配對成功！</h3>
    <p>你已經能分辨這些常見詐騙類型了，很棒！</p>
    <button class="btn" @click="restart">再玩一次</button>
  </div>
  <div v-else>
    <p class="muted">先點一張<strong>話術卡</strong>，再點它屬於的<strong>詐騙類型</strong>：</p>
    <div class="items">
      <button v-for="(it, idx) in matchItems" :key="idx" class="it" :class="{ on: picked === idx, done: matched[idx] }" :disabled="matched[idx]" @click="pickItem(idx)">
        {{ matched[idx] ? "✅ " : "" }}{{ it.text }}
      </button>
    </div>
    <div class="types">
      <button v-for="t in matchTypes" :key="t" class="ty" :class="{ shake: wrong === t }" @click="chooseType(t)">{{ t }}</button>
    </div>
    <p class="muted">已配對 {{ Object.keys(matched).length }} / {{ matchItems.length }}</p>
  </div>
</template>
<style scoped>
.items { display: flex; flex-direction: column; gap: .5rem; margin: .6rem 0 1rem; }
.it { text-align: left; cursor: pointer; background: var(--cream-2); border: 1.5px solid var(--line); border-radius: 12px; padding: .7rem 1rem; font-size: 1rem; transition: all .12s; }
.it.on { border-color: var(--brand); background: var(--brand-soft); }
.it.done { opacity: .55; border-color: var(--ok); }
.types { display: flex; flex-wrap: wrap; gap: .5rem; }
.ty { cursor: pointer; background: #fff; border: 1.6px solid var(--brand); color: var(--brand-deep); border-radius: 999px; padding: .5rem 1rem; font-weight: 700; }
.ty:hover { background: var(--brand-soft); }
.shake { animation: sh .4s; background: #fdecec; border-color: var(--danger); color: var(--danger); }
@keyframes sh { 0%,100%{transform:translateX(0)} 25%{transform:translateX(-5px)} 75%{transform:translateX(5px)} }
.fin { text-align: center; }
</style>
