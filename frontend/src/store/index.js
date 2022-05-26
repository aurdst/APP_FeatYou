import Vue from 'vue'
import Vuex from 'vuex'
import qs from "qs"
import router from "../router"; 

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

let user = localStorage.getItem('user');
if(!user) {
  user = {
    id          : -1,
    access_token: '',
    token_type  : '',
  } 
} else {
  try {
    user = JSON.parse(user);
    instance.defaults.headers.common['Authorization'] = user.access_token;
  } catch (error) {
    user = {
      id          : -1,
      access_token: '',
      token_type  : '',
    } 
  }
}

export default new Vuex.Store({
  state : {
      status: null,
      user: user,
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
      instance.defaults.headers.common['Authorization'] = user.access_token;
      state.user = user
      localStorage.setItem('user', JSON.stringify(user));
    },
    user: (state, info) => {
      state.user = info
    },
    logout: (state) => {
      state.user = {
        id: -1
      }
      localStorage.removeItem('user')
    },
  },

  actions  : {
    loginAccount: async function ({commit}, loginInfos) {
      commit('setStatus', 'loading');
      const response = await auth.post('/login', qs.stringify(loginInfos))
      if (response.status === 200) {
        commit('logUser', response.data)
        commit('setStatus', '');
        router.push('profile');
        return
      }
          
      commit('setStatus', 'failed_log');
      console.log('Connection Failed');
      //TODO Gerer erreur
    },
    createAccount: ({commit}, userInfos) => {
      return new Promise((resolve, reject) => {
        commit;
        
        instance.post('/create', userInfos).then(
          (response) => {
            commit('logUser', response.data)
            commit('setStatus', 'created');
            resolve(response);
            router.push('profile');
            return
          }
        ).catch(
          (error) => {
            commit('setStatus', 'failed_create');
            reject(error);
          }
        );
      })
    },
    getUserInfos: async function ({commit}) {
      const response = await instance.get(`/infos/${JSON.parse(localStorage.user).user.id}`)
      commit('user', response.data);
      return response;
    },
  },
  modules: {}
})