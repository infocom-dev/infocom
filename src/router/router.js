import Vue from 'vue'
import Router from 'vue-router'

import login from '../components/Login'
import register from '../components/Register'
import logout from '../components/Logout'
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
            component: login,
            meta: {
                requiresLogged: true
            }
        },
        {
            path: '/register',
            name: 'register',
            component: register,
            meta: {
                requiresLogged: true
            }
        },
        {
            path: '/logout',
            name: 'logout',
            component: logout,
            meta: {
                requiresAuth: true
            }
        }
    ]
})

export default router;