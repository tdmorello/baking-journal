import { createRouter, createWebHistory } from "vue-router";
import Recipes from "@/views/Recipes.vue";

const routes = [
  {
    path: "/recipes",
    name: "Recipes",
    component: Recipes,
  },
  // Add other routes here
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
