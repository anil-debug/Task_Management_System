<template>
  <div class="create-task-container">
    <h2>Create New Task</h2>
    <form @submit.prevent="createTask" class="task-form">
      <label for="title">Title</label>
      <input v-model="title" id="title" placeholder="Title" type="text" />

      <label for="description">Description</label>
      <textarea v-model="description" id="description" placeholder="Description"></textarea>

      <label for="dueDate">Due Date</label>
      <input v-model="dueDate" id="dueDate" type="date" />

      <label for="userId">User ID</label>
      <input v-model.number="userId" id="userId" placeholder="User ID" type="number" />

      <button type="submit">Create</button>
      
      <p v-if="message" class="message">{{ message }}</p>
    </form>
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

<style scoped>
.create-task-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 1rem;
}

h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.task-form {
  display: flex;
  flex-direction: column;
}

.task-form label {
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.task-form input,
.task-form textarea {
  margin-bottom: 1rem;
  padding: 0.5rem;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.task-form input[type="date"] {
  padding: 0.5rem 0.75rem;
}

.task-form button {
  padding: 0.75rem;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
}

.task-form button:hover {
  background-color: #0056b3;
}

.message {
  color: #d9534f;
  text-align: center;
  margin-top: 1rem;
}
</style>
