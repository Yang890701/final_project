<script setup>
import { ref, onMounted } from "vue";
import { getQuestions, answer } from "../api.js";

const questions = ref([]);
const idx = ref(0);
const feedback = ref(null);
const picked = ref(null);
const score = ref(0);
const done = ref(false);
const error = ref("");
const loading = ref(true);

async function load() {
  loading.value = true; error.value = "";
  try {
    questions.value = await getQuestions(5);
  } catch (e) {
    error.value = "載入題目失敗，請確認後端是否啟動：" + e.message;
  } finally {
    loading.value = false;
  }
}
onMounted(load);

async function choose(i) {
  if (feedback.value) return;
  picked.value = i;
  try {
    feedback.value = await answer(questions.value[idx.value].id, i);
    if (feedback.value.correct) score.value++;
  } catch (e) {
    error.value = "批改失敗：" + e.message;
  }
}
function next() {
  if (idx.value + 1 >= questions.value.length) { done.value = true; return; }
  idx.value++; picked.value = null; feedback.value = null;
}
function restart() {
  idx.value = 0; picked.value = null; feedback.value = null; score.value = 0; done.value = false; load();
}
function optClass(i) {
  if (!feedback.value) return "";
  if (i === feedback.value.correct_idx) return "opt-correct";
  if (i === picked.value) return "opt-wrong";
  return "";
}
</script>

<template>
  <div class="card" v-if="error"><p style="color:var(--danger)">{{ error }}</p></div>

  <div class="card" v-else-if="loading"><p class="muted">載入題目中…</p></div>

  <div class="card result" v-else-if="done">
    <h2>🎉 遊戲結束</h2>
    <p class="big">{{ score }} / {{ questions.length }}</p>
    <p class="muted">答對 {{ score }} 題！多練習就能練出辨識詐騙的直覺。</p>
    <button class="btn" @click="restart">再玩一次</button>
  </div>

  <div class="card" v-else-if="questions.length">
    <div class="progress">
      <span>第 {{ idx + 1 }} / {{ questions.length }} 題</span>
      <span>得分 {{ score }}</span>
    </div>
    <span class="tag">{{ questions[idx].scam_type || "綜合" }}</span>
    <h3 class="q">{{ questions[idx].prompt }}</h3>
    <button
      v-for="(opt, i) in questions[idx].options"
      :key="i"
      class="opt"
      :class="optClass(i)"
      :disabled="!!feedback"
      @click="choose(i)"
    >{{ opt }}</button>

    <div v-if="feedback" class="feedback">
      <p :style="{ color: feedback.correct ? 'var(--ok)' : 'var(--danger)', fontWeight: 800 }">
        {{ feedback.correct ? "✅ 答對了！" : "❌ 答錯了" }}
      </p>
      <p>{{ feedback.explanation }}</p>
      <button class="btn" @click="next">{{ idx + 1 >= questions.length ? "看結果" : "下一題" }}</button>
    </div>
  </div>
</template>

<style scoped>
.progress { display: flex; justify-content: space-between; color: var(--muted); font-weight: 700; margin-bottom: .4rem; }
.tag { display: inline-block; background: #eef2ff; color: #3147b8; border-radius: 6px; padding: .15rem .6rem; font-size: .85rem; }
.q { font-size: 1.25rem; margin: .6rem 0 1rem; }
.opt {
  display: block; width: 100%; text-align: left; cursor: pointer;
  background: #f7f9ff; border: 1.5px solid var(--line); border-radius: 10px;
  padding: .85rem 1rem; margin: .5rem 0; font-size: 1.05rem; transition: all .12s;
}
.opt:hover:not(:disabled) { border-color: var(--brand); background: #eef2ff; }
.opt:disabled { cursor: default; }
.opt-correct { border-color: var(--ok); background: #e9f7ef; }
.opt-wrong { border-color: var(--danger); background: #fdecec; }
.feedback { margin-top: 1rem; padding-top: 1rem; border-top: 1px solid var(--line); }
.result { text-align: center; }
.big { font-size: 2.6rem; font-weight: 800; color: var(--brand); margin: .3rem 0; }
</style>
