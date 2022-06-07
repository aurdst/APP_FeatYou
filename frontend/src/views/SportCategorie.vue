<template>
    <v-row class="mt-5" no-gutters>
        <v-col cols="12" class="text-center">
            <h2>Nos Sports :</h2>
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/musculation">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="musculation" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Musculation</h2>
                </v-img>
            </router-link>  
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/crossfit">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="crossfit" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Crossfit</h2>
                </v-img>
            </router-link>  
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/yoga">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="yoga" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Yoga</h2>
                </v-img>
            </router-link>  
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/step">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="step" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Step</h2>
                </v-img>
            </router-link>  
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/zumba">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="zumba" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Zumba</h2>
                </v-img>
            </router-link>  
        </v-col>

        <v-col cols="6" class="mt-5">
                <router-link to="/running">
                <v-img class="rounded-circle text-center mx-auto overlay" :src="running" width="170" height="170">
                    <h2 class="text-center mt-16 text_sport_categorie">Running</h2>
                </v-img>
            </router-link>  
        </v-col>
    </v-row>
</template>
<script>
export default ({
    data: () => ({
        step: require("@/assets/img/step.jpg"),
        yoga: require("@/assets/img/yoga_categorie.jpg"),
        musculation: require("@/assets/img/musculation.jpg"),
        zumba: require("@/assets/img/zumba.jpg"),
        crossfit: require("@/assets/img/crossfit.jpg"),
        running: require("@/assets/img/running.jpg")
    })
})
</script>
