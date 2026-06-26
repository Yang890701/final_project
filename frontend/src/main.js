import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";
import HomeView from "./views/HomeView.vue";
import DetectView from "./views/DetectView.vue";
import GameView from "./views/GameView.vue";
import StatsView from "./views/StatsView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: HomeView },
    { path: "/detect", component: DetectView },
    { path: "/game", component: GameView },
    { path: "/stats", component: StatsView },
  ],
});

createApp(App).use(router).mount("#app");
