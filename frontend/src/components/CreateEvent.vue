<template>
    <v-row no-gutters>
        <v-col cols="12">
            <v-dialog v-model="dialog" persistent max-width="600px">
                <template v-slot:activator="{ on, attrs }">
                    <img width="200" height="155" :src="create_event"/>

                    <v-btn  class="btn_event mb-5" v-bind="attrs" v-on="on">
                        <v-icon>
                            mdi-plus
                        </v-icon>
                    </v-btn>
                </template>

                <v-card>
                    <v-card-title>
                        <span class="text-h5">Créer un évenement</span>
                    </v-card-title>

                    <v-card-text>
                        <v-container>
                            <v-row>
                                <v-col cols="12" sm="6" md="4">
                                    <v-text-field solo color="black" v-model="label" label="Nom du cours" required/>
                                    <v-select :items="items" v-model="selected_sport" label="Sport"></v-select>
                                    <v-textarea solo name="input-7-4" v-model="description" label="Description du cours"></v-textarea>
                                    <vuetify-google-autocomplete id="map" label="Adresse de l'évenement" v-on:placechanged="getAddressData" v-model="adress" required></vuetify-google-autocomplete>

                                    <h3>Séléctionnez le prix de l'évenement (en Featcoin): </h3>

                                    <v-row>
                                        <v-col>
                                            <v-row>
                                                <v-col cols="8">
                                                    <v-select :items="price" v-model="selected_price" label="Prix en FeatCoin" class="mt-2" required></v-select>
                                                </v-col>
                                                
                                                <v-col cols="4">
                                                    <template>
                                                        <v-fade-transition leave-absolute>
                                                            <img width="50" height="65" :src="featcoin" alt="">
                                                        </v-fade-transition>
                                                    </template>
                                                </v-col>
                                            </v-row>
                                        </v-col>
                                    </v-row>

                                    <h3>Durée de l'évenement : </h3>

                                    <v-row>
                                        <v-col>
                                            <v-select :items="duree" v-model="selected_duree" label="Durée de l'évenement" class="mt-2" required></v-select>
                                        </v-col>
                                    </v-row>

                                    <h3>Séléctionnez la date de l'évenement : </h3>

                                    <br>

                                    <template>
                                        <v-row justify="space-around" align="center">
                                            <v-date-picker color="#5C3C90" v-model="date" flat></v-date-picker>
                                        </v-row>
                                    </template>

                                    <template>
                                        <v-row justify="center">
                                            <v-col>
                                                <v-time-picker v-model="hours" color="#5C3C90" format="24hr"></v-time-picker>
                                            </v-col>
                                        </v-row>
                                    </template>
                                </v-col>
                            </v-row>
                        </v-container>
                    </v-card-text>

                    <v-card-actions>
                        <v-spacer></v-spacer>

                        <v-btn color="blue darken-1" text @click="dialog = false">
                            Close
                        </v-btn>

                        <v-btn color="blue darken-1" text @click="createEvent()">
                            Créer un événement
                        </v-btn> 
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-col>
    </v-row>
</template>

<script>
    import router from "../router";
    import { mapState } from 'vuex'

export default ({
        data: () => ({
            featcoin          : require('@/assets/img/fitcoin.png'),
            create_event      : require('@/assets/img/create_event.png'),
            dialog            : false,
            hours             : null,
            date              : null,
            adress            : '',
            label             : '',
            description       : '',
            selected_sport    : '',
            listOfParticipant : '[]',
            items             : [
                'Yoga', 
                'Musculation', 
                'Zumba', 
                'Step', 
                'Crossfit'
            ],            
            duree : [
                '30 min',
                '1h',
                '1h30',
                '2h',
                '2h30',
                '3h'
            ],
            price : [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10
            ],
            ValidatePasswordRules : [
                value => !!value || 'Password is required.',
            ],
        }),

        mounted : function() {
            if (this.$store.state.user.id == -1) {
                router.push('/');
                return
            }
        },

        computed:{
            //* For get the status into store
            ...mapState(['status'])
        },

        methods: {
            //* Create event method
            createEvent() {
                this.$store.dispatch('createEvent', {
                    date        : this.date,
                    label       : this.label,
                    hours       : this.hours,
                    adress      : this.adress,
                    description : this.description,
                    price       : this.selected_price,
                    sport       : this.selected_sport,
                    duree       : this.selected_duree,
                    idUser      : JSON.parse(localStorage.getItem("user")).user.id
                });

                this.dialog = false;
            }
        },
    })
</script>
