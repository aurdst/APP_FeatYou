<template>
  <div>
    <v-row
      class="mb-6 mx-auto" no-gutters
    >   
      <v-col cols="12">
        <Carrousel to="/conseils"/>
      </v-col>
      <v-col cols="3"
        class="mx-auto"
      >
        <router-link to="/sport_details">
          <Cards/>
        </router-link>
      </v-col>

      <v-col cols="3"
        class="mx-auto"
      >
        <Cards/>
      </v-col>

      <v-col cols="3"
        class="mx-auto"
      >
        <Cards/>
      </v-col>
    </v-row>

    <router-link to="sport">
      <div class="btn_view_sport">
        <v-btn solo class="mb-5 btn_log ">
          Voir tout les sports
        </v-btn>
      </div>
    </router-link>
    
    <CreateEvent/>

    <v-row class="mb-6 mx-5" no-gutters>
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

    <v-row class="mb-6" fluid no-gutters>
      <List/>
    </v-row>
  </div>
</template>

<script>
  import Carrousel from '../components/CarrouselView'
  import Cards from '../components/CardsSportView.vue'
  import List from '../components/ListCoachView.vue'
  import CreateEvent from '../components/CreateEvent.vue'

  export default {
    name: 'HomeView',

    components: {
      Carrousel, Cards, List, CreateEvent
    },
  }
</script>
