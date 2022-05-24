import Vue from 'vue'
import Vuex from 'vuex'
import qs from "qs"

const axios = require('axios');

const instance = axios.create({
  baseURL: 'http://localhost:8000/api/v1/user/',
  headers: { 
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json'
  }
})

const auth = axios.create({
  baseURL: 'http://localhost:8000/api/v1/auth/',
  headers: { 
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/x-www-form-urlencoded'
  }
})

Vue.use(Vuex)

export default new Vuex.Store({
  state    : {
      status: null,
      user: {
        id: -1,
        access_token: '',
      }
  },
  getters  : {
    isAuth: state => !!state.user,
    stateUser: state => state.user
  },
  mutations: {
    setStatus: (state, status) => {
      state.status = status
    },
    logUser: (state, user) => {
      state.user = user
    }
  },
  actions  : {
    loginAccount: ({commit}, userInfos) =>{
      commit('setStatus', 'loading');
      return new Promise((resolve, reject) => {
        auth.post('/login', qs.stringify(userInfos)).then(
          (response) => {
            commit('setStatus', '');
            commit('logUser', response.data.user);
            this.$router.push('profile');
          }
        ).catch(
          (error) => {
            commit('setStatus', 'failed_log');
            reject(error);
          }
        );
      })
    },
    createAccount: ({commit}, userInfos) => {
      return new Promise((resolve, reject) => {
        commit;
  
        instance.post('/create', userInfos).then(
          (response) => {
            commit('setStatus', 'created');
            resolve(response);
          }
        ).catch(
          (error) => {
            commit('setStatus', 'failed_create');
            reject(error);
          }
        );
      })
    }
  },
  modules: {}
})