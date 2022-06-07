<template>
    <div>
        <v-col>
            <h3 class="title_buy_coin">Choisissez votre quantité de featcoin : </h3>
        </v-col>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="200" height="190" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-container class="container_radio" fluid>
                        <v-radio-group
                        v-model="select_2"
                        column
                        >
                            <v-radio
                                class="mx-auto radio"
                                color="success"
                                value="success"
                            ></v-radio>
                        </v-radio-group>
                    </v-container>
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">2 featcoins</p>
                    <p class="price pb-5">15€</p>

                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card width="200" height="190" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-container class="container_radio" fluid>
                        <v-radio-group
                        v-model="select_5"
                        column
                        >
                            <v-radio
                                class="mx-auto radio"
                                color="success"
                                value="success"
                            ></v-radio>
                        </v-radio-group>
                    </v-container>
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">5 featcoins</p>
                    <p class="price pb-5">35€</p>
                </v-card>
            </v-col>
        </v-row>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="200" height="190" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-container class="container_radio" fluid>
                        <v-radio-group
                        v-model="select_5"
                        column
                        >
                            <v-radio
                                class="mx-auto radio"
                                color="success"
                                value="success"
                            ></v-radio>
                        </v-radio-group>
                    </v-container>
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">10 featcoins</p>
                    <p class="price pb-5">70€</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card width="200" height="190" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-container class="container_radio" fluid>
                        <v-radio-group
                        v-model="select_5"
                        column
                        >
                            <v-radio
                                class="mx-auto radio"
                                color="success"
                                value="success"
                            ></v-radio>
                        </v-radio-group>
                    </v-container>
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">15 featcoins</p>
                    <p class="price pb-5">100€</p>
                </v-card>
            </v-col>
        </v-row>

        <v-row>
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
                        >Payer</v-btn>
                    </template>
    
                    <v-card>
                        <v-card-title>
                            <span class="text-h5">Methods of paiment</span>
                        </v-card-title>
    
                        <v-card-text>
                            <v-container>
                                <v-row>
                                    <v-col
                                        cols="12"
                                        sm="6"
                                        md="4"
                                    >
                                    </v-col>
                                </v-row>
                            </v-container>
                        </v-card-text>

                        <v-row no-gutters>    
                            <v-col clos="6">
                                <v-card width="150" height="100" class="cards_select_coins pt-5 mt-5 mx-auto">
                                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                                </v-card>
                            </v-col>
                            <v-col clos="6">
                                <v-card width="150" height="100" class="cards_select_coins pt-5 mt-5 mx-auto">
                                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                                </v-card>
                            </v-col>
                        </v-row>

                        <v-row no-gutters>    
                            <v-col clos="6">
                                <v-card width="150" height="100" class="cards_select_coins pt-5 mt-5 mx-auto">
                                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                                </v-card>
                            </v-col>
                            <v-col clos="6">
                                <v-card width="150" height="100" class="cards_select_coins pt-5 mt-5 mx-auto">
                                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                                </v-card>
                            </v-col>
                        </v-row>
    
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
                            >
                                Save
                            </v-btn> 
                        </v-card-actions>
                    </v-card>
                </v-dialog>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default ({
        data: () => ({
            fitcoin : require("@/assets/img/fitcoin.png"),
            // paypal : require('@/assets/img/'),
            // googlepay : require('@/assets/img/'),
            // other : require('@/assets/img/'),
            // againother : require('@/assets/img/'),
            dialog : false,
            select_2: null,
            select_5: null  
        })
    })
</script>