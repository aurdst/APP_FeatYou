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
      <h2>
        Hello text here ! So good 
      </h2>
      <p>
        Lorem impsum extrano torime ameno ameno latiré oh latiré ah torime 
      </p>
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
