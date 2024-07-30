<template>
    <div>
      <h2>Create New User</h2>
      <input v-model="username" placeholder="Username"/>
      <input v-model="email" placeholder="Email"/>
      <button @click="createUser">Create</button>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'CreateUser',
    data() {
      return {
        username: '',
        email: '',
        message: ''
      }
    },
    methods: {
      async createUser() {
        const backendUrl = process.env.VUE_APP_BACKEND_URL;
        console.log(`Backend URL: ${backendUrl}`);
        console.log(`Attempting to create user with username: ${this.username} and email: ${this.email}`);
        try {
          const response = await axios.post(`${backendUrl}/users`, {
            username: this.username,
            email: this.email
          });
          console.log('Response:', response.data);
          if (response.status === 201) {
            this.message = 'User created successfully!';
          }
        } catch (error) {
          console.error('Error creating user:', error.response ? error.response.data : error.message);
          this.message = 'Failed to create user.';
        }
      }
    }
  }
  </script>
  