<template>
    <v-row no-gutters>
        <v-col cols="12">
            <div class="mx-auto container_logout pb-3">
                <p class="text-center ma-0 pt-5">Se déconnecter :</p>
                <v-icon @click="logout()" class="btn_profile mt-0" color="red">mdi-logout-variant</v-icon>
            </div>
        </v-col>

        <v-col cols="12" class="mt-5">
            <v-img class="rounded-circle text-center mx-auto" :src="img" width="80" height="80"></v-img>

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
                <p class="text-left zone_data">{{ new Date(user.dateRegister).toLocaleDateString('fr-FR') }}</p>

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
                                            v-model="current_data.username"
                                            outlined
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="Username"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.firstName"
                                            outlined
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="Name"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.lastName"
                                            outlined
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="LastName"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.email"
                                            outlined
                                            color="black"
                                            :rules="EmailRulesValidation"
                                            background-color="#F5F5F5"
                                            label="Email"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.phone"
                                            outlined
                                            :rules="phoneNumberValidation"
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="Phone Number"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.adress"
                                            outlined
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="Adress"
                                            required
                                        />

                                        <v-text-field
                                            v-model="current_data.postalCode"
                                            outlined
                                            :rules="zipCodeValidation"
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="PostalCode"
                                            required
                                        />

                                        <v-subheader class="sub-title-dialog"> 
                                            Change your password
                                        </v-subheader>

                                        <v-divider></v-divider>

                                        <v-text-field
                                            outlined
                                            v-model="old_password"
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="Old password"
                                            required
                                        />

                                        <v-text-field
                                            outlined
                                            v-model="new_password"
                                            color="black"
                                            background-color="#F5F5F5"
                                            label="New password"
                                            required
                                        />

                                        <v-alert dismissible :type=alert.type  elevation="6" v-if="alert.show" class="mt-5 mx-auto" width="300">
                                            {{alert.msg}}
                                        </v-alert>
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
                    <p class="text_fitcoins">{{user.coin}} Fitcoins</p>
                </div>

                <div class="div_action_btn">
                    <router-link to="/home">
                        <v-btn @click="buy_featcoin()" block class="btn_lowercase">Acheter des fitcoin</v-btn>
                    </router-link>

                    <!-- Dialog featcoin -->
                    <v-dialog
                    v-model="dialog_featcoin"
                    max-width="600px"
                    >
                        <v-card>
                            <v-card-title>
                                <span class="text-h5">Choisir le moyen de paiement</span>
                            </v-card-title>

                            <v-btn
                                color="blue darken-1"
                                text
                                @click="dialog_featcoin = false"
                            >
                                Close
                            </v-btn>
                        </v-card>
                    </v-dialog>

                    <router-link to="/home">
                        <v-btn block class="mt-5 pt-5 pb-5 btn_lowercase">Réserver une séance</v-btn>
                    </router-link>
                </div>
            </div>
        </v-col>
    </v-row>
</template>

<style scoped>
    .remove_margin {
        margin-bottom: 0px;
    }

    .v-divider {
        margin : 15px 0px 15px 0px;
    }
</style>

<script>
    import router from "../router";
    import store from "../store"
    import { mapState } from 'vuex'

    export default ({
        data : () => ({
            new_password         : '',
            old_password         : '',
            alert                : {
                show : false,
                type : '',
                msg  : ''
            },
            dialog               : false,
            dialog_featcoin : false,
            img                  : require("@/assets/img/halt.jpeg"),
            fitcoin              : require("@/assets/img/fitcoin.png"),
            current_data         : {
                firstName    : '',
                lastName     : '',
                username     : '',
                phone        : '',
                email        : '',
                adress       : '',
                postalCode   : '',
            },
            EmailRulesValidation : [
                value => !!value || 'Email is required.',
                value => value.indexOf('@') !== 0 || 'Email should have a username.',
                value => value.includes('@') || 'Email should have an @.',
                value => value.indexOf('.') - value.indexOf('@') > 1 || 'Email should contain a valid domain',
                value => value.indexOf('.') <= value.length - 3 || 'Email should contain a valid domain extention.',
            ],
            zipCodeValidation : [
                value => /^(?:0[1-9]|[1-8]\d|9[0-8])\d{3}$/.test(value) || 'Please enter a valid zipcode (e.g : 59117)'
            ],
            phoneNumberValidation : [
                value => /^((\+)33|0)[1-9](\d{2}){4}$/.test(value) || 'Please enter a valid phone number (e.g : +336 10 42 37 65)'
            ]
        }),

        //* When the vue is generate
        mounted : function() {
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
                    console.log(error)
                }
            )
        },

        computed : {
            ...mapState({
                user: 'user',
            })
        },

        methods : {
            //* Disconnect user
            logout: () => {
                store.commit('logout');
                router.push('/');
            },

            //* Update user
            updateData() {
                store.dispatch('putUser', {
                    firstName    : this.current_data.firstName,
                    lastName     : this.current_data.lastName,
                    username     : this.current_data.username,
                    phone        : this.current_data.phone,
                    email        : this.current_data.email,
                    adress       : this.current_data.adress,
                    postalCode   : this.current_data.postalCode,
                    old_password : this.old_password,
                    new_password : this.new_password
                }).then(
                    (rs) => {
                        this.alert.show = true
                        this.alert.msg  = rs
                        this.alert.type = 'success'
                    }
                ).catch(
                    (error) => {
                        this.alert.show = true
                        this.alert.msg  = error
                        this.alert.type = 'error'
                    }
                );
            },
            
            buy_featcoin() {
                this.dialog_featcoin = true;
            }
        }
    });
</script>