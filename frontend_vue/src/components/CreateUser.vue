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
        try {
          const response = await axios.post('http://backend:5000/users', {
            username: this.username,
            email: this.email
          });
          if (response.status === 201) {
            this.message = 'User created successfully!';
          }
        } catch (error) {
          this.message = 'Failed to create user.';
          console.error(error);
        }
      }
    }
  }
  </script>
  