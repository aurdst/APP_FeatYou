<template>
    <v-row no-gutters>
        <v-col cols="12" class="mt-10">
            <v-img class="rounded-circle text-center mx-auto" :src="img" width="150" height="150"></v-img>
            <div class="profile_text ma-auto mt-5 pa-5">
                <p class="text-left label_profil remove_margin">Nom :</p>
                <p class="text-left zone_data">{{ user.lastName }}</p>

                <p class="text-left label_profil remove_margin">Prénom :</p>
                <p class="text-left zone_data">{{ user.firstName }}</p>

                <p class="text-left label_profil remove_margin">Mail :</p>
                <p class="text-left zone_data">{{ user.email }}</p>

                <p class="text-left label_profil remove_margin">Adresse :</p>
                <p class="text-left zone_data">{{ user.adress }}</p>

                <p class="text-left label_profil remove_margin">Numéro de téléphone :</p>
                <p class="text-left zone_data">{{ user.phone }}</p>

                <p class="text-left label_profil remove_margin">Inscrit depuis le :</p>
                <p class="text-left zone_data">{{ user.dateRegister }}</p>

                <p class="text-left label_profil remove_margin">Carte enregistrée :</p>
                <p class="text-left zone_data">{{ user.banqCardNumb }}</p>
            </div>

            <div class="mx-auto">
                <v-btn class="btn_profile btn_log">Modifier</v-btn>
            </div>

            <div class="ma-auto mt-5">
                <div class="div_action">
                    <img :src="fitcoin" />
                    <p>{{}}</p>
                </div>
                <div class="div_action_btn">
                    <v-link to="/home">
                        <v-btn block class="btn_lowercase">Acheter des fitcoin</v-btn>
                    </v-link>

                    <v-link to="/home">
                        <v-btn block class="mt-5 pt-5 pb-5 btn_lowercase">Réserver une séance</v-btn>
                    </v-link>
                </div>
            </div>

            <div class="mx-auto">
                <v-btn @click="logout()" class="btn_profile" color="red">Déconnexion</v-btn>
            </div>
        </v-col>
    </v-row>
</template>

<style scoped>
    .remove_margin{
        margin-bottom: 0px;
    }
</style>

<script>
import router from "../router";
import store from "../store"
import { mapState } from 'vuex'

export default ({
    data: () => ({
        img: require("@/assets/img/halt.jpeg"),
        fitcoin: require("@/assets/img/fitcoin.png")
    }),

    //* When the vue is generate     
    mounted: function() {
        //* If not connect
        if (this.$store.state.user.id == -1) {
            router.push('/');
            return
        }

        //* Get user info
        this.$store.dispatch('getUserInfos').then((rs) => {
            console.log(rs)
        }).catch((error) => {
            console.log(error)
        })
    },

    computed:{
      ...mapState({
          user: 'user',
      })
    },
    methods: {
        logout: () => {
            store.commit('logout');
            router.push('/');
        }
    }
})
</script>