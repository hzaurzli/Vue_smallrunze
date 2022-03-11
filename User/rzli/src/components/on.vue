<template>
	<div id="app">
		组件A
		<h2>{{ data }}</h2>
    <div v-html="word"></div>
    <div>
      <img :src= "img">
    </div>
    <!--利用v-show来控制是否添加loading效果，v-show不需要绑定事件-->
    <div v-show="is">
      <img src="../assets/loader.gif">
    </div>
	</div>
</template>

<script>
export default {
	name: 'comA',
	data() {
		return {
			data: '',
      word:'',
      img: '',
      is: true
		}
	},
	methods: {},
  // 设置this.word添加html文本代码
  created(){
	  this.is = false;
	  console.log(this.is);
	  var word = '<p>aaaaa</p>';
	  this.word = word;
	  // this.is = false;
	  this.img = "http://localhost:8080/src/assets/logo.png";
	  console.log(word);
  },
	mounted() {
	  this.word = '';
	  this.img = '';
		this.$bus.$on('sendToA', data => {
			this.data = data;
      console.log(this.data)
		})
	}
}
</script>
