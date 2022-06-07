<template>
    <div>
        <h1>{{this.coach.firstName + ' ' + this.coach.lastName}}</h1>
        <p>{{this.coach.email}}</p>

        <br>

        <h2>Activités principales :</h2>
        <li :key="index" v-for="(item, index) in this.coach.sport">
          {{ item }} 
        </li>

        <br>

        <h2>Lieux d'intervention :</h2>
        <li :key="index" v-for="(item, index) in this.coach.lieux">
          {{ item }} 
        </li>
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