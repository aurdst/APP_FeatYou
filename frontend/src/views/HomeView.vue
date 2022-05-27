<template>
  <div>
    <v-row
      class="mb-6 mx-auto"
    >   
      <v-col cols="12">
        <Carrousel to="/conseils"/>
      </v-col>
      <v-col cols="4">
        <router-link to="/sport">
          <Cards/>
        </router-link>
      </v-col>

      <v-col cols="4">
        <Cards/>
      </v-col>

      <v-col cols="4">
        <Cards/>
      </v-col>
    </v-row>

    <v-row class="mb-6 mx-5">
      <v-col cols="12">
        <h2 class="text-center bg_home_seance">
          Séances à venir 
        </h2>
      </v-col>

      <v-col cols="12">
        <p class="text-center">
          {{}} 
        </p>
      </v-col>

      <v-col cols="12">
        <p class="text-center btn_seance">
          Voir toutes mes séances 
        </p>
      </v-col>
    </v-row>

    <v-row class="mb-6 mx-5">
      <List/>
    </v-row>
  </div>
</template>

<script>
  import Carrousel from '../components/CarrouselView'
  import Cards from '../components/CardsSportView.vue'
  import List from '../components/ListCoachView.vue'

  export default {
    name: 'HomeView',

    components: {
      Carrousel, Cards, List
    },
  }
</script>
