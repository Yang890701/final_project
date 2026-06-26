<script setup>
// 統一線性 icon 系統：同 viewBox、同線寬、圓頭線端（暖人文調性）
const props = defineProps({ name: String, size: { type: [Number, String], default: 22 } });
const paths = {
  home: ["M3 11.5 12 4l9 7.5", "M5 10v9h14v-9", "M10 19v-5h4v5"],
  detect: ["M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14Z", "M16 16l4.5 4.5", "M8.5 11h5M11 8.5v5"],
  chat: ["M4 5h16v11H9l-4 3v-3H4Z", "M8 10h8M8 13h5"],
  game: ["M7 8h10a4 4 0 0 1 4 4v0a4 4 0 0 1-4 4c-1.5 0-2.2-1-3-2H10c-.8 1-1.5 2-3 2a4 4 0 0 1-4-4v0a4 4 0 0 1 4-4Z", "M7 11v3M5.5 12.5h3", "M16 12h.01M18 14h.01"],
  intel: ["M4 20V10M9 20V4M14 20v-7M19 20V8"],
  help: ["M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18Z", "M9.2 9.2a2.8 2.8 0 0 1 5.4 1c0 1.8-2.6 2.3-2.6 4", "M12 17.5h.01"],
  heart: ["M12 20s-7-4.5-9.2-8.6C1.2 8.3 2.6 5 5.8 5 8 5 9.3 6.4 12 9c2.7-2.6 4-4 6.2-4 3.2 0 4.6 3.3 3 6.4C19 15.5 12 20 12 20Z"],
  shield: ["M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6l7-3Z", "M9 12l2 2 4-4"],
};
</script>
<template>
  <svg :width="size" :height="size" viewBox="0 0 24 24" fill="none"
       stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"
       aria-hidden="true" class="icon">
    <path v-for="(d, i) in paths[name]" :key="i" :d="d" />
  </svg>
</template>
<style scoped>.icon { display: inline-block; vertical-align: -0.18em; }</style>
