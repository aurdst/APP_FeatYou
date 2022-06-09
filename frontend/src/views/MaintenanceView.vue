<template>
    <div>
        <v-row no-gutters>
            <v-col cols="12">
                <h1>Messagerie bientôt disponible ! </h1>
            </v-col>
        </v-row>

        <v-row no-gutters>
            <v-col cols="12">
                <img :src="img" alt="messagerie">
            </v-col>
        </v-row>
    </div>
</template>

<script>
export default ({
    data: () => ({
      img: require('@/assets/img/messagerie.png')  
    }),
})
</script>