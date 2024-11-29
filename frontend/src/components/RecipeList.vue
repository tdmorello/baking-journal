<template>
    <div>
      <h1>Recipes</h1>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <ul v-else>
        <li v-for="recipe in recipes" :key="recipe.id">
          <h2>{{ recipe.title }}</h2>
          <p><strong>Ingredients:</strong> {{ recipe.ingredients }}</p>
          <p><strong>Instructions:</strong> {{ recipe.instructions }}</p>
        </li>
      </ul>
    </div>
</template>


<script>
import axios from "axios";

export default {
data() {
    return {
    recipes: [],
    loading: true,
    error: null,
    };
},
created() {
    this.fetchRecipes();
},
methods: {
    async fetchRecipes() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/recipes/");
        this.recipes = response.data;
    } catch (err) {
        this.error = "Failed to load recipes.";
    } finally {
        this.loading = false;
    }
    },
},
};
</script>