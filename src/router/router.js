import Vue from 'vue'
import Router from 'vue-router'

// import SignIn from '../components/SignIn';
// import SignUp from '../components/SignUp';
import vQuestion from '../components/v-question.vue'
import vHomePage from '../components/v-home-page.vue'
Vue.use(Router);

import projects from '../components/projects';

import Login from '../components/Login';
import Register from '../components/Register';
import reject from '../components/reject'
import account from '../components/v-account-page'
import google_auth from '../components/Google-auth.vue'

import store from '../store';

const requireAuthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (!store.getters['auth/isAuthenticated']) {
                next('/login');
            } else {
                next();
            }
        });
};

const requireUnauthenticated = (to, from, next) => {
    store.dispatch('auth/initialize')
        .then(() => {
            if (store.getters['auth/isAuthenticated']) {
                next('/');
            } else {
                next();
            }
        });
};

const redirectLogout = (to, from, next) => {
    store.dispatch('auth/logout')
        .then(() => next('/'));
};

let router = new Router({
    saveScrollPosition: true,
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
            path: '/register',
            component: Register,
        },
        {
            path: '/login',
            component: Login,
            beforeEnter: requireUnauthenticated,
        },
        {
            path: '/reject',
            name: 'reject',
            component: reject,
            beforeEnter: requireAuthenticated,
        },
        {
            path: '/account',
            name: 'account',
            component: account,

        },
        {
            path: '/logout',
            name: 'logout',
            beforeEnter: redirectLogout,
        },
        {
            path: '/google',
            name: 'google',
            component: google_auth,
        },
        {
            path: '/account/projects',
            name: 'projects',
            component: projects,
        }
    ]
})

export default router;