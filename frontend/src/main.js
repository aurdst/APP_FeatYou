import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import './assets/css/style.css'
import VuetifyGoogleAutocomplete from 'vuetify-google-autocomplete';

Vue.config.productionTip = false


Vue.use(VuetifyGoogleAutocomplete, {
  apiKey: 'AIzaSyDvxf-L2iOi4WteY3ber4wA0Gt-ljucLeA', 
  language: 'fr',
  installComponents: true,
  vueGoogleMapsCompatibility: false,
  country : 'France'
});

export const EventBus = new Vue();

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
