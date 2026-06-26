<script setup>
import { ref } from "vue";
import { detect } from "../api.js";

const text = ref("");
const loading = ref(false);
const result = ref(null);
const error = ref("");

const verdictLabel = { scam: "⚠️ 疑似詐騙", legit: "✅ 看起來正常", uncertain: "❓ 無法確定" };
const verdictColor = { scam: "#c0392b", legit: "#27ae60", uncertain: "#f39c12" };

async function run() {
  if (!text.value.trim()) return;
  loading.value = true;
  error.value = "";
  result.value = null;
  try {
    result.value = await detect(text.value);
  } catch (e) {
    error.value = "偵測失敗：" + e.message;
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div class="card">
    <h2>詐騙偵測</h2>
    <p>貼上可疑的訊息或網址，讓 AI 幫你判斷。</p>
    <textarea v-model="text" placeholder="例如：老師帶單保證獲利30%，加LINE進VIP群…"></textarea>
    <p><button :disabled="loading" @click="run">{{ loading ? "分析中…" : "開始偵測" }}</button></p>
    <p v-if="error" style="color:#c0392b">{{ error }}</p>
  </div>

  <div v-if="result" class="card">
    <h3 :style="{ color: verdictColor[result.verdict] }">
      {{ verdictLabel[result.verdict] || result.verdict }}
      <small style="color:#888">（信心 {{ Math.round(result.confidence * 100) }}%）</small>
    </h3>
    <p>{{ result.reasoning }}</p>
    <p style="font-size:.8rem;color:#888">判定引擎：{{ result.engine }}</p>
    <div v-if="result.similar_examples?.length">
      <h4>相似的歷史案例</h4>
      <ul>
        <li v-for="(ex, i) in result.similar_examples" :key="i">
          <strong>{{ ex.scam_type || "一般" }}</strong>（相似度 {{ ex.score }}）：{{ ex.content }}
        </li>
      </ul>
    </div>
  </div>
</template>
