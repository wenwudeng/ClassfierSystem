// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/css/main.css'
import '@/assets/css/scrollbar.css'
import VueParticles from 'vue-particles'

import VCharts from 'v-charts'


Vue.use(VCharts)

Vue.use(VueParticles)

Vue.config.productionTip = false
Vue.use(ElementUI);

//axios赋值给http
// Vue.prototype.$http = axios
// Vue.prototype.$url = 'http://127.0.0.1:8000/'

// 设置反向代理，前端请求默认发送到 http://localhost:8087/api
var axios = require('axios')
axios.defaults.baseURL = 'http://127.0.0.1:8000/'
// 全局注册，之后可在其他组件中通过 this.$axios 发送数据
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


