import Vue from 'vue';
import Vuex from 'vuex';
import createLogger from 'vuex/dist/logger';

import auth from './auth';
import signup from './signup';

const debug = process.env.NODE_ENV !== 'production';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    signup,
  },
  strict: debug,
  plugins: debug ? [createLogger()] : [],
});