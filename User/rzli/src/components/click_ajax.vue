<template>
  <div id="app">
    <p>
      <button @click="click()">click</button>
    </p>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
  data(){
    return {
      opinionData: []
    }
  },
  methods:{
    click(){
      axios.get('http://127.0.0.1:5000/json').then(response => {
                // console.log(response.data);
                this.opinionData =response.data;
                console.log(this.opinionData);
            }).catch(function (error) {
              console.log(error);
            })
    }
  },

  mounted(){
    // this.click();
  },

  created(){
      console.log(this.$route.query)
  }
}
</script>
