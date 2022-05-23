import Vue from 'vue'
import Vuex from 'vuex'

const axios = require('axios');

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/v1/user/',
  headers: { 
    'Content-Type': 'Access-Control-Allow-Origin'
  }
})

Vue.use(Vuex)

export default new Vuex.Store({
  state    : {},
  getters  : {},
  mutations: {},
  actions  : {
    createAccount: ({commit}, userInfos) => {
      commit;
      console.log('test');

      instance.post('/create', userInfos).then(
        (response) => {
          console.log('OK');
          console.log(response);
        }
      ).catch(
        (error) => {
          console.log('K.O');
          console.log(error);
          console.log(userInfos);
        }
      );
    }
  },
  modules: {}
})