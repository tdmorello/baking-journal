<template>
    <div>
      <h1>Experiments</h1>
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <ul v-else>
        <li v-for="experiment in experiments" :key="experiment.id">
          <h2>{{ experiment.recipe }}</h2>
          <p>{{ experiment.created_at }}</p>
          <p><strong>Notes:</strong> {{ experiment.notes }}</p>
          <p><strong>Outcome:</strong> {{ experiment.outcome }}</p>
        </li>
      </ul>
    </div>
</template>


<script>
import axios from "axios";

export default {
data() {
    return {
    experiments: [],
    loading: true,
    error: null,
    };
},
created() {
    this.fetchExperiments();
},
methods: {
    async fetchExperiments() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/api/experiments/");
        this.experiments = response.data;
    } catch (err) {
        this.error = "Failed to load experiments.";
    } finally {
        this.loading = false;
    }
    },
},
};
</script>