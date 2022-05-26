<template>
     <v-carousel hide-delimiters class="px-1 mt-5" height="350" rounded-lg>
        <v-carousel-item
        v-for="image in images"
        :key="image"
        :src="image.url"
        ></v-carousel-item>
  </v-carousel>
</template>
<script>
export default ({
    data: () => ({
        images: [
              { url: require("@/assets/img/1.jpg"), alt: 'Commencer une activité sportive' },
              { url: require("@/assets/img/2.jpg"), alt: 'Feat you est officiellement ouvert' },
              { url: require("@/assets/img/3.jpg"), alt: 'I love you nature' },
              { url: require("@/assets/img/4.jpg"), alt: 'Quel genre de sportif es tu ?' },
          ]
      }),
})
</script>

<style scoped>
    .carrousel{
        border-radius: 30px!important;
    }
</style>
