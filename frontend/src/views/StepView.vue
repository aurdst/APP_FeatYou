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
                <v-img height="150" :src="step" />
            </div>
        </v-col>


        <v-col cols="12">
            <h1 class="text-center mt-5">Step</h1>
        </v-col>

        <v-col cols="12">
            <p class="text-center ma-5">
               Le step est une des composantes fondamentales dans les activités du fitness. Créé en 1986 par Gin Miller, les cours de step sont aujourd'hui populaires. Le nom de cette activité est lié à l'appareil qui est utilisé et qui s'appelle le step. La discipline détient également un enjeu compétitif depuis 2014</p>
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
        step: require("@/assets/img/step.jpg"),
    }),
})

</script>
