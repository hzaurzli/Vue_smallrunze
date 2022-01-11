<template>
  <div></div>
</template>

<script>
  export default {
    data() {
      return {};
    },
    mounted() {
      const aa = this.$route.query;
      this.$router.push({name:'table',query:{id:aa}});
      console.log(aa)
    }
  };
</script>
