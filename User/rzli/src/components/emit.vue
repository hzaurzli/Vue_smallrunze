<template>
	<div>
		组件B
		<button @click="send">发送</button>
	</div>
</template>

<script>
export default {
	name: 'comB',
	data() {
		return {
			data: '组件B里的数据'
		}
	},
	methods: {
		send() {
			this.$bus.$emit('sendToA', this.data)
		}
	}
}
</script>
