<template>
  <div id="app">
    <Menu />
    <CreateUser />
    <CreateTask />
    <ViewTasks />
  </div>
</template>

<script>
import Menu from "./components/Menu.vue";
import CreateUser from "./components/CreateUser.vue";
import CreateTask from "./components/CreateTask.vue";
import ViewTasks from "./components/ViewTasks.vue";

export default {
  name: "App",
  components: {
    Menu,
    CreateUser,
    CreateTask,
    ViewTasks,
  },
};
</script>

<style>
/* Add any necessary styles */
</style>
