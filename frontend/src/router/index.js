import { createRouter, createWebHistory } from "vue-router";
import Dashboard from "@/views/Dashboard.vue";
import Recipes from "@/views/Recipes.vue";
import Experiments from "@/views/Experiments.vue";
// import Calendar from "@/views/Calendar.vue";
import CalendarView from "@/views/CalendarView.vue";
import NewRecipe from "@/views/NewRecipe.vue";
import NewExperiment from "@/views/NewExperiment.vue";


const routes = [
  { path: "/", component: Dashboard, children: [
    { path: "recipes", component: Recipes },
    { path: "recipes/new", component: NewRecipe },
    { path: "experiments", component: Experiments },
    { path: "experiments/new", component: NewExperiment },
    { path: "calendar", component: CalendarView },
  ] },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
