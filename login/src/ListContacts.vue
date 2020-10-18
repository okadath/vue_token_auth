<template>
  <div>
    asdasdasaaa
    <h1>Contacts ()</h1>

    <!-- si no usamos el key podemos inicializar con {} -->
    <div v-bind="data">
     <b-button @click="clickMe(data.title)">{{ data.title }}</b-button>
    <!-- <p>{{ data.subtitles_suported }}</p> -->

    <!-- <p >{{data.featured}}</p> -->
    <p>{{ data.video_uri }}</p>
</div>
    <div>

        <b-message v-bind="error" v-if="error" title="Danger" type="is-danger" aria-close-label="Close message">
{{ error }}
        </b-message>




  <form v-on:submit.prevent="postGetToken">
          <label for="name">Nombre</label>
    <input
      id="name"
      v-model="post.code"
      type="text"
      name="name"
    >
<button class="btn btn-primary">Submit</button>
      </form>

    <div v-bind="d_post" v-if="d_post" >   
       <!-- <p>{{ d_post }}</p> -->
       <p>{{ d_post.access }}</p>
</div>

    </div>
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
      post:{},
      error:"", 
      d_post:{},
    };
  },

  methods: {
    getContacts() {
      apiService.getContacts().then((data) => {
        this.data = data;
      });
    },

    postGetToken() {
      apiService.createToken(this.post).then((data) => {
        // this.data = data;
        console.log(this.post);
        console.log(this.post.code);
        console.log(data);
        this.error = "";
        this.d_post=data
      })
      .catch(error => {
        this.error = error;
        console.log('There was an error!', error.response.data);
      });


    },

    clickMe(asd) {
      this.$buefy.notification.open(asd)
    },

  },

  mounted() {
    this.getContacts();
    // this.postGetToken()
  },
};
</script>
