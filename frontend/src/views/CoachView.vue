<template>
  <v-container>
    <v-row no-gutters class="text_coach">
      <v-row no-gutters>
        <v-col cols="12">
          <v-avatar>
            <v-img :src="test" width="50"></v-img>
          </v-avatar>
        </v-col>
        <v-col cols="10" class="container_infos mx-auto mt-5 pa-2">
          <v-col cols="12" class="cols_12">
            <h4>{{this.coach.firstName + ' ' + this.coach.lastName}}</h4>
          </v-col>
          
          <v-col cols="12" class="cols_12">
            <div :key="index" v-for="(item, index) in this.coach.sport" class="container_sport">
              <p>{{ item }}</p>
            </div>
          </v-col>
        </v-col>
      </v-row>

      <v-col cols="12" class="mt-5 mb-5">
        <h2>Séances en cours :</h2>
      </v-col>

      <v-row no-gutters>
        <v-col cols="12" class="mx-auto" v-if="not_coach == true">
          <p>Aucune séances disponible</p>
        </v-col>
      </v-row>

      <template v-for="(item) in events">
        <v-list-item :key="item" class="css_item_event">
          <v-container>
            <v-row no-gutters>
              <v-col cols="12">
                <p class="txt_event_600">{{item.label}}</p>
                <p class="txt_event">{{item.sport}}</p>
                <p class="txt_event_600">{{item.date}}</p>
                <p class="txt_event">{{item.hours}}</p>
              </v-col>
            </v-row>
          
            <v-row no-gutters>
              <v-col cols="10">
                <span><p class="txt_event">Prix :</p></span>
              </v-col>
              <v-col cols="1">
                <p class="txt_event mt-1">{{item.price}}</p>
              </v-col>
              <v-col cols="1">
                <v-img width="30" :src="featcoin"></v-img>
              </v-col>
            </v-row>

            <v-row no-gutters>
              <v-col cols="12" >
                <v-btn bottom class="btn_lowercase mr-5 mt-5" @click="infos = true" rounded>
                  en savoir plus
                </v-btn>

                <v-btn bottom class="btn_lowercase mr-5 mt-5" @click="infos = true" rounded>
                  réserver
                </v-btn>
              </v-col>
            </v-row>

          </v-container>
        </v-list-item>
      </template>

      <template v-for="(item) in events">
        <v-dialog :key="item" v-model="infos">
          <p  class="dialog_infos">{{item.description}}</p>

          <v-btn @click="infos = false">fermer</v-btn>
        </v-dialog>
      </template>
    </v-row>
  </v-container>
</template>

<script>
  import router from "../router";

  export default ({
    data: () => ({
      coach : null,
      events: [],
      not_coach: false,
      infos: false,
      test: require('@/assets/img/crossfit.jpg'),
      featcoin: require('@/assets/img/fitcoin.png')
    }),

    mounted: function() {
      //* If not connect
      if (this.$store.state.user.id == -1) {
          router.push('/');
          return
     }

      let query = router.history.current.query.id;

      this.$store.dispatch('getEventbyUserId', query).then(
        (rs) => {
          this.events = rs.data;
        }
      ).catch(
        (error) => {
          console.log(error);
        }
      );

      //* Get router params

      this.$store.dispatch('getCoachById', query).then(
        (rs) => {
          this.coach = rs.data;
        }
      ).catch(
        (error) => {
          console.log(error);
        }
      );

      return;
    },

    computed : {},

    methods : {}
})
</script>

<style scoped>
.cols_12{
  padding: 0;
}
</style>