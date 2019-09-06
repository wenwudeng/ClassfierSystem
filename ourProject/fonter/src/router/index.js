import Vue from 'vue'
import Router from 'vue-router'
import test from '@/components/dataTest'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: () => import('@/components/login')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/components/login')
    },
    {
      path: '/home',
      name: 'home',
      component: () => import('@/components/home')
    },
    {
      path: '/test',
      name: 'home',
      component: test
    }
  ]
})
