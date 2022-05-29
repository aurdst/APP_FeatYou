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
});

const auth = axios.create({
  baseURL: 'http://localhost:8000/api/v1/auth/',
  headers: { 
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/x-www-form-urlencoded'
  }
});

Vue.use(Vuex);

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

let alluser = localStorage.getItem('alluser');
if(!alluser) {
  alluser = {
    id          : -1,
    access_token: '',
    token_type  : '',
  } 
} else {
  try {
    alluser = JSON.parse(alluser);
  } catch (error) {
    alluser = {
      firstName    : "",
      lastName     : "",
      isadmin      : false,
      phone        : "",
      adress       : "",
      email        : "",
      postalCode   : 59999,
      banqCardNumb : 0,
      dateRegister : "2022-05-24T09: 31: 50.950885",
      pict         : null
    } 
  }
}

export default new Vuex.Store({
  state : {
      status  : null,
      user    : user,
      alluser : alluser
  },

  getters : {
    isAuth    : state => !!state.user,
    stateUser : state => state.user
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

    update : (state, user) => {
      state.user = user
      let u      = JSON.parse(localStorage.getItem('user'));
      u.user     = user;
      localStorage.setItem('user', JSON.stringify(u));
    }
  },

  actions : {
    loginAccount : async function ({commit}, loginInfos) {
      commit('setStatus', 'loading');

      await auth.post('/login', qs.stringify(loginInfos)).then(
        (response) => {
          if (response.status === 200) {
            commit('logUser', response.data)
            commit('setStatus', '');
            router.push('profile');
    
            return;
          }
        }
      ).catch(
        () => {
          commit('setStatus', 'failed_log');
          return;
        }
      );
    },

    createAccount : ({commit}, userInfos) => {
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

    getUserInfos : async function ({commit}) {
      const response = await instance.get(`/infos/${JSON.parse(localStorage.user).user.id}`)
      commit('user', response.data);
      return response;
    },

    getAllUserInfos : async function ({commit}) {
      const response = await instance.get('/getall')
      commit('alluser', response.data);
      return response;
    },

    putUser : async function({commit}, infos) {
      const rs = await instance.put(`/update/${JSON.parse(localStorage.user).user.id}`, infos).then(
        (response) => {
          commit('update', response.data);
          return "Your account has been modified successfully";
        }
      ).catch(
        (error) => {
          throw new Error(JSON.parse(error.request.response).detail, error.message, 401);
        }
      );

      return rs;
    }
  },

  modules: {}
});