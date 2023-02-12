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
  // 定义全局搜索,定义个空组件 search.vue,然后由 search.vue 返回本组件,这样如果位于 table 页面,则进入空组件 search.vue,然后返回 table 页面，类似于刷新;
  // 如果是其他页面搜索则跳转为 table 页面
  methods:{
    click(){
      var path = '/table';
      if (path == this.$route.path) {
        // this.$refs.getValue.value获取input搜索框的值
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
