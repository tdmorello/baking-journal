<!-- Recipes.vue -->
<template>
    <div>
      <h1>All Recipes</h1>
      <RecipeList />
    </div>
</template>

<script>
import RecipeList from "@/components/RecipeList.vue";

export default {
components: {
    RecipeList,
},
};
</script>
