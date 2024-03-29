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

const instanceEvent = axios.create({
  baseURL: 'http://localhost:8000/api/v1/events/',
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

let event = localStorage.getItem('event');
if(!event) {
  event = {
    id: null,
    label: '',
    sport: '',
    description: '',
    idUser: '',
    date: '',
    hours: '',
    lieu: '',
    price : 0.0,
    listOfParticipant: '[]'
    }
  }else {
    try {
      allcoachs = JSON.parse(allcoachs);
    } catch (error) {
      event = {
        id: null,
        label: '',
        sport: '',
        description: '',
        idUser: '',
        date: '',
        hours: '',
        lieu: '',
        price : 0.0,
        listOfParticipant: '[]'
        } 
    }
  }

  let allcoachs = localStorage.getItem('allcoachs');
  if(!allcoachs) {
    allcoachs = {
      firstName    : "",
      lastName     : "",
      isadmin      : false,
      iscoach      : null,
      phone        : "",
      adress       : "",
      email        : "",
      postalCode   : 0,
      banqCardNumb : 0,
      dateRegister : "",
      pict         : null,
      coin         : 0
    }
} else {
  try {
    allcoachs = JSON.parse(allcoachs);
  } catch (error) {
    allcoachs = {
      firstName    : "",
      lastName     : "",
      isadmin      : false,
      iscoach      : null,
      phone        : "",
      adress       : "",
      email        : "",
      postalCode   : 0,
      banqCardNumb : 0,
      dateRegister : "",
      pict         : null,
      coin         : 0
    } 
  }
}

export default new Vuex.Store({
  state : {
      status    : null,
      user      : user,
      allcoachs : allcoachs,
      // coach : coach
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

    event: (state, event)=> {
      state.event = event
      localStorage.getItem('event');
    },

    allcoachs: (state, allcoachs) => {
      state.allcoachs = allcoachs
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
    },

    update_current_user_coin : (state, ammount) => {
      let user = JSON.parse(localStorage.getItem('user'))
      user.user.coin = ammount;

      state.user = user
      localStorage.setItem('user', JSON.stringify(user));
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
        (err) => {
          console.log(err)
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

    getEventInfos : async function ({commit}) {
      const response = await instanceEvent.get('/get_all')
      commit('event', response.data);
      return response;
    },

    getEvents : async function ({commit}, sport) {
      const response = await instanceEvent.get(`/events/${sport}`);
      commit('event', response.data);
      return response;
    },
    
    getEventbyUserId : async function ({commit}, id) {
      const response = await instanceEvent.get(`by_user/${id}`)
      commit;
      if (response == 200) {
        this.not_coach = true;
      }
      return response;
    },

    createEvent : async function({commit}, eventInfo) {
      console.log(eventInfo)
      const rs = await instanceEvent.post('create_event', eventInfo).then(
        (response) => {
          commit('event', response.data);
          console.log(response.data)
          this.dialog = false;
          this.confirm = true;
          return response;
        }
      );
      
      return rs;
    },

    getAllUserInfos : async function ({commit}) {
      const response = await instance.get('/get_coachs')

      for (let i = 0; i < response.data.length; i++) {
        response.data[i].lieux = JSON.parse(response.data[i].lieux);
        response.data[i].sport = JSON.parse(response.data[i].sport);
      }

      commit('allcoachs', response);
      return response.data;
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
    },

    getCoachById : async function({commit}, id) {
      const response = await instance.get(`/coach/${id}`);
      response.data.lieux = JSON.parse(response.data.lieux);
      response.data.sport = JSON.parse(response.data.sport);

      commit;
      return response;
    },

    manage_coin : async function({commit}, datas) {
      const response = await instance.put('/manage_coin', datas);
      console.log(response)
      commit('update_current_user_coin', response.data);

      return response
    },

    manage_participant : async function({commit}, datas) {
      const response = await instanceEvent.put('/manage_paricipant', datas);
      console.log(response)
      commit('update_current_user_coin', response.data);

      return response
    }
  }
});