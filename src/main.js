import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from "./router/router";
import store from './store/store'

import PrettyCheckbox from 'pretty-checkbox-vue';
// import 'vue-slider-component/theme/default.css'
import 'pretty-checkbox/src/pretty-checkbox.scss';
import { BootstrapVue } from 'bootstrap-vue';

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vuelidate from 'vuelidate'

Vue.use(BootstrapVue);
Vue.use(Vuelidate);

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
import VueAxios from 'vue-axios';


Vue.config.productionTip = false
Vue.use(PrettyCheckbox);
axios.defaults.baseURL = process.env.VUE_APP_URL;

// require('@/assets/styles/fonts.scss')
Vue.use(VueAxios,axios)


router.beforeEach((to, from, next) => {
  // if any of the routes in ./router.js has a meta named 'requiresAuth: true'
  // then check if the user is logged in before routing to this path:
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.loggedIn) {
      next({ name: 'login' })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.requiresLogged)) {
    // else if any of the routes in ./router.js has a meta named 'requiresLogged: true'
    // then check if the user is logged in; if true continue to home page else continue routing to the destination path
    // this comes to play if the user is logged in and tries to access the login/register page
    if (store.getters.loggedIn) {
      next({ name: 'home' })
    } else {
      next()
    }
  } else {
    next()
  }
})

new Vue({
  render: h => h(App),
  router,
  store,
  axios
}).$mount('#app')