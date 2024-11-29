<template>
    <div class="dashboard">
      <!-- Left Sidebar -->
      <aside class="sidebar">
        <nav>
          <ul>
            <li><router-link to="/recipes">Recipes</router-link></li>
            <li><router-link to="/experiments">Experiments</router-link></li>
            <li><router-link to="/calendar">Calendar</router-link></li>
          </ul>
        </nav>
      </aside>
  
      <!-- Main Content Area -->
      <div class="main">
        <!-- Top Bar -->
        <header class="topbar">
          <div class="user-actions">
            <button @click="createRecipe">+ New Recipe</button>
            <button @click="createExperiment">+ New Experiment</button>
            <div class="user-icon">👤</div>
          </div>
        </header>
  
        <!-- Main Content -->
        <section class="content">
          <router-view />
        </section>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Dashboard",
    methods: {
      createRecipe() {
        // Navigate to the New Recipe page
        this.$router.push("/recipes/new");
      },
      createExperiment() {
        // Navigate to the New Experiment page
        this.$router.push("/experiments/new");
      },
    },
  };
  </script>
  
  <style scoped>
  .dashboard {
    display: flex;
    height: 100vh;
    font-family: Arial, sans-serif;
  }
  
  .sidebar {
    width: 250px;
    background-color: #2c3e50;
    color: white;
    padding: 20px;
    box-sizing: border-box;
  }
  
  .sidebar nav ul {
    list-style: none;
    padding: 0;
  }
  
  .sidebar nav ul li {
    margin: 10px 0;
  }
  
  .sidebar nav ul li a {
    color: white;
    text-decoration: none;
    font-size: 16px;
  }
  
  .sidebar nav ul li a:hover {
    text-decoration: underline;
  }
  
  .main {
    flex: 1;
    display: flex;
    flex-direction: column;
  }
  
  .topbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding: 10px 20px;
    background-color: #34495e;
    color: white;
  }
  
  .user-actions {
    display: flex;
    align-items: center;
    gap: 15px;
  }
  
  .user-actions button {
    padding: 5px 10px;
    font-size: 14px;
    border: none;
    border-radius: 5px;
    background-color: #1abc9c;
    color: white;
    cursor: pointer;
  }
  
  .user-actions button:hover {
    background-color: #16a085;
  }
  
  .user-icon {
    width: 30px;
    height: 30px;
    background-color: white;
    color: #2c3e50;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
  }
  
  .content {
    padding: 20px;
    box-sizing: border-box;
    background-color: #ecf0f1;
    flex: 1;
  }
  </style>
  