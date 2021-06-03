import Vue from 'vue'
import Router from 'vue-router'

import vHomePage from '../components/v-home-page.vue'
Vue.use(Router);

import projects from '../components/projects';

import Login from '../components/Login';
import Register from '../components/Register';
import Loading from '../components/Loading'
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
            path: '/register',
            component: Register,
        },
        {
            path: '/login',
            component: Login,
            beforeEnter: requireUnauthenticated,
        },
        {
            path: '/loading',
            name: 'loading',
            component: Loading,
            beforeEnter: requireAuthenticated,
        },

        {
            path: '/logout',
            name: 'logout',
            beforeEnter: redirectLogout,
        },
        {
            path: '/account/projects',
            name: 'projects',
            component: projects,
            beforeEnter: requireAuthenticated
        },
    ]
})

export default router;