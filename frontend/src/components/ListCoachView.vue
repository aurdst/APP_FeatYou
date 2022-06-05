<template>
  <v-card
    class="mx-auto"
    fluid
    width="90%"
  >
    <v-spacer></v-spacer>

    <v-btn class="btn_list ma-3" text to="/">
      Voir tout nos coachs
      <v-icon
        dark
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
            Voir profile
          </v-btn>
        </v-list-item>

       
      </template>
    </v-list>
  </v-card>
</template>

<script>
  import router from "../router";
  import { mapState } from 'vuex'
  import store from "../store"
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
          for (let i = 0; i < 10; i++) {
            this.coachs.push(
              {
                avatar : rs[i].pict,
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

    methods : {
      go_to_profile() {
        store.dispatch('goToProfile', {
            user_id    : this.coachs.id,
        }).then(
            (rs) => {
              console.log(rs)
            }
        ).catch(
            (error) => {
                this.alert.show = true
                this.alert.msg  = error
                this.alert.type = 'error'
            }
        );
      }
    }
})
</script>