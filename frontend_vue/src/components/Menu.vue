<template>
    <div class="menu">
      <ul>
        <li @click="emitMenu('CreateUser')">Create User</li>
        <li @click="emitMenu('CreateTask')">Create Task</li>
        <li @click="emitMenu('ViewTasks')">View Tasks</li>
        <!-- <li @click="emitMenu('UpdateTaskStatus')">Update Task Status</li> -->
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
  
  <style>
  .menu ul {
    list-style-type: none;
    padding: 0;
  }
  
  .menu li {
    cursor: pointer;
    padding: 10px;
    border-bottom: 1px solid #ccc;
  }
  </style>
  