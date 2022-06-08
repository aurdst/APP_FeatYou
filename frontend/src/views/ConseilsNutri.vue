<template>
    <v-row no-gutters>
        <router-link to="conseils">
            <div class="container_btn_back mt-5 ml-5">
                <v-btn>
                    <v-icon>
                        mdi-arrow-left
                    </v-icon>
                </v-btn>
            </div>
        </router-link>
        <v-row no-gutters>
            <v-col cols="12">
                <h1 class="text-center mb-5 mt-5">Toujours bien s'étirer</h1>
            </v-col>
            <v-col cols="12">
                <p class="text-left mx-9"> 
                    Le meilleur moment pour bien s'étirer, c'est après l'entraînement, quand le corps est encore chaud. Mais les étirements doivent rester courts, entre 10 et 20 secondes
                </p>
                <p class="text-left mx-9"> 
                    Quelques exemples d'étirements :
                </p>
                <iframe width="370" height="295" src="https://www.youtube.com/embed/s-HoqxE-iDI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </v-col>
        </v-row>
    </v-row>
</template>
<script>
export default ({
    data: () => ({
      img: require('@/assets/img/halt.jpeg')  
    }),
})
</script>

<style scoped>
    iframe{
        display: block;
        margin: auto;
    }
</style>