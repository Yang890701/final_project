<script setup>
import { ref } from "vue";
import { detect } from "../api.js";

const text = ref("");
const loading = ref(false);
const result = ref(null);
const error = ref("");

const examples = [
  "老師帶單保證獲利30%，加LINE進VIP群",
  "您的帳戶涉及洗錢，請將存款匯到安全帳戶配合調查",
  "媽我晚點回家，晚餐不用等我",
  "您的包裹地址有誤，請點 http://reurl-fake.xyz 更新資料",
];

const badge = {
  scam: { label: "⚠️ 疑似詐騙", color: "var(--danger)", bg: "#fdecec" },
  legit: { label: "✅ 看起來正常", color: "var(--ok)", bg: "#e9f7ef" },
  uncertain: { label: "❓ 無法確定", color: "var(--warn)", bg: "#fff6e6" },
};

function useExample(e) { text.value = e; }

async function run() {
  if (!text.value.trim()) return;
  loading.value = true; error.value = ""; result.value = null;
  try {
    result.value = await detect(text.value);
  } catch (e) {
    error.value = "偵測失敗，請確認後端是否啟動：" + e.message;
  } finally {
    loading.value = false;
  }
}
</script>

<template>
  <div class="card">
    <h2>🔍 詐騙偵測</h2>
    <p class="muted">把可疑的訊息或網址貼進來，AI 幫你判斷是不是詐騙，並說明理由。</p>
    <textarea v-model="text" placeholder="例如：老師帶單保證獲利30%，加LINE進VIP群…"></textarea>
    <div style="margin:.6rem 0">
      <span class="muted" style="font-size:.9rem">試試範例：</span><br />
      <span v-for="e in examples" :key="e" class="chip" @click="useExample(e)">{{ e.slice(0, 16) }}…</span>
    </div>
    <button class="btn" :disabled="loading || !text.trim()" @click="run">
      {{ loading ? "分析中…" : "開始偵測" }}
    </button>
    <p v-if="error" style="color:var(--danger);margin-top:.8rem">{{ error }}</p>
    <p class="disclosure">
      🔒 隱私說明：您的訊息會傳送至本平台後端分析；若啟用 AI 解釋，會一併送交 Google Gemini 處理。
      請勿輸入他人個資。模型基於有限官方樣本訓練，信心分數僅供參考、非法律判定。
    </p>
  </div>

  <div v-if="result" class="card">
    <div class="verdict" :style="{ background: badge[result.verdict]?.bg }">
      <span class="v-label" :style="{ color: badge[result.verdict]?.color }">
        {{ badge[result.verdict]?.label || result.verdict }}
      </span>
      <span class="v-conf">風險信心 {{ Math.round(result.confidence * 100) }}%</span>
    </div>
    <div class="bar"><div class="bar-fill" :style="{ width: (result.confidence*100)+'%', background: badge[result.verdict]?.color }"></div></div>

    <h3 style="margin-top:1.1rem">為什麼這樣判斷？</h3>
    <p>{{ result.reasoning }}</p>
    <p class="muted" style="font-size:.85rem">判定引擎：{{ result.engine }}</p>

    <template v-if="result.similar_examples?.length">
      <h3>資料庫中相似的歷史案例</h3>
      <ul class="sims">
        <li v-for="(ex, i) in result.similar_examples" :key="i">
          <span class="tag">{{ ex.scam_type || "一般" }}</span>{{ ex.content.slice(0, 50) }}…
        </li>
      </ul>
    </template>
  </div>
</template>

<style scoped>
.verdict { display: flex; align-items: center; justify-content: space-between; padding: .9rem 1.1rem; border-radius: 10px; }
.v-label { font-size: 1.35rem; font-weight: 800; }
.v-conf { color: var(--muted); font-weight: 700; }
.bar { height: 10px; background: #eef0f5; border-radius: 999px; margin-top: .6rem; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 999px; transition: width .4s; }
.sims { list-style: none; padding: 0; margin: .4rem 0 0; }
.sims li { padding: .55rem 0; border-top: 1px solid var(--line); font-size: .95rem; }
.tag { display: inline-block; background: #eef2ff; color: #3147b8; border-radius: 6px; padding: .1rem .5rem; margin-right: .5rem; font-size: .8rem; }
.disclosure { margin-top: 1rem; font-size: .8rem; color: var(--muted); background: #f7f9ff; border-left: 3px solid var(--warn); padding: .55rem .75rem; border-radius: 0 6px 6px 0; line-height: 1.6; }
</style>
