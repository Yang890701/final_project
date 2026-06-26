import { createApp } from "vue";
import { createRouter, createWebHashHistory } from "vue-router";
import App from "./App.vue";
import HomeView from "./views/HomeView.vue";
import DetectView from "./views/DetectView.vue";
import GameView from "./views/GameView.vue";
import StatsView from "./views/StatsView.vue";

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: "/", name: "home", component: HomeView },
    { path: "/detect", name: "detect", component: DetectView },
    { path: "/game", name: "game", component: GameView },
    { path: "/stats", name: "stats", component: StatsView },
  ],
});

createApp(App).use(router).mount("#app");
