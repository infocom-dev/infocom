import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from "./router/router";
import PrettyCheckbox from 'pretty-checkbox-vue';
// import 'vue-slider-component/theme/default.css'
import 'pretty-checkbox/src/pretty-checkbox.scss';
// import { BootstrapVue } from 'bootstrap-vue';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vuelidate from 'vuelidate'
Vue.use(BootstrapVue,BootstrapVueIcons);
Vue.use(Vuelidate);

import '@/plugins/apexcharts';

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import VueAxios from 'vue-axios';
Vue.config.productionTip = false
Vue.use(PrettyCheckbox);
axios.defaults.baseURL = process.env.VUE_APP_URL;
import store from './store';

Vue.use(VueAxios,axios)

new Vue({
  render: h => h(App),
  router,
  store,
  axios
}).$mount('#app')


