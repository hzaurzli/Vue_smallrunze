<template>
  <div id="app">
    <div>
      <input ref="getValue" type="text"/>
      <button type="button" @click="click">搜索</button>
    </div>
    <div>
      <img src="./assets/logo.png">
      <router-link  to="/">test</router-link>|
      <router-link  to="/click_ajax">click_ajax</router-link>|
      <router-link  to="/echarts_not">echarts_not</router-link>|
      <router-link  to="/vueechart">vueechart</router-link>|
      <router-link  to="/tab">tab</router-link>|
      <router-link  to="/click_echart">click_echart</router-link>|
      <router-link  to="/table">table</router-link>|
      <!--<router-link  to="/search">search</router-link>|-->
      <router-link  to="/emit">emit</router-link>|
      <router-link  to="/on">on</router-link>|
    </div>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data(){
    return{
      Ative:true
    }
  },

  methods:{
    click(){
      var path = '/table';
      if (path == this.$route.path) {
        var aa = this.$refs.getValue.value;
        this.$router.push({name:'search',query:aa});
      }
      else {
        var aa = this.$refs.getValue.value;

        this.$router.push({name:'table',query: {id:aa}})
      }
    },
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
