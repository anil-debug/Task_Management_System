<template>
  <div class="view-tasks-container">
    <h2>View Tasks</h2>
    <form @submit.prevent="viewTasks" class="view-tasks-form">
      <label for="userId">User ID</label>
      <input v-model.number="userId" id="userId" placeholder="User ID" type="number" />

      <button type="submit">View</button>
    </form>
    
    <div v-if="tasks.length" class="tasks-list">
      <div v-for="task in tasks" :key="task.id" class="task">
        <p><strong>Title:</strong> {{ task.title }}</p>
        <p><strong>Description:</strong> {{ task.description }}</p>
        <p><strong>Due Date:</strong> {{ task.due_date }}</p>
        <p><strong>Status:</strong> {{ task.status }}</p>
        <hr />
      </div>
    </div>
    <p v-else class="no-tasks">No tasks found.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userId: null,
      tasks: [],
    };
  },
  methods: {
    async viewTasks() {
      if (this.userId) {
        try {
          const response = await axios.get(`http://backend:5000/tasks/${this.userId}`);
          this.tasks = response.data;
        } catch (error) {
          console.error('Failed to fetch tasks:', error);
          alert('Failed to retrieve tasks.');
        }
      } else {
        alert('Please enter a User ID.');
      }
    },
  },
};
</script>

<style scoped>
.view-tasks-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}

h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.view-tasks-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.view-tasks-form label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.view-tasks-form input {
  margin-bottom: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.view-tasks-form button {
  padding: 0.75rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

.view-tasks-form button:hover {
  background-color: #0056b3;
}

.tasks-list {
  margin-top: 1rem;
}

.task {
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-bottom: 1rem;
  background-color: #f9f9f9;
}

.no-tasks {
  text-align: center;
  color: #d9534f;
  font-weight: bold;
}
</style>
