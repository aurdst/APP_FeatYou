<template>
  <v-app>
    <v-app-bar
      app
      elevation="6"
    >
      <v-img :src="logo" max-width="150" class="ma-auto"></v-img>
      <!-- <v-spacer/> -->
      <v-avatar
        color="primary"
        size="46"
      ></v-avatar>
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
        <v-avatar
          color="primary"
          size="40"
        ></v-avatar>
      <v-spacer/>
        <v-avatar
        color="primary"
        size="40"
        ></v-avatar>
      <v-spacer/>
        <v-avatar 
        color="primary"
        size="40"
        ></v-avatar>
      <v-spacer/>
    </v-app-bar>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    logo: require("@/assets/img/final.svg")
  }),
};
</script>
