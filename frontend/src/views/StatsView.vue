<script setup>
import { ref, onMounted, computed } from "vue";
import { getStats } from "../api.js";

const stats = ref(null);
const error = ref("");

onMounted(async () => {
  try {
    stats.value = await getStats(2020, 2025);
  } catch (e) {
    error.value = "載入統計失敗，請確認後端是否啟動：" + e.message;
  }
});

const maxYear = computed(() => stats.value?.by_year?.length ? Math.max(...stats.value.by_year.map((y) => y.case_count)) : 1);
const maxType = computed(() => stats.value?.by_sample_type?.length ? Math.max(...stats.value.by_sample_type.map((c) => c.count)) : 1);
const palette = ["#1e4fd6", "#d83a3a", "#e08a00", "#1f9d57", "#7c3aed", "#0891b2", "#db2777"];

function fmt(n) { return n.toLocaleString(); }
function toYi(n) { return n ? (n / 1e8).toFixed(0) + " 億" : "—"; }
</script>

<template>
  <div class="card" v-if="error"><p style="color:var(--danger)">{{ error }}</p></div>

  <template v-else-if="stats">
    <div class="card">
      <h2>📈 全台詐騙案件年度趨勢</h2>
      <p class="muted">內政部刑事警察局 / 165 打詐儀錶板公開統計</p>
      <div v-for="y in stats.by_year" :key="y.year" class="row">
        <span class="row-label">{{ y.year }}</span>
        <div class="track">
          <div class="fill" :style="{ width: (y.case_count / maxYear * 100) + '%', background: 'var(--brand)' }"></div>
        </div>
        <span class="row-val">{{ fmt(y.case_count) }} 件 · 財損 {{ toYi(y.loss_amount) }}</span>
      </div>
      <p class="note">ℹ️ {{ stats.note }}</p>
    </div>

    <div class="card">
      <h2>🧩 收集樣本的詐騙類型分布</h2>
      <p class="muted">本平台實際收集的 165 官方詐騙闢謠案例（真實資料）依類型分布</p>
      <div v-for="(c, i) in stats.by_sample_type" :key="c.scam_type" class="row">
        <span class="row-label wide">{{ c.scam_type }}</span>
        <div class="track">
          <div class="fill" :style="{ width: (c.count / maxType * 100) + '%', background: palette[i % palette.length] }"></div>
        </div>
        <span class="row-val">{{ c.count }} 筆</span>
      </div>
      <p class="note">官方統計指出「假投資」為財損最大宗（2022 年約占案件 22%、財損近半）。</p>
    </div>
  </template>

  <div class="card" v-else><p class="muted">載入統計中…</p></div>
</template>

<style scoped>
.row { display: flex; align-items: center; gap: .7rem; margin: .55rem 0; }
.row-label { width: 3.5rem; font-weight: 700; flex-shrink: 0; }
.row-label.wide { width: 7rem; }
.track { flex: 1; height: 22px; background: #eef0f5; border-radius: 6px; overflow: hidden; }
.fill { height: 100%; border-radius: 6px; transition: width .5s; }
.row-val { width: 12rem; text-align: right; color: var(--muted); font-size: .9rem; flex-shrink: 0; }
.note { font-size: .82rem; color: var(--muted); background: #f7f9ff; border-left: 3px solid var(--brand); padding: .5rem .7rem; border-radius: 0 6px 6px 0; margin-top: .8rem; }
@media (max-width: 600px) {
  .row { flex-wrap: wrap; }
  .row-val { width: 100%; text-align: left; }
}
</style>
