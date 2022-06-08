<template>
    <v-row no-gutters class="text_coach">
      <v-row no-gutters>
        <v-col cols="10" class="container_infos mx-auto mt-5">
          <v-col cols="12" class="cols_12">
            <br>
            <h4>{{this.coach.firstName + ' ' + this.coach.lastName}}</h4>
            <p>{{this.coach.email}}</p>
          </v-col>
          <v-col cols="12" class="cols_12">
            <h4>Sport pratiqué :</h4>
            <div :key="index" v-for="(item, index) in this.coach.sport" class="container_sport">
              <p>{{ item }}</p>
            </div>
          </v-col>
          <v-col cols="12" class="mt-4 cols_12">
            <h4>Lieu d'exertion :</h4>
            <p :key="index" v-for="(item, index) in this.coach.lieux">
              {{ item }}
            </p>
          </v-col>
        </v-col>
      </v-row>

      <v-col cols="12">
        <template v-for="(item, i) in events[i]">
          <v-list-item
            :key="i"
            class="css_item_coach"
          >
            <v-list-item-content class="list_item">
              <v-list-item-title class="txt_coach_preview" v-html="item"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </template>
      </v-col>
    </v-row>
</template>

<script>
  import router from "../router";

  export default ({
    data: () => ({
      coach : null,
      events: [],
      not_coach: false
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
          this.events = rs;
          console.log(this.events.data)
        }
      ).catch(
        (error) => {
          console.log(error);
          this.not_coach = true;
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