<template>
  <div>
    <v-row
      class="mb-6 mx-auto" no-gutters
    >   
      <v-col cols="12">
        <p class="p_choose">Choissez votre sport :</p>
      </v-col>
      <br>
      <v-col cols="3"
        class="mx-auto"
      >
        <router-link to="/musculation">
          <CardsMuscu/>
        </router-link>
      </v-col>

      <v-col cols="3"
        class="mx-auto"
      >
        <router-link to="/crossfit">
          <CardsCroosfit/>
        </router-link>
      </v-col>

      <v-col cols="3"
        class="mx-auto"
      >
        <router-link to="/step">
          <CardsStep/>
        </router-link>
      </v-col>
    </v-row>

    <router-link to="categorie">
      <div class="btn_view_sport">
        <p solo class="mb-5 btn_seance">
          Voir nos cours
        </p>
      </div>
    </router-link>
    
    <CreateEvent/>
    <div class="container_current_event">
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
    </div>
      <v-row class="mb-6" fluid no-gutters>
        <List/>
      </v-row>
  </div>
</template>

<script>
  import CardsMuscu from '../components/CardsMuscu.vue'
  import List from '../components/ListCoachView.vue'
  import CreateEvent from '../components/CreateEvent.vue'
  import CardsCroosfit from '@/components/CardsCroosfit.vue'
  import CardsStep from '@/components/CardsStep.vue'

  export default {
    name: 'HomeView',

    components: {
    CardsMuscu,
    List,
    CreateEvent,
    CardsCroosfit,
    CardsStep
},
  }
</script>
