<template>
    <v-row no-gutters>
        <router-link to="categorie">
            <div class="container_btn_back mt-5 ml-5">
                <v-btn>
                    <v-icon>
                        mdi-arrow-left
                    </v-icon>
                </v-btn>
            </div>
        </router-link>

        <v-col cols="12">
            <div class="container_img_sport">
                <v-img height="150" :src="yoga" />
            </div>
        </v-col>

        <v-col cols="12">
            <h1 class="text-center mt-5">Yoga</h1>
        </v-col>

        <v-col cols="12">
            <p class="text-center ma-5">
                Le yoga apporte un grand nombre de bienfaits physiques notamment l'assouplissement des muscles (les postures de yoga sont variées pour étirer l'ensemble des grands groupes musculaires). Certaines postures aident au renforcement musculaire en douceur, d'autres font plutôt travailler l'équilibre. 
            </p>
        </v-col>

        <v-col cols="12">
            <h2 class="text-left ma-3">Pour découvrir :</h2>
            <v-btn large class="large mb-15 ml-3">Je réserve ma séance</v-btn>
        </v-col>
    </v-row>
</template>
<script>

export default({
    data: () => ({
        yoga: require("@/assets/img/yoga.jpg"),
    }),
})

</script>
