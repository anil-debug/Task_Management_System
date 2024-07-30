<template>
    <div class="main-container">
      <aside class="sidebar">
        <h2>Task Management System</h2>
        <ul>
          <li @click="setActiveSection('createUser')">Create New User</li>
          <li @click="setActiveSection('createTask')">Create New Task</li>
          <li @click="setActiveSection('viewTasks')">View Tasks</li>
          <li @click="setActiveSection('updateTaskStatus')">Update Task Status</li>
        </ul>
      </aside>
      <main class="content">
        <component :is="currentComponent"></component>
      </main>
    </div>
  </template>
  
  <script>
  import CreateUser from './CreateUser.vue';
  import CreateTask from './CreateTask.vue';
  import ViewTasks from './ViewTasks.vue';
  import UpdateTaskStatus from './UpdateTaskStatus.vue';
  
  export default {
    components: {
      CreateUser,
      CreateTask,
      ViewTasks,
      UpdateTaskStatus
    },
    data() {
      return {
        activeSection: 'createUser'
      };
    },
    computed: {
      currentComponent() {
        switch (this.activeSection) {
          case 'createUser':
            return CreateUser;
          case 'createTask':
            return CreateTask;
          case 'viewTasks':
            return ViewTasks;
          case 'updateTaskStatus':
            return UpdateTaskStatus;
          default:
            return CreateUser;
        }
      }
    },
    methods: {
      setActiveSection(section) {
        this.activeSection = section;
      }
    }
  };
  </script>
  
<style scoped>
.main-container {
  display: flex;
  height: 100vh; /* Full viewport height */
}

.sidebar {
  width: 250px; /* Adjust width as needed */
  background-color: #f4f4f4;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
  position: fixed; /* Ensure the sidebar stays fixed */
  top: 0;
  bottom: 0;
  left: 0;
}

.sidebar h2 {
  text-align: center;
  margin-bottom: 20px;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

.sidebar ul li {
  margin: 10px 0;
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.sidebar ul li:hover {
  background-color: #007bff;
  color: white;
}

.content {
  margin-left: 250px; /* Adjust margin to match sidebar width */
  padding: 20px;
  background-color: #ffffff;
  flex: 1;
  height: calc(100vh - 40px); /* Full height minus any header/footer height if applicable */
  overflow-y: auto; /* Add scroll if content exceeds viewport height */
  box-sizing: border-box; /* Include padding and border in element's total width and height */
}

h2 {
  font-size: 24px;
  margin-bottom: 20px;
}

input, textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box; /* Include padding and border in element's total width */
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #0056b3;
}

p {
  font-size: 16px;
  margin-top: 10px;
}
</style>
