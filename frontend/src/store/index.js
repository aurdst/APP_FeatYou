import Vue from 'vue'
import Vuex from 'vuex'

const axios = require('axios');

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/v1/user/',
  headers: { 
    'Content-Type': 'application/json'
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
      console.log(console.log(userInfos));
      instance.post('/create', userInfos).then(
        (response) => {
          console.log(response);
        }
      ).catch(
        (error) => {
          console.log(error.response);
          console.log(userInfos);
        }
      );
    }
  },
  modules: {}
})