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
                <v-img height="150" :src="musculation" />
            </div>
        </v-col>

        <v-col cols="12">
            <h1 class="text-center mt-5">Musculation</h1>
        </v-col>

        <v-col cols="12">
            <p class="text-center ma-5">
                Les bienfaits de la musculation et l'entrainement physique sont notables. En effet, un bon régime d'entrainement physique a été prouvé comme étant bénéfique pour la santé physique et mentale de l'individu. La musculation aurait en plus un impact sur la santé générale, la circulation sanguine, les préventions des blessures, le ralentissement des signes de vieillissement, pour n'en nommer que quelques-uns. Plusieurs études suggèrent même qu'un bon régime d'entrainement pourrait avoir des effets positifs sur le sommeil.
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
        musculation: require("@/assets/img/musculation.jpg"),
    }),
})

</script>
