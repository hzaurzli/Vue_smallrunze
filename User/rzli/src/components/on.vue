<template>
	<div>
		组件A
		<h2>{{ data }}</h2>
	</div>
</template>

<script>
export default {
	name: 'comA',
	data() {
		return {
			data: ''
		}
	},
	methods: {},
	mounted() {
		this.$bus.$on('sendToA', data => {
			this.data = data;
      console.log(this.data)
		})
	}
}
</script>
