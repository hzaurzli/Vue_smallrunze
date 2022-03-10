<template>
	<div id="app">
		组件A
		<h2>{{ data }}</h2>
    <div v-html="word"></div>
    <div>
      <img :src= "img">
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
      img: ''

		}
	},
	methods: {},
  // 设置this.word动态loading效果
  created(){
	  var word = '<p>aaaaa</p>';
	  this.word = word;
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
