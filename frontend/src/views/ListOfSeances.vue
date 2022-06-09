<template>
    <v-container>
        <div class="elevation-10 my-5 pa-5 rounded" :key="item" v-for="(item) in this.events">
            <v-row>
                <v-col cols="12">
                    <div>
                        <span class="font-weight-600 ">{{ item.label }}</span> - {{ item.duree }}
                        
                        <span class="float-right">
                            <span class="font-weight-medium">
                                {{ item.price }}
                            </span>
                            
                            <img class="fitcoin-minified" :src="fitcoin" />
                        </span>
                    </div>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="12">
                    <p>Le {{ new Date(item.date).toLocaleDateString('fr-FR')}} à {{ item.hours }}</p>

                    
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="12">
                    <p>{{ item.adress }}</p>
                </v-col>
            </v-row>

            <v-row>
                <v-col cols="12" class="d-flex justify-end">
                    <v-btn class="deep-purple darken-1 mx-3" color="white" text @click="dialog = true">
                        En savoir +
                    </v-btn>

                    <v-btn class="deep-purple darken-1 mx-3" color="white" text @click="buy_dialog = true">
                        Réserver
                    </v-btn>
                </v-col>
            </v-row>

            <v-dialog v-model="dialog" max-width="600px">
                <v-card>
                    <v-card-title>
                        <span class="text-h5">{{ item.label }} - {{ item.duree }}</span>
                    </v-card-title>

                    <v-card-body>
                        <p class="px-5">
                           <span class="font-weight-600">Description :</span> {{ item.description }}
                        </p>

                        <p class="px-5">
                            <span class="font-weight-600">Organisateur :</span> {{ item.idUser.firstName }} {{ item.idUser.lastName }}
                        </p>
                    </v-card-body>

                    <v-card-footer>
                        <v-btn color="blue darken-1" text @click="dialog = false">
                            Close
                        </v-btn>
                    </v-card-footer>
                </v-card>
            </v-dialog>

            <v-dialog v-model="buy_dialog" max-width="600px">
                <v-card>
                    <v-card-title>
                        <span class="text-h5">S'inscrire à un évènement</span>
                    </v-card-title>

                    <v-card-body>
                        <p class="px-5">
                            <span class="font-weight-600">TODO</span>
                        </p>
                    </v-card-body>

                    <v-card-footer>
                        <v-btn color="blue darken-1" text @click="reserver(item.price, item.id)">
                            Close
                        </v-btn>
                    </v-card-footer>
                </v-card>
            </v-dialog>
        </div>
    </v-container>
</template>

<style scoped>
    .fitcoin-minified {
        width: 40px;
    }

    .font-weight-600 {
        font-weight: 600;
    }
</style>

<script>
    import { mapState } from 'vuex'
    import router from "../router";
    import store from "../store";

    export default({
        data: () => ({
            fitcoin      : require("@/assets/img/fitcoin.png"),
            musculation  : require("@/assets/img/musculation.jpg"),
            dialog       : false,
            buy_dialog   : false,
            events       : {},
        }),

        mounted : function() {
            let query = router.app._route.query

            this.$store.dispatch('getEvents', query.sport).then(
                (rs) => {
                    this.events = rs.data
                }
            ).catch(
                (error) => {
                    console.log(error)
                }
            )
        },

        methods: {
            reserver(price, id_event) {
                store.dispatch('manage_participant', {
                    id_participant: JSON.parse(localStorage.getItem('user')).user.id,
                    id_event      : id_event,
                    ammount       : price,
                }).then(
                    (rs) => {
                        if (rs.status === 202) {
                            this.dialog_show = false;
                            router.push('/profile');
                        }
                    }
                );
            }
        },

        computed : {
            ...mapState({
                event: 'event',
            })
        },
    })
</script>