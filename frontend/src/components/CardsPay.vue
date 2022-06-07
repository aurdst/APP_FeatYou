<template>
    <div>
        <v-col>
            <h3 class="title_buy_coin">Choisissez votre quantité de featcoin : </h3>
        </v-col>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">50 featcoins</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">100 featcoins</p>
                </v-card>
            </v-col>
        </v-row>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">150 featcoins</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">200 featcoins</p>
                </v-card>
            </v-col>
        </v-row>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">250 featcoins</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card width="150" height="130" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">300 featcoins</p>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default ({
        data: () => ({
            fitcoin : require("@/assets/img/fitcoin.png"),        
        })
    })
</script>