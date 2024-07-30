<template>
    <div>
      <h2>Update Task Status</h2>
      <input v-model.number="taskId" placeholder="Task ID" type="number"/>
      <select v-model="status">
        <option value="Pending">Pending</option>
        <option value="In Progress">In Progress</option>
        <option value="Completed">Completed</option>
      </select>
      <button @click="updateTaskStatus">Update Status</button>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        taskId: null,
        status: 'Pending',
        message: ''
      };
    },
    methods: {
      async updateTaskStatus() {
        try {
          const response = await axios.patch(`http://backend:5000/tasks/${this.taskId}`, {
            status: this.status
          });
          if (response.status === 200) {
            this.message = 'Task status updated successfully!';
          }
        } catch (error) {
          this.message = 'Failed to update task status.';
          console.error(error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Add specific styles for UpdateTaskStatus component */
  </style>
  