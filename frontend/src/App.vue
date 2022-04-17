<template>
  <v-app>
    <v-app-bar
      app
      elevation="4"
    >
      <v-img :src="logo" max-width="100" class="ma-auto"></v-img>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
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
