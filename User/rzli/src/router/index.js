import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import click_ajax from '@/components/click_ajax'
import echarts_not from '@/components/echart_not'
import vueechart from '@/components/vueechart'
import route_ajax from '@/components/route_ajax'
import tab from '@/components/tab'
import click_echart from '@/components/click_echart'
import table from '@/components/table'
import search from '@/components/search'
import emit from '@/components/emit'
import on from '@/components/on'

Vue.use(Router);
const originalPush = Router.prototype.push;
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
};

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/click_ajax/',
      name: 'click_ajax',
      component: click_ajax
    },
    {
      path: '/echarts_not',
      name: 'echarts_not',
      component: echarts_not
    },
    {
      path: '/vueechart',
      name: 'vueechart',
      component: vueechart
    },
    {
      path: '/route_ajax',
      name: 'route_ajax',
      component: route_ajax
    },
    {
      path: '/tab',
      name: 'tab',
      component: tab
    },
    {
      path: '/click_echart',
      name: 'click_echart',
      component: click_echart
    },
    {
      path: '/table',
      name: 'table',
      component: table
    },
    {
      path: '/search',
      name: 'search',
      component: search
    },
    {
      path: '/emit',
      name: 'emit',
      component: emit
    },
    {
      path: '/on',
      name: 'on',
      component: on
    },
  ]
})
