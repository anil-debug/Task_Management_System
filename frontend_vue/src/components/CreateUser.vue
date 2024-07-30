<template>
  <div class="create-user-container">
    <h2>Create New User</h2>
    <form @submit.prevent="createUser" class="user-form">
      <label for="username">Username</label>
      <input v-model="username" id="username" placeholder="Username" type="text" />

      <label for="email">Email</label>
      <input v-model="email" id="email" placeholder="Email" type="email" />

      <button type="submit">Create</button>
      
      <p v-if="message" class="message">{{ message }}</p>
    </form>
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

<style scoped>
.create-user-container {
  max-width: 500px;
  margin: 0 auto;
  padding: 1rem;
}

h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.user-form {
  display: flex;
  flex-direction: column;
}

.user-form label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.user-form input {
  margin-bottom: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.user-form button {
  padding: 0.75rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

.user-form button:hover {
  background-color: #0056b3;
}

.message {
  color: #d9534f;
  text-align: center;
  margin-top: 1rem;
}
</style>
