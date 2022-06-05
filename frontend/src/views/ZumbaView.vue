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
                <v-img height="150" :src="zumba" />
            </div>
        </v-col>

        <v-col cols="12">
            <h1 class="text-center mt-5">Zumba</h1>
        </v-col>

        <v-col cols="12">
            <p class="text-center ma-5">
                La Zumba est un programme d'entraînement physique complet, alliant tous les éléments de la remise en forme : cardio et préparation musculaire, équilibre et flexibilité. Les chorégraphies s'inspirent principalement des danses latines, mais aussi de styles variés comme la danse du ventre ou la Quebradita.</p>
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
        zumba: require("@/assets/img/zumba.jpg"),
    }),
})

</script>
