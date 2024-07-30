<template>
  <div id="app">
    <MainLayout />
  </div>
</template>

<script>
import MainLayout from "./components/MainLayout.vue";

export default {
  name: "App",
  components: {
    MainLayout,
  },
};
</script>

<style>
/* Ensure the app fills the viewport */
html, body, #app {
  height: 100%;
  margin: 0;
  font-family: Arial, sans-serif;
  color: #333;
}

/* Center the MainLayout component */
#app {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #e9ecef;
}

/* Optional: Add a border or shadow to the MainLayout for visual appeal */
.main-layout {
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  overflow: hidden;
}
</style>
