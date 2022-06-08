<template>
    <div>
        <v-col>
            <h3 class="title_buy_coin">Choisissez votre quantité de featcoin : </h3>
        </v-col>
        <v-row no-gutters>
            <v-col clos="6">
                <v-card @click="data = 2" width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">2 featcoins</p>
                    <p class="price pb-5">15€</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card @click="data = 5" width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">5 featcoins</p>
                    <p class="price pb-5">35€</p>
                </v-card>
            </v-col>
        </v-row>
        <v-row no-gutters>    
            <v-col clos="6">
                <v-spacer></v-spacer>
                <v-card @click="data = 10" width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class=" img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">10 featcoins</p>
                    <p class="price pb-5">70€</p>
                </v-card>
            </v-col>
            <v-col clos="6">
                <v-card @click="data = 15" width="190" height="170" class="cards_select_coins pt-5 mt-5 mx-auto">
                    <v-img :src="fitcoin" width="70" height="70" class="img_coin mx-auto"></v-img>
                    <p class="text_card_featcoin">15 featcoins</p>
                    <p class="price pb-5">100€</p>
                </v-card>
            </v-col>
        </v-row>

    </div>
</template>

<script>
    export default ({
        data: () => ({
            fitcoin : require("@/assets/img/fitcoin.png"),
            data: 0    
        })
    })
</script>