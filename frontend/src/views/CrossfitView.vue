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
                <v-img height="150" :src="crossfit" />
            </div>
        </v-col>

        <v-col cols="12">
            <h1 class="text-center mt-5">Crossfit</h1>
        </v-col>

        <v-col cols="12">
            <p class="text-center ma-5">
                Le CrossFit axe son fonctionnement autour de dix compétences athlétiques : endurance cardiovasculaire et respiratoire, endurance musculaire, force, souplesse, puissance, vitesse, agilité, psychomotricité, équilibre et précision.</p>
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
        crossfit: require("@/assets/img/crossfit.jpg"),
    }),
})

</script>
