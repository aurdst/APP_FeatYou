<template>
    <v-row no-gutters>
        <v-col cols="12" class="mt-10">
            <v-img class="rounded-circle text-center mx-auto" :src="img" width="170" height="170"></v-img>
            <div class="profile_text ma-auto mt-5">
                <p class="text-center">Nom :</p>
                <p class="text-center">{{ user.lastName }}</p>

                <p class="text-center ">Prénom :</p>
                <p class="text-center">{{ user.firstName }}</p>

                <p class="text-center ">Mail :</p>
                <p class="text-center">{{ user.email }}</p>

                <p class="text-center ">Adresse :</p>
                <p class="text-center">{{ user.adress }}</p>

                <p class="text-center ">Numéro de téléphone :</p>
                <p class="text-center">{{ user.phone }}</p>

                <p class="text-center ">Inscrit depuis le :</p>
                <p class="text-center">{{ user.dateRegister }}</p>

                <p class="text-center ">Carte enregistrée :</p>
                <p class="text-center">{{ user.banqCardNumb }}</p>

            </div>

            <div class="mx-auto">
                <v-btn class="btn_profile btn_log">Modifier</v-btn>
            </div>

            <div class="profile_text ma-auto mt-5">
                <div class="div_action">
                </div>
                <div class="div_action_btn">
                    <v-btn block>Acheter des fitcoin</v-btn>
                    <v-btn block class="mt-3" to="/home">Réserver une séance</v-btn>
                </div>
            </div>

            <div class="mx-auto">
                <v-btn @click="logout()" class="btn_profile" color="red">Déconnexion</v-btn>
            </div>
        </v-col>
    </v-row>
</template>

<script>
import router from "../router";
import store from "../store"
import { mapState } from 'vuex'

export default ({
    data: () => ({
        img: require("@/assets/img/halt.jpeg")
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