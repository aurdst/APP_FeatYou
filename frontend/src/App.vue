<template>
  <v-app>
    <v-app-bar
      app
      elevation="6"
    >
    <v-spacer/>
      <router-link to="/home">
        <v-img :src="logo" max-width="150" class="ma-auto"></v-img>
      </router-link>
    <v-spacer/>
    
    <router-link to="/infos">
      <v-avatar
        size="46"
      >
        <img
          :src="icon_faq"
          alt="faq"
        >   
      </v-avatar>
    </router-link>
    
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
      <v-app-bar
      app
      elevation="6"
      bottom
      >
        <v-spacer/>

        <router-link to="/home">
            <v-avatar
            size="45"
            >
            <img
              :src="icon_home"
              alt="home"
            >   
            </v-avatar>
        </router-link>

        <v-spacer/>

          <router-link to="/conseils">
            <v-avatar
            size="45"
            >
            <img
              :src="icon_conseil"
              alt="conseils"
            >   
            </v-avatar>
          </router-link>

        <v-spacer/>

          <router-link to="/conversation">
            <v-avatar
            size="45"
            >
            <img
              :src="icon_messag"
              alt="message"
            >   
            </v-avatar>
          </router-link>

        <v-spacer/>

          <router-link to="/profile">
            <v-avatar 
            size="45"
            >
            <img
              :src="icon_profile"
              alt="profile"
            >         
            </v-avatar>
          </router-link>

        <v-spacer/>
    </v-app-bar>
  </v-app>
</template>

<script>
import NavBottom from './components/NavBottom.vue'

export default {
  name: 'App',

  component:{
    NavBottom
  },

  data: () => ({
    logo: require("@/assets/img/logo.png"),
    icon_profile: require("@/assets/img/icone_profile.png"),
    icon_home: require("@/assets/img/icon_home.png"),
    icon_messag: require("@/assets/img/icon_message.png"),
    icon_conseil: require("@/assets/img/icon_conseil.png"),
    icon_faq: require("@/assets/img/icon_faq.png"),
  }),
};
</script>
