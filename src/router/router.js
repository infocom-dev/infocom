import Vue from 'vue'
import Router from 'vue-router'

import vQuestion from '../components/v-question.vue'
import vHomePage from '../components/v-home-page.vue'
Vue.use(Router);

let router = new Router({
    routes:[
        {
            path :'/',
            name : 'home',
            component:vHomePage

        },
        {
            path : '/anketa',
            name : 'anketa',
            component : vQuestion,
            props : true
        }
    ]
})

export default router; 