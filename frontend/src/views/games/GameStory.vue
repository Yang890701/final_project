<script setup>
import { ref, computed } from "vue";
import { story } from "../../data/games.js";

const cur = ref(story.start);
const node = computed(() => story.nodes[cur.value]);
const ended = computed(() => !!node.value.end);
function pick(to) { cur.value = to; }
function restart() { cur.value = story.start; }
</script>
<template>
  <div v-if="ended" class="end" :class="node.end">
    <div class="emoji">{{ node.end === 'good' ? '🛡️' : '💸' }}</div>
    <h3>{{ node.end === 'good' ? '你守住了！' : '糟糕，被騙了…' }}</h3>
    <p>{{ node.text }}</p>
    <button class="btn" @click="restart">再玩一次</button>
  </div>
  <div v-else>
    <p class="muted">情境模擬 — 看你的選擇，會不會一路被騙到匯款：</p>
    <div class="npc">{{ node.npc }}</div>
    <div class="choices">
      <button v-for="(c, k) in node.choices" :key="k" class="choice" @click="pick(c.to)">{{ c.label }}</button>
    </div>
  </div>
</template>
<style scoped>
.npc { background: #fff; border: 1px solid var(--line); border-radius: 16px 16px 16px 3px; padding: 1rem 1.2rem; font-size: 1.1rem; line-height: 1.8; box-shadow: var(--shadow); margin: .6rem 0 1rem; }
.choices { display: flex; flex-direction: column; gap: .6rem; }
.choice { text-align: left; cursor: pointer; background: var(--brand-soft); color: var(--brand-deep); border: 1.5px solid #f4cdb6; border-radius: 14px; padding: .9rem 1.1rem; font-size: 1.05rem; font-weight: 600; transition: all .12s; }
.choice:hover { background: #fbdcca; transform: translateX(3px); }
.end { text-align: center; padding: 1rem; }
.end .emoji { font-size: 3rem; }
.end.bad h3 { color: var(--danger); } .end.good h3 { color: var(--ok); }
</style>
