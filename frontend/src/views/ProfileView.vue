<template>
    <v-row no-gutters>
        <v-col cols="12">
            <div class="mx-auto container_logout pb-3">
                <p class="text-center ma-0 pt-5">Se déconnecter :</p>
                <v-icon @click="logout()" class="btn_profile mt-0" color="red">mdi-logout-variant</v-icon>
            </div>
        </v-col>
        <v-col cols="12" class="mt-5">
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

            <v-col cols="12">
                <v-dialog
                    v-model="dialog"
                    persistent
                    max-width="600px"
                    >
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn 
                            class="btn_profile btn_log"
                            v-bind="attrs"
                            v-on="on"
                        >Modifier</v-btn>
                    </template>
                    <v-card>
                        <v-card-title>
                        <span class="text-h5">User Profile</span>
                        </v-card-title>
                        <v-card-text>
                        <v-container>
                            <v-row>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                            <v-text-field
                            v-model="username_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="Username"
                            required
                            />

                            <v-text-field
                            v-model="name_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="Name"
                            required
                            />

                            <v-text-field
                            v-model="lastname_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="LastName"
                            required
                            />

                            <v-text-field
                            v-model="email_reg"
                            outlined
                            color="black"
                            :rules="EmailRulesValidation"
                            background-color="#F5F5F5"
                            label="Email"
                            required
                            />

                            <v-text-field
                            v-model="phone_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="Phone Number"
                            required
                            />

                            <v-text-field
                            v-model="adress_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="Adress"
                            required
                            />

                            <v-text-field
                            v-model="postal_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="PostalCode"
                            required
                            />

                            <v-text-field
                            v-model="password_reg"
                            outlined
                            color="black"
                            background-color="#F5F5F5"
                            label="Password"
                            required
                            />

                            <div class="text-center">
                                <v-alert type="success" v-if="status == 'created'" class="mt-5 mx-auto" width="300">
                                Account has been create !
                                </v-alert>

                                <v-alert type="error" v-if="status == 'failed_create'" class="mt-5 mx-auto" width="300">
                                Error: Please check all fields !
                                </v-alert>
                            </div>
                        </v-col>
                </v-row>
            </v-container>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="dialog = false"
                    >
                        Close
                    </v-btn>
                    <v-btn
                        color="blue darken-1"
                        text
                        @click="updateData()" 
                    >
                        Save
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-col>

            <div class="ma-auto mt-5 mb-15 container_fitcoin">
                <div class="div_action">
                    <img :src="fitcoin" />
                    <p class="text_fitcoins">{{}} Fitcoins</p>
                </div>
                <div class="div_action_btn">
                    <router-link to="/home">
                        <v-btn block class="btn_lowercase">Acheter des fitcoin</v-btn>
                    </router-link>

                    <router-link to="/home">
                        <v-btn block class="mt-5 pt-5 pb-5 btn_lowercase">Réserver une séance</v-btn>
                    </router-link>
                </div>
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
        fitcoin: require("@/assets/img/fitcoin.png"),
        dialogm1: '',
        dialog: false,
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
        }),

        this.$store.dispatch('updateData').then((rs) => {
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
        },
        updateData: () => {
            store.commit('updateData');
        }
    }
})
</script>