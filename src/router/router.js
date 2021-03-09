import Vue from 'vue'
import Router from 'vue-router'

import SignIn from '../components/SignIn';
import SignUp from '../components/SignUp';
import vQuestion from '../components/v-question.vue'
import vHomePage from '../components/v-home-page.vue'
Vue.use(Router);

let router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: vHomePage

        },
        {
            path: '/anketa',
            name: 'anketa',
            component: vQuestion,
            props: true
        },
        {
            path: '/login',
            name: 'login',
            component: SignIn,
        },
        {
            path: '/register',
            name: 'register',
            component: SignUp,
        },
    ]
})

export default router; 