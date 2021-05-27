import auth from '../api/auth';

import {
  REGISTRATION_BEGIN,
  REGISTRATION_CLEAR,
  REGISTRATION_FAILURE,
  REGISTRATION_SUCCESS,
} from './types';

export default {
  namespaced: true,
  state: {
    registrationCompleted: false,
    registrationError: false,
    registrationLoading: false,
    errror : "",
  },
  actions: {
    createAccount({ commit }, {  password1, password2, email,phone }) {
      commit(REGISTRATION_BEGIN);
      console.log("sss")
        return auth.createAccount( password1, password2, email,phone)
        .then(() => commit(REGISTRATION_SUCCESS))
        .catch(() => commit(REGISTRATION_FAILURE));
    },
    clearRegistrationStatus({ commit }) {
      commit(REGISTRATION_CLEAR);
    },
  },
  mutations: {
    [REGISTRATION_BEGIN](state) {
      state.registrationLoading = true;
    },
    [REGISTRATION_CLEAR](state) {
      state.registrationCompleted = false;
      state.registrationError = false;
      state.registrationLoading = false;
    },
    [REGISTRATION_FAILURE](state) {
      state.registrationError = true;
      state.registrationLoading = false;
    },
    [REGISTRATION_SUCCESS](state) {
      state.registrationCompleted = true;
      state.registrationError = false;
      state.registrationLoading = false;
    },
  },
};