<script setup>
import { ref, onMounted, computed } from "vue";
import { getStats } from "../api.js";

const stats = ref(null);
const error = ref("");

onMounted(async () => {
  try {
    stats.value = await getStats(2021, 2025);
  } catch (e) {
    error.value = "載入統計失敗，請確認後端是否啟動：" + e.message;
  }
});

const maxYear = computed(() => stats.value ? Math.max(...stats.value.by_year.map((y) => y.case_count)) : 1);
const maxCat = computed(() => stats.value ? Math.max(...stats.value.by_category.map((c) => c.case_count)) : 1);
const palette = ["#1e4fd6", "#d83a3a", "#e08a00", "#1f9d57", "#7c3aed", "#0891b2"];

function fmt(n) { return n.toLocaleString(); }
function toYi(n) { return (n / 1e8).toFixed(1); }
</script>

<template>
  <div class="card" v-if="error"><p style="color:var(--danger)">{{ error }}</p></div>

  <template v-else-if="stats">
    <div class="card">
      <h2>📈 年度詐騙案件趨勢</h2>
      <p class="muted">2021–2025 各年通報案件數與財損（資料來源：165 反詐騙開放資料）</p>
      <div v-for="y in stats.by_year" :key="y.year" class="row">
        <span class="row-label">{{ y.year }}</span>
        <div class="track">
          <div class="fill" :style="{ width: (y.case_count / maxYear * 100) + '%', background: 'var(--brand)' }"></div>
        </div>
        <span class="row-val">{{ fmt(y.case_count) }} 件 · 損失 {{ toYi(y.loss_amount) }} 億</span>
      </div>
    </div>

    <div class="card">
      <h2>🧩 各類型詐騙占比</h2>
      <p class="muted">哪一種詐騙最常見？</p>
      <div v-for="(c, i) in stats.by_category" :key="c.category" class="row">
        <span class="row-label wide">{{ c.category }}</span>
        <div class="track">
          <div class="fill" :style="{ width: (c.case_count / maxCat * 100) + '%', background: palette[i % palette.length] }"></div>
        </div>
        <span class="row-val">{{ fmt(c.case_count) }} 件</span>
      </div>
    </div>
  </template>

  <div class="card" v-else><p class="muted">載入統計中…</p></div>
</template>

<style scoped>
.row { display: flex; align-items: center; gap: .7rem; margin: .55rem 0; }
.row-label { width: 3rem; font-weight: 700; flex-shrink: 0; }
.row-label.wide { width: 6.5rem; }
.track { flex: 1; height: 22px; background: #eef0f5; border-radius: 6px; overflow: hidden; }
.fill { height: 100%; border-radius: 6px; transition: width .5s; }
.row-val { width: 11rem; text-align: right; color: var(--muted); font-size: .9rem; flex-shrink: 0; }
@media (max-width: 600px) {
  .row { flex-wrap: wrap; }
  .row-val { width: 100%; text-align: left; }
}
</style>
