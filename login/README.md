# test CRUD

## test login&CRUD Vue-Buefy

crear el proyecto, creo el entorno dos

```bash
yarn init
yarn add @vue/cli
yarn vue create login
cd login/

yarn add @vue/cli
yarn add buefy axios vuex
yarn vue --version
yarn serve
```

separamos el script de consumo de la api `APIService.js`:

```js
import axios from "axios";
const API_URL = "https://www.glsteamedition.com/v0";
export class APIService {
  // https://www.glsteamedition.com/v0/media/GET/video/Bend%20the%20Curve/
  constructor() {}

  async getContacts() {
    const url = `${API_URL}/media/GET/video/Bend%20the%20Curve/`;
    const response = await axios.get(url);
    console.log(response.data);
    return response.data;
  }
}
```

y luego creamos al componente a llamar `ListContacts.vue`:

```vue
<template>
  <div>
    asdasdasaaa
    <h1>Contacts ()</h1>

    <!-- si no usamos el key podemos inicializar con {} -->
    <div v-bind="data"></div>
    <p>{{ data.title }}</p>
    <p>{{ data.subtitles_suported }}</p>
    <!-- <p >{{data.featured}}</p> -->
    <p>{{ data.video_uri }}</p>
  </div>
</template>

<script>
import { APIService } from "./APIService";
const apiService = new APIService();
export default {
  name: "ListContacts",

  components: {},

  data() {
    return {
      data: {},
      title: "",
    };
  },

  methods: {
    getContacts() {
      apiService.getContacts().then((data) => {
        this.data = data;
      });
    },
  },

  mounted() {
    this.getContacts();
  },
};
</script>

```

para ejecutar la app con Buefy usando otro componente como main(creo que da igual) `App.vue`:

```js
import Vue from "vue";
// import App from './App.vue'
import ListContacts from "./ListContacts.vue";
Vue.config.productionTip = false;

import Buefy from "buefy";
import "buefy/dist/buefy.css";

new Vue({
  render: (h) => h(ListContacts),
}).$mount("#app");

Vue.use(Buefy);
```