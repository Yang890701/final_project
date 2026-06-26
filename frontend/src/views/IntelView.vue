<script setup>
import { ref, onMounted, computed } from "vue";
import { getAlerts, getStats } from "../api.js";

const alerts = ref([]); const alertSrc = ref(""); const stats = ref(null); const err = ref("");

onMounted(async () => {
  try {
    const a = await getAlerts(8); alerts.value = a.alerts; alertSrc.value = a.source;
  } catch (e) { /* 警示牆失敗不致命 */ }
  try { stats.value = await getStats(2020, 2025); } catch (e) { err.value = "統計載入失敗：" + e.message; }
});

const maxYear = computed(() => stats.value?.by_year?.length ? Math.max(...stats.value.by_year.map(y => y.case_count)) : 1);
const maxType = computed(() => stats.value?.by_sample_type?.length ? Math.max(...stats.value.by_sample_type.map(c => c.count)) : 1);
const palette = ["#1e4fd6", "#d83a3a", "#e08a00", "#1f9d57", "#7c3aed", "#0891b2", "#db2777"];
const fmt = (n) => n.toLocaleString();
const toYi = (n) => n ? (n / 1e8).toFixed(0) + " 億" : "—";

const guide = [
  { icon: "📈", type: "假投資", desc: "保證獲利、老師帶單、加 VIP 群、初期小賺誘你加碼。", defend: "合法投資必有風險；勿匯款到個人帳戶。" },
  { icon: "💳", type: "解除分期付款", desc: "假客服稱訂單被設成分期，要你操作 ATM/網銀解除。", defend: "ATM 不能解除分期，這是話術；撥 165 查證。" },
  { icon: "👮", type: "假冒公務機關", desc: "自稱檢警/地檢，說你帳戶涉案，要匯到安全帳戶。", defend: "司法機關不會要你匯款或設安全帳戶。" },
  { icon: "🛒", type: "假網拍", desc: "超低價商品、要求私下先匯款、貨到付款詐騙。", defend: "用有保障的平台交易，勿私下匯款。" },
  { icon: "💌", type: "假交友（殺豬盤）", desc: "網路戀情後誘導投資，或編造海關扣留要付清關費。", defend: "沒見過面就談錢，幾乎都是詐騙。" },
  { icon: "📩", type: "釣魚簡訊", desc: "包裹/帳單異常，附陌生短網址誘你點擊登入。", defend: "別點連結，回官方 App/網站查詢。" },
];
</script>

<template>
  <!-- 警示牆 -->
  <div class="card">
    <h2>📰 最新詐騙手法警示牆</h2>
    <p class="muted">{{ alertSrc || '載入中…' }}</p>
    <div v-for="(a, i) in alerts" :key="i" class="alert">
      <div class="ahead"><span class="adate">{{ a.date }}</span><strong>{{ a.title }}</strong></div>
      <p class="muted asum">{{ a.summary }}</p>
    </div>
    <p v-if="!alerts.length" class="muted">（警示資料載入中或暫時無法取得）</p>
  </div>

  <!-- 統計 -->
  <div class="card" v-if="err"><p style="color:var(--danger)">{{ err }}</p></div>
  <template v-else-if="stats">
    <div class="card">
      <h2>📈 全台詐騙案件年度趨勢</h2>
      <p class="muted">內政部刑事警察局 / 165 打詐儀錶板公開統計</p>
      <div v-for="y in stats.by_year" :key="y.year" class="row">
        <span class="rl">{{ y.year }}</span>
        <div class="trk"><div class="fl" :style="{ width: (y.case_count/maxYear*100)+'%', background:'var(--brand)' }"></div></div>
        <span class="rv">{{ fmt(y.case_count) }} 件 · 財損 {{ toYi(y.loss_amount) }}</span>
      </div>
      <p class="note">ℹ️ {{ stats.note }}</p>
    </div>
    <div class="card">
      <h2>🧩 收集樣本的詐騙類型分布</h2>
      <p class="muted">本平台實際收集的 165 官方詐騙案例（真實資料）依類型分布</p>
      <div v-for="(c, i) in stats.by_sample_type" :key="c.scam_type" class="row">
        <span class="rl wide">{{ c.scam_type }}</span>
        <div class="trk"><div class="fl" :style="{ width: (c.count/maxType*100)+'%', background: palette[i%palette.length] }"></div></div>
        <span class="rv">{{ c.count }} 筆</span>
      </div>
    </div>
  </template>

  <!-- 手法圖鑑 -->
  <div class="card">
    <h2>📖 詐騙手法圖鑑</h2>
    <p class="muted">認得這些套路，就不容易上當</p>
    <div class="guide">
      <div v-for="g in guide" :key="g.type" class="gitem">
        <div class="gh">{{ g.icon }} <strong>{{ g.type }}</strong></div>
        <p class="muted">{{ g.desc }}</p>
        <p class="gdef">🛡️ {{ g.defend }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.alert { padding: .7rem 0; border-top: 1px solid var(--line); }
.alert:first-of-type { border-top: none; }
.ahead { display: flex; gap: .6rem; align-items: baseline; }
.adate { color: var(--muted); font-size: .82rem; white-space: nowrap; }
.asum { margin: .3rem 0 0; font-size: .92rem; }
.row { display: flex; align-items: center; gap: .7rem; margin: .55rem 0; }
.rl { width: 3.5rem; font-weight: 700; flex-shrink: 0; }
.rl.wide { width: 7rem; }
.trk { flex: 1; height: 22px; background: #eef0f5; border-radius: 6px; overflow: hidden; }
.fl { height: 100%; border-radius: 6px; transition: width .5s; }
.rv { width: 12rem; text-align: right; color: var(--muted); font-size: .9rem; flex-shrink: 0; }
.note { font-size: .82rem; color: var(--muted); background: #f7f9ff; border-left: 3px solid var(--brand); padding: .5rem .7rem; border-radius: 0 6px 6px 0; margin-top: .8rem; }
.guide { display: grid; grid-template-columns: 1fr; gap: .8rem; }
@media (min-width: 680px) { .guide { grid-template-columns: 1fr 1fr; } }
.gitem { background: #f7f9ff; border: 1px solid var(--line); border-radius: 10px; padding: .8rem 1rem; }
.gh { font-size: 1.1rem; margin-bottom: .3rem; }
.gdef { color: var(--ok); font-size: .9rem; margin: .4rem 0 0; }
@media (max-width: 600px) { .row { flex-wrap: wrap; } .rv { width: 100%; text-align: left; } }
</style>
