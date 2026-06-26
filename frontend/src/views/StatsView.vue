<script setup>
import { ref, onMounted, computed } from "vue";
import { getStats } from "../api.js";

const stats = ref(null);
const error = ref("");

onMounted(async () => {
  try {
    stats.value = await getStats(2021, 2025);
  } catch (e) {
    error.value = "載入統計失敗：" + e.message;
  }
});

const maxYear = computed(() =>
  stats.value ? Math.max(...stats.value.by_year.map((y) => y.case_count)) : 1,
);
const maxCat = computed(() =>
  stats.value ? Math.max(...stats.value.by_category.map((c) => c.case_count)) : 1,
);
const fmt = (n) => n.toLocaleString();
const億 = (n) => (n / 1e8).toFixed(1);
</script>

<template>
  <div class="card" v-if="error"><p style="color:#c0392b">{{ error }}</p></div>
  <template v-else-if="stats">
    <div class="card">
      <h2>年度詐騙案件趨勢（2021–2025）</h2>
      <div v-for="y in stats.by_year" :key="y.year" style="margin:.5rem 0">
        <span style="display:inline-block;width:3rem">{{ y.year }}</span>
        <span
          :style="`display:inline-block;height:1.1rem;background:#0f3460;border-radius:4px;width:${(y.case_count / maxYear) * 70}%`"
        ></span>
        <span style="margin-left:.5rem;color:#555">{{ fmt(y.case_count) }} 件 · 損失 {{ 億(y.loss_amount) }} 億</span>
      </div>
    </div>

    <div class="card">
      <h2>各類型詐騙占比</h2>
      <div v-for="c in stats.by_category" :key="c.category" style="margin:.5rem 0">
        <span style="display:inline-block;width:7rem">{{ c.category }}</span>
        <span
          :style="`display:inline-block;height:1.1rem;background:#c0392b;border-radius:4px;width:${(c.case_count / maxCat) * 60}%`"
        ></span>
        <span style="margin-left:.5rem;color:#555">{{ fmt(c.case_count) }} 件</span>
      </div>
    </div>
  </template>
  <div class="card" v-else><p>載入中…</p></div>
</template>
