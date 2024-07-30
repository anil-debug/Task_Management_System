<template>
  <div class="menu">
    <ul>
      <li @click="emitMenu('createUser')">Create User</li>
      <li @click="emitMenu('createTask')">Create Task</li>
      <li @click="emitMenu('viewTasks')">View Tasks</li>
      <li @click="emitMenu('updateTaskStatus')">Update Task Status</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Menu',
  methods: {
    emitMenu(menuItem) {
      this.$emit('menu-select', menuItem);
    }
  }
}
</script>

<style scoped>
.menu ul {
  list-style-type: none;
  padding: 0;
}

.menu li {
  cursor: pointer;
  padding: 10px;
  border-bottom: 1px solid #ccc;
}

.menu li:hover {
  color: #007bff;
}
</style>
