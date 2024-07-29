<template>
    <div>
      <h2>View Tasks</h2>
      <input v-model.number="userId" placeholder="User ID" type="number"/>
      <button @click="viewTasks">View</button>
      <div v-if="tasks.length">
        <div v-for="task in tasks" :key="task.id" class="task">
          <p><strong>Title:</strong> {{ task.title }}</p>
          <p><strong>Description:</strong> {{ task.description }}</p>
          <p><strong>Due Date:</strong> {{ task.due_date }}</p>
          <p><strong>Status:</strong> {{ task.status }}</p>
          <hr />
        </div>
      </div>
      <p v-else>No tasks found.</p>
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
  .task {
    margin-bottom: 20px;
  }
  </style>
  