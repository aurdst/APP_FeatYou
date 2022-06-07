<template>
  <v-card
    class="mx-auto"
    fluid
    width="90%"
  >
    <v-spacer></v-spacer>

    <v-btn class="btn_list mt-3" text to="/">
      Choisissez vôtre coach
      <v-icon
        color="#DAAB39"
        dark
        medium
        right
      >
        mdi-arrow-right
      </v-icon>
    </v-btn>

    <v-list three-line>
      <template v-for="(item, index) in coachs">
        <v-divider
          v-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-item
          :key="item"
          class="css_item_coach"
        >
          
          <v-list-item-avatar>
            <!-- <v-img :src="item.avatar"></v-img> -->
          </v-list-item-avatar>
         

          <v-list-item-content>
            <v-list-item-title class="txt_coach_preview" v-html="item.lastName + ' ' + item.name"></v-list-item-title>
            <v-list-item-subtitle class="txt_coach_preview" v-html="item.sport"></v-list-item-subtitle>
          </v-list-item-content>

          <br>

          <v-btn @click="go_to_profile(item.id)" text color="#FFF" small :key="item" >
            <v-icon small>mdi-arrow-right</v-icon>
          </v-btn>
        </v-list-item>

        
          <v-btn @click="go_to_profile(item.id)" :key="item">
            Voir profile
          </v-btn>
      </template>
    </v-list>
  </v-card>
</template>

<script>
  import router from "../router";
  import { mapState } from 'vuex'
  // import store from "../store"
  //import { sortItems } from "vuetify/lib/util/helpers";

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
          console.log(rs)
          this.coachs = rs;
          
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

    methods : {
      go_to_profile(id) {
        router.push({
          path   : 'coach_view',
          query  : { id: id }
        });
      }
    }
})
</script>