<template>
    <div>
      <h1>Recipes</h1>
      <ul>
        <li v-for="recipe in recipes" :key="recipe.id">{{ recipe.title }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import api from "../services/api";
  
  export default {
    data() {
      return {
        recipes: [],
      };
    },
    async mounted() {
      try {
        const response = await api.get("recipes/");
        this.recipes = response.data;
      } catch (error) {
        console.error(error);
      }
    },
  };
  </script>
  