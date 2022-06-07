<template>
    <div class="text_coach">
        <h2>{{this.coach.firstName + ' ' + this.coach.lastName}}</h2>
        <p>{{this.coach.email}}</p>
        <h2>Sport pratiqué :</h2>
        <p :key="index" v-for="(item, index) in this.coach.sport">
          {{ item }} 
        </p>
        <h2>Lieu d'exertion :</h2>
        <p :key="index" v-for="(item, index) in this.coach.lieux">
          {{ item }} 
        </p>
    </div>
</template>

<script>
  import router from "../router";

  export default ({
    data: () => ({
      coach : null
    }),

    mounted: function() {
      //* If not connect
      if (this.$store.state.user.id == -1) {
          router.push('/');
          return
      }

      //* Get router params
      let query = router.history.current.query.id;

      this.$store.dispatch('getCoachById', query).then(
        (rs) => {
          this.coach = rs.data;
          console.log(this.coach)
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