<template>

<v-list three-line>
    <template v-for="(item, index) in coachs">
      <v-divider
          v-if="item.divider"
          :key="index"
          :inset="item.inset"
      ></v-divider>

      <v-list-item
        :key="item"
      >
        <v-list-item-content>
        <v-list-item-title v-html="item.lastName + ' ' + item.name"></v-list-item-title>
        <v-list-item-subtitle v-html="item.sport"></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>
    </template>
</v-list>

</template>

<script>
  import router from "../router";
  import { mapState } from 'vuex'

  export default ({
    data: () => ({
      coachs: [],
    }),

    mounted: function() {
      //* If not connect
      if (this.$store.state.user.id == -1) {
          router.push('/');
          return
      }

      //* Get user info
      this.$store.dispatch('getAllUserInfos').then(
        (rs) => {
          for (let i = 0; i < rs.length; i++) {
            this.coachs.push(
              {
                // avatar : rs[i].pict',
                name     : rs[i].firstName,
                lastName : rs[i].lastName,
                sport    : rs[i].sport,
              }
            )
          }

          return;
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
})
</script>