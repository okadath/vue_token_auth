import Vue from 'vue'
import Router from 'vue-router'
import store from './store.js'
import Home from './views/Home.vue'
import About from './views/About.vue'
import Login from './components/auth/Login.vue'
import Register from './components/auth/Register.vue'
import Resource from './components/resources/Resources.vue'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/resources',
      name: 'resources',
      component: Resource,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    
    {
      path: '/about',
      name: 'about',
      component: About,
    }
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      console.log("store.getters.isLoggedIn");
      next()
      // .then(() => this.$router.push("/"))
      return
    }
    next('/login')
  } else {
    // console.log("store.getters.isLoggedIn");
    next()
  }
})


export default router