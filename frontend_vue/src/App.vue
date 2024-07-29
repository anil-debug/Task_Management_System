<template>
  <div id="app">
    <Menu @menu-select="selectMenu"/>
    <component :is="currentComponent"/>
  </div>
</template>

<script>
import Menu from './components/Menu.vue';
import CreateUser from './components/CreateUser.vue';
import CreateTask from './components/CreateTask.vue';
import ViewTasks from './components/ViewTasks.vue';
import UpdateTaskStatus from './components/UpdateTaskStatus.vue';

export default {
  name: 'App',
  components: {
    Menu,
    CreateUser,
    CreateTask,
    ViewTasks,
    UpdateTaskStatus
  },
  data() {
    return {
      currentComponent: 'CreateUser'  // Default component
    }
  },
  methods: {
    selectMenu(menuItem) {
      this.currentComponent = menuItem;
    }
  }
}
</script>

<style>
/* Add your styles here */
</style>
