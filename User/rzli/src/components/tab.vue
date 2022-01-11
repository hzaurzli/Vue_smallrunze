<template>
  <div>
    <h2>vue 动态组件实现tab切换加载不同的小模块</h2>
    <div>
      <a href="javascript:void(0)" @click="tabChange(goods)">第一项</a>
      <a href="javascript:void(0)" @click="tabChange(soso)">第二项</a>
      <a href="javascript:void(0)" @click="tabChange(bad)">第三项</a>
    </div>
    <!--
      动态地绑定到它的 is 特性，我们让多个组件可以使用同一个挂载点，并动态切换。
    -->
    <div :is="currentView"></div>
  </div>
</template>

<script>
  import goods from '@/components/goods';
  import soso from '@/components/soso';
  import bad from '@/components/bad';

  export default {
   data () {
     return {
       goods: 'goods',
       soso: 'soso',
       bad: 'bad',
       currentView: 'goods' // 默认选中第一项
     };
   },
   methods: {
     tabChange(tabItem) {
       this.currentView = tabItem;
     }
   },
   components: {
     goods,
     soso,
     bad
   }
 };
</script>
