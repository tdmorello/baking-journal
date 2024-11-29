<template>
  <div id="app">
    <nav>
      <nl>
        <li><router-link to="/recipes">Recipes</router-link></li>
      </nl>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>
