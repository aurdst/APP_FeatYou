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

        <v-row no-gutters>
            <v-col>
                <div class="container_btn_buy">
                    <v-btn class="btn_lowercase">
                        Payer
                    </v-btn>
                </div>
            </v-col>
        </v-row>

        <v-row no-gutters>
            
        </v-row>
    </div>
</template>

<script>
    export default ({
        data: () => ({
            fitcoin : require("@/assets/img/fitcoin.png"),
            select_2: null,
            select_5: null  
        })
    })
</script>