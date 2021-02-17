import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from "./router/router";

import PrettyCheckbox from 'pretty-checkbox-vue';
// import 'vue-slider-component/theme/default.css'
import 'pretty-checkbox/src/pretty-checkbox.scss';

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'


Vue.config.productionTip = false
Vue.use(PrettyCheckbox);
axios.defaults.baseURL = process.env.VUE_APP_URL;

// require('@/assets/styles/fonts.scss')


new Vue({
  render: h => h(App),
  router
}).$mount('#app')