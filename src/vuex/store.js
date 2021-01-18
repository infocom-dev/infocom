import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios';

Vue.use(Vuex);

let store = new Vuex.Store({
    state:{ 
        questions:[]
    },
    mutations:{
        'SET_QUESTIONS_TO_STATE' : (state,questions)=>{
            state.questions = questions;
        }
    },
    actions:{
        GET_QUESTIONS_FROM_API({commit}) {
            return axios('http://45.90.216.173/api/hello/', {
                method:"GET"
            })
            .then((questions)=>{
                commit('SET_QUESTIONS_TO_STATE',questions.data);
                return questions;
            })
            .catch((error)=>{
                console.log(error);
                return error;
            })

        }
    },
    getters:{
        QUESTIONS(state){
        return state.questions;
    }}

});

export default store;