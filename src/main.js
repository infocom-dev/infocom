import Vue from 'vue'
import App from './App.vue'
import store from './vuex/store'
// import VueSlider from 'vue-slider-component'
import PrettyCheckbox from 'pretty-checkbox-vue';
import 'vue-slider-component/theme/default.css'
import 'pretty-checkbox/src/pretty-checkbox.scss';
// import Multiselect from 'vue-multiselect'

// Vue.component('VueSlider', VueSlider)
// Vue.component('vue-multiselect', window.VueMultiselect.default)
Vue.config.productionTip = false
Vue.use(PrettyCheckbox);

new Vue({
  render: h => h(App),
  store
}).$mount('#app')