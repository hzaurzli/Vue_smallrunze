<template>
  <div id="app">
    <p>
      后台传值
    </p>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
  data(){
    return {
      opinionData: [],
      param : ''
    }
  },
  methods:{
    route_ajax(){
      axios.get('http://127.0.0.1:5000/route_ajax/'+this.param.name).then(response => {
                // console.log(response.data);
                this.opinionData =response.data;
                console.log(this.opinionData);
            }).catch(function (error) {
              console.log(error);
            })
    }
  },

  mounted(){
    this.route_ajax();
  },

  created(){
      this.param = this.$route.query;
      console.log(this.param);
  }
}
</script>
