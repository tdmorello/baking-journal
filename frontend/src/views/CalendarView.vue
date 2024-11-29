<template>
  <div class="calendar">
    <!-- Month Navigation -->
    <header class="calendar-header">
      <button @click="changeMonth(-1)">◀</button>
      <h2>{{ formattedMonth }}</h2>
      <button @click="changeMonth(1)">▶</button>
    </header>

    <!-- Calendar Grid -->
    <div class="calendar-grid">
      <div class="day-name" v-for="day in dayNames" :key="day">{{ day }}</div>
      <div
        class="day"
        v-for="(date, index) in days"
        :key="index"
        :class="{ 'current-day': isToday(date), 'has-experiments': hasExperiments(date) }"
      >
        <span>{{ date.getDate() }}</span>
        <!-- Experiment Links -->
        <ul>
          <li v-for="experiment in getExperiments(date)" :key="experiment.id">
            <router-link :to="'/experiments/' + experiment.id">
              {{ experiment.recipe || 'Experiment' }}
            </router-link>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import { format, startOfMonth, endOfMonth, startOfWeek, endOfWeek, addDays, subMonths, addMonths, isSameDay, isToday } from "date-fns";
import axios from "axios";

export default {
  data() {
    return {
      currentMonth: new Date(),
      experiments: [], // List of experiments fetched from API
    };
  },
  computed: {
    // Get formatted month name and year
    formattedMonth() {
      return format(this.currentMonth, "MMMM yyyy");
    },
    // Generate day names for the calendar header
    dayNames() {
      return ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    },
    // Generate all the days to display in the calendar grid
    days() {
      const start = startOfWeek(startOfMonth(this.currentMonth));
      const end = endOfWeek(endOfMonth(this.currentMonth));
      let date = start;
      const days = [];
      while (date <= end) {
        days.push(date);
        date = addDays(date, 1);
      }
      return days;
    },
  },
  methods: {
    // Change the month by adding or subtracting months
    changeMonth(offset) {
      this.currentMonth = offset > 0 ? addMonths(this.currentMonth, 1) : subMonths(this.currentMonth, 1);
    },
    // Check if the date is today
    isToday(date) {
      return isToday(date);
    },
    // Check if the date has experiments
    hasExperiments(date) {
      return this.getExperiments(date).length > 0;
    },
    // Get experiments for a specific date
    getExperiments(date) {
      return this.experiments.filter((experiment) =>
        isSameDay(new Date(experiment.created_at), date)
      );
    },
    // Fetch experiments from API
    async fetchExperiments() {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/experiments/");
        this.experiments = response.data;
      } catch (error) {
        console.error("Failed to fetch experiments:", error);
      }
    },
  },
  created() {
    this.fetchExperiments(); // Load experiments on component creation
  },
};
</script>

<style scoped>
.calendar {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.calendar-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 600px;
  margin-bottom: 10px;
}

.calendar-header h2 {
  font-size: 1.5em;
}

.calendar-grid {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 5px;
  width: 100%;
  max-width: 600px;
}

.day-name {
  font-weight: bold;
  text-align: center;
}

.day {
  border: 1px solid #ddd;
  padding: 10px;
  min-height: 100px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
}

.day.current-day {
  background-color: #f0f8ff;
}

.day.has-experiments {
  background-color: #e6f7e6;
}

.day span {
  font-size: 14px;
  font-weight: bold;
}

.day ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.day ul li {
  font-size: 12px;
  text-align: left;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.day ul li a {
  color: #007bff;
  text-decoration: none;
}

.day ul li a:hover {
  text-decoration: underline;
}
</style>
