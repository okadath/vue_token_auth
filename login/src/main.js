import Vue from "vue";
// import App from './App.vue'
import ListContacts from "./ListContacts.vue";
Vue.config.productionTip = false;

import Buefy from "buefy";
import "buefy/dist/buefy.css";

// import { router } from './router';
// import store from './store';


new Vue({
  // router,
  // store, 
  render: (h) => h(ListContacts),
}).$mount("#app");

Vue.use(Buefy);
