<script setup>
import { ref, onMounted } from "vue";
import { getQuestions, answer } from "../api.js";

const questions = ref([]);
const idx = ref(0);
const picked = ref(null);
const feedback = ref(null);
const score = ref(0);
const done = ref(false);
const error = ref("");

async function load() {
  try {
    questions.value = await getQuestions(5);
  } catch (e) {
    error.value = "載入題目失敗：" + e.message;
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
  if (idx.value + 1 >= questions.value.length) {
    done.value = true;
  } else {
    idx.value++;
    picked.value = null;
    feedback.value = null;
  }
}

function restart() {
  idx.value = 0;
  picked.value = null;
  feedback.value = null;
  score.value = 0;
  done.value = false;
  load();
}
</script>

<template>
  <div class="card" v-if="error"><p style="color:#c0392b">{{ error }}</p></div>

  <div class="card" v-else-if="done">
    <h2>遊戲結束</h2>
    <p>你答對了 <strong>{{ score }} / {{ questions.length }}</strong> 題！</p>
    <button @click="restart">再玩一次</button>
  </div>

  <div class="card" v-else-if="questions.length">
    <p style="color:#888">第 {{ idx + 1 }} / {{ questions.length }} 題 · 得分 {{ score }}</p>
    <h3>{{ questions[idx].prompt }}</h3>
    <p>
      <button
        v-for="(opt, i) in questions[idx].options"
        :key="i"
        style="display:block;width:100%;text-align:left;margin:.4rem 0;background:#eef"
        :style="feedback && i === feedback.correct_idx ? 'background:#cfc' : (picked === i && !feedback?.correct ? 'background:#fcc' : '')"
        @click="choose(i)"
      >
        {{ opt }}
      </button>
    </p>
    <div v-if="feedback">
      <p :style="{ color: feedback.correct ? '#27ae60' : '#c0392b' }">
        {{ feedback.correct ? "✅ 答對了！" : "❌ 答錯了" }}
      </p>
      <p>{{ feedback.explanation }}</p>
      <button @click="next">下一題</button>
    </div>
  </div>

  <div class="card" v-else><p>載入中…</p></div>
</template>
