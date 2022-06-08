<template>
    <v-row
      class="mb-6 mx-auto" no-gutters
    >
        <v-col cols="12" v-if="iscoach == false">
          <p class="p_choose">Choissez votre sport :</p>
        </v-col>
        
        <br>
        <br>

        <v-col cols="3"
          class="mx-auto"
          v-if="iscoach == false"
        >
          <router-link to="/musculation">
            <CardsMuscu/>
          </router-link>
        </v-col>

        <v-col cols="3"
          class="mx-auto"
          v-if="iscoach == false"
        >
          <router-link to="/crossfit">
            <CardsCroosfit/>
          </router-link>
        </v-col>

        <v-col cols="3"
          class="mx-auto"
          v-if="iscoach == false"
        >
          <router-link to="/step">
            <CardsStep/>
          </router-link>

        </v-col>

        <v-col cols="12" class="mt-5" v-if="iscoach == false">
          <router-link to="categorie">
            <div class="btn_view_sport">
              <p solo class="mb-5 btn_seance">
                Voir nos cours
              </p>
            </div>
          </router-link>
        </v-col>

      <v-row no-gutters>
        <v-col cols="12" v-if="iscoach == true">
          <br>
          <h2 class="title_home">Bonjour {{current_user_name}}</h2>
          <br>
          <CreateEvent/>
        </v-col>
      </v-row>

      <v-row no-gutters>
        <v-col cols="12">
          <v-dialog v-model="confirm">
            <v-alert
              type="success"
            >Vôtre événement est créer !</v-alert>
          </v-dialog>
        </v-col>
      </v-row>


    <div class="container_current_event mx-auto">
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

    <v-row no-gutters  v-if="iscoach == false">
      <v-col class="mb-6">
        <List/>
      </v-col>
    </v-row>
  </v-row>
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

    data: () => ({
      current_user_name: JSON.parse(localStorage.getItem('user')).user.username,
      iscoach : JSON.parse(localStorage.getItem('user')).user.iscoach,
      confirm : false,
    })
  }
</script>
