<template>
    <div>
      <h2>Create a New Recipe</h2>
      <form>
        <div>
          <label for="title">Title:</label>
          <input type="text" id="title" name="title" placeholder="Recipe Title" />
        </div>
        <div>
          <label for="ingredients">Ingredients:</label>
          <textarea id="ingredients" name="ingredients" placeholder="List of Ingredients"></textarea>
        </div>
        <div>
          <label for="instructions">Instructions:</label>
          <textarea id="instructions" name="instructions" placeholder="Cooking Instructions"></textarea>
        </div>
        <button type="submit">Save Recipe</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "NewRecipe",
  };
  </script>
  