<template>
    <div id="app">
        <div id="main" style="width: 100%;height: 400px;"></div>
      <!--<div class="test" style="width: 100%;height: 400px;">-->
      <div id="for" v-for="(item,index) in opinionData.list" :key="index">
         <router-link :to="{path:'/route_ajax/',query: {name: index}}">
              <a>click:{{index}}</a><br>
          </router-link>
        <div :id="index" style="width: 100%;height: 400px;">

        </div>
      </div>
    </div>
</template>

<script>
import axios from "axios";
import *as echarts from 'echarts';

export default{
    data() {
        return {
            charts: '',
            opinionData: {}
        }
    },

    // beforeMount() {
    //   this.getData();
    // },

    updated(){
      this.for_do();
    },

    mounted() {
        this.getData();
    },

    methods: {
        getData() {
            axios.get('http://127.0.0.1:5000/vue/aa').then(response => {
                // console.log(response.data);
                this.opinionData =response.data;
                console.log(this.opinionData);

                // var roseCharts = document.getElementById('test');
            }).catch(function (error) {
              console.log(error);
            })
        },

        for_do() {
          for (var i = 0; i < this.opinionData.list.length; i++) {
                  var dat = this.opinionData.list[i].data;
                  // console.log(dat);
                  console.log(document.getElementById('0'));
                  console.log(document.getElementById('main'));
                  this.drawLine(i);
                }
        },

        drawLine(id) {
            this.charts = echarts.init(document.getElementById(id));
            this.charts.setOption({
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['近七日收益']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },

                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ["1","2","3","4","5"]
                },
                yAxis: {
                    type: 'value'
                },
                series: [{
                    name: '近七日收益',
                    type: 'line',
                    stack: '总量',
                    data: this.opinionData.list[id].data
                }]
            })
        },
    }
}
</script>
