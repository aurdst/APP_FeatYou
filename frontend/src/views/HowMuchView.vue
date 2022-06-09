<template>
    <div>
        <v-col>
            <h3 class="title_buy_coin">Choisissez votre quantité de featcoin : </h3>
        </v-col>

        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto" @click="dialog_show = true, ammount=2">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">2 featcoins</p>
                    <p class="price pb-5">15€</p>
                </v-card>
            </v-col>

            <v-col clos="6">
                <v-card width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto" @click="dialog_show = true, ammount=5">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">5 featcoins</p>
                    <p class="price pb-5">35€</p>
                </v-card>
            </v-col>
        </v-row>

        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto" @click="dialog_show = true, ammount=10">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">10 featcoins</p>
                    <p class="price pb-5">70€</p>
                </v-card>
            </v-col>
            
            <v-col clos="6">
                <v-card width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto" @click="dialog_show = true, ammount=15">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">15 featcoins</p>
                    <p class="price pb-5">100€</p>
                </v-card>
            </v-col>
        </v-row>

        <v-dialog v-model="dialog_show" max-width="600px" class="pa-5">
            <v-card>
                <v-card-title>
                    <span class="text-h5">Achetez {{ammount}} featcoins</span>
                </v-card-title>

                <v-card-body>
                    <v-text-field v-model="card_owner" outlined color="black" background-color="#F5F5F5" label="Titulaire de la carte" required/>
                    <v-text-field solo type="number" v-model.number="card_numbers" outlined color="black" background-color="#F5F5F5" label="Numéro de la carte" required hint="Enter un numéro de carte valide"/>

                    <v-row>
                        <v-col clos="4">
                            <v-text-field solo v-model.number="card_ccv" type="number" outlined color="black" background-color="#F5F5F5" label="CCV" max-length="3" required/>
                        </v-col>

                        <v-col clos="4">
                            <v-select v-model="card_month_expire" :items="['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']" label="Mois d'expiration" required @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select>
                        </v-col>

                        <v-col clos="4">
                            <v-select v-model="card_year_expire" :items="['2022', '2023', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']" label="Année d'expiration" required @change="$v.select.$touch()" @blur="$v.select.$touch()"></v-select>
                        </v-col>
                    </v-row>
                </v-card-body>

                <v-card-footer>
                    <v-btn color="blue darken-1" text @click="dialog_show = false">
                        Close
                    </v-btn>

                    <v-btn color="blue darken-1" text @click="credit_featcoin(ammount)">
                        Buy
                    </v-btn>
                </v-card-footer>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
    import store from "../store";
    import router from "../router";


    export default ({
        data: () => ({
            fitcoin          : require("@/assets/img/fitcoin.png"),
            dialog_show      : false,
            card_owner       : null,
            card_numbers     : null,
            card_ccv         : null,
            card_year_expire : null,
            card_month_expire: null,
            ammount          : 0
        }),

        methods : {
            credit_featcoin(ammount) {
                store.dispatch('manage_coin', {
                    id       : JSON.parse(localStorage.getItem('user')).user.id,
                    ammount  : ammount,
                    operator : '+'
                }).then(
                    (rs) => {
                        if (rs.status === 202) {
                            this.dialog_show = false;
                            router.push('/profile');
                        }
                    }
                );
            }
        }
    })
</script>