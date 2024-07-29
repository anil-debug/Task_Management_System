<template>
    <div>
      <h2>Create New Task</h2>
      <input v-model="title" placeholder="Title"/>
      <textarea v-model="description" placeholder="Description"></textarea>
      <input v-model="dueDate" type="date"/>
      <input v-model.number="userId" placeholder="User ID" type="number"/>
      <button @click="createTask">Create</button>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CreateTask',
    data() {
      return {
        title: '',
        description: '',
        dueDate: '',
        userId: null,
        message: ''
      }
    },
    methods: {
      async createTask() {
        try {
          const response = await axios.post('http://backend:5000/tasks', {
            title: this.title,
            description: this.description,
            due_date: this.dueDate,
            user_id: this.userId
          });
          if (response.status === 201) {
            this.message = 'Task created successfully!';
          }
        } catch (error) {
          this.message = 'Failed to create task.';
          console.error(error);
        }
      }
    }
  }
  </script>
  