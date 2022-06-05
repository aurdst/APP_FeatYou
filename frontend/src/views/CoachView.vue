<template>
    <div>
      <div class="container_view_coach">
        <h1>{{}}</h1>
        <p>{{}}</p>
        <!-- Here mettre les sport -->
        <p>{{}}</p>
        <!-- Here mettre les lieux -->
        <p>{{}}</p>
      </div>
      <br>
      <div class="mx-auto">
        <p class="p_coach_view">Prochain cours de {{}}  :</p>
      </div>
    </div>
</template>

<script>
  import router from "../router";
  import { mapState } from 'vuex';

  export default ({
    data: () => ({
    }),

    mounted: function() {
      //* If not connect
      if (this.$store.state.user.id == -1) {
          router.push('/');
          return
      }

        //* Get user info
        this.$store.dispatch('getUserInfos').then(
            (rs) => {
                this.current_data = rs.data
            }
      ).catch(
        (error) => {
          console.log(error);
        }
      );
    },

    computed:{
      ...mapState({
          coach: 'allcoachs',
      })
    },

    methods : {
      go_to_profile(user_id) {
        router.push('/infos', {user_id})
      }
    }
})
</script>