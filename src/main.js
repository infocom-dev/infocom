import Vue from 'vue'
import App from './App.vue'
import store from './vuex/store'
import VueSlider from 'vue-slider-component'
import PrettyCheckbox from 'pretty-checkbox-vue';
import 'vue-slider-component/theme/default.css'
import 'pretty-checkbox/src/pretty-checkbox.scss';
 

Vue.component('VueSlider', VueSlider)
Vue.config.productionTip = false
Vue.use(PrettyCheckbox);
new Vue({
  render: h => h(App),
  store
}).$mount('#app')