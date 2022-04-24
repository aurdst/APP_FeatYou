<template>
  <v-app>
    <v-app-bar
      app
      elevation="6"
    >
    <v-spacer/>
      <router-link to="/">
        <v-img :src="logo" max-width="150" class="ma-auto"></v-img>
      </router-link>
    <v-spacer/>
    
    <router-link to="/infos">
      <v-avatar
        color="primary"
        size="46"
      ></v-avatar>
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

        <router-link to="/">
            <v-avatar
            color="primary"
            size="40"
            ></v-avatar>
        </router-link>

        <v-spacer/>

          <router-link to="/conversation">
            <v-avatar
            color="primary"
            size="40"
            ></v-avatar>
          </router-link>

        <v-spacer/>

          <router-link to="/conseils">
            <v-avatar
            color="primary"
            size="40"
            ></v-avatar>
          </router-link>

        <v-spacer/>

          <router-link to="/profile">
            <v-avatar 
            color="primary"
            size="40"
            ></v-avatar>
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
    logo: require("@/assets/img/final.svg")
  }),
};
</script>
