<template>
  <v-row no-gutters>
    <v-col cols="12">
    <v-dialog
        v-model="dialog"
        persistent
        max-width="600px"
    >

        <template v-slot:activator="{ on, attrs }">
            <v-btn 
                class="btn_profile btn_log mb-5"
                v-bind="attrs"
                v-on="on"
            >Créer un cours</v-btn>
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
                                solo
                                color="black"
                                v-model="label"
                                label="Nom du cours"
                                required
                            />

                            <v-select
                                :items="items"
                                v-model="selectSport"
                                :menu-props="{ top: true, offsetY: true }"
                                label="Choisissez le Sport"
                                :return-object="false"
                            ></v-select>

                            <v-textarea
                                solo
                                name="input-7-4"
                                v-model="description"
                                label="Description du cours"
                            ></v-textarea>

                            <h3>Séléctionnez le prix de l'évenement (en Featcoin): </h3>

                            <v-row>
                                <v-col>
                                    <v-row>
                                        <v-col cols="8">
                                            <v-text-field
                                                solo
                                                color="black"
                                                v-model.number="price"
                                                type="number"
                                                class="mt-2"
                                                label="Prix en FeatCoin"
                                                required
                                            />
                                        </v-col>
                                        
                                        <v-col cols="4">
                                            <template>
                                                <v-fade-transition leave-absolute>
                                                    <img
                                                    width="50"
                                                    height="65"
                                                    :src="featcoin"
                                                    alt=""
                                                    >
                                                </v-fade-transition>
                                            </template>
                                        </v-col>
                                    </v-row>
                                </v-col>
                            </v-row>


                            <h3>Séléctionnez la date de l'évenement : </h3>

                            <br>
                            
                            <template>
                                <v-row
                                    justify="space-around"
                                    align="center"
                                >
                                    <v-date-picker
                                    color="#5C3C90"
                                    v-model="date"
                                    flat
                                    ></v-date-picker>
                                </v-row>
                            </template>

                            <template>
                                <v-row justify="center">
                                    <v-col>
                                    <v-time-picker
                                        v-model="hours"
                                        color="#5C3C90"
                                        format="24hr"
                                    ></v-time-picker>
                                    </v-col>
                                </v-row>
                            </template>
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
                    @click="createEvent()" 
                >
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
      dialog : false,
      featcoin: require('@/assets/img/fitcoin.png'),
      label : '',
      description : '',
      hours: null,
      selectSport: '',
      lieu: 'Lille',
      items: ['Musculation', 'Running', 'Yoga', 'Step', 'Crossfit'],
      idUser : null,
      date: null,
      price: null,
      listOfParticipant: [],
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
      //* Login user method
      createEvent() {
        this.$store.dispatch('createEvent', {
            label: this.label,
            description: this.description,
            date: this.date,
            sport: JSON.stringify(this.items),
            lieu: this.lieu,
            hours: this.hours,
            price: this.price,
        });
        this.dialog = false;
        console.log(this.items)
      }
    },
  })
</script>
