<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
      <span v-if="isLoggedIn"> | <a @click="logout">Logout</a></span>

      <span v-else> | 
        <router-link to="/login">Login</router-link>
        </span>
      
|
      <router-link to="/register">Register</router-link> |
      <router-link to="/resources">Resources</router-link>
    </div>
    <router-view/>
  </div>
</template>


<script>
export default {
  computed: {
    isLoggedIn: function() {
      return this.$store.getters.isLoggedIn;
    }
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    }
  }
};
</script>
