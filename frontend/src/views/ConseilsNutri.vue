<template>
    <v-row no-gutters>
        <v-row>
            <v-col cols="12">
                <h1 class="text-center mb-5 mt-5">Un déjeuner equilibré</h1>
            </v-col>
            <v-col cols="12">
                <h1 class="text-center">Conseils</h1>
                <p class="text-left mx-9"> 
                    - tVero eos et accusamus sc et iusto odio dignissimos ducimus 
                    <br>
                    - qui blanditiis praesentium voluptatum jkbjhgv deleniti atque corrupti quos dolores et 
                    <br>
                    - quas molestias excepturi sint occaecati.
                    <br>
                    - qui blanditiis praesentium voluptatum jkbjhgv deleniti atque corrupti quos dolores et 
                    <br>
                    - quas molestias excepturi sint occaecati
                </p>
            </v-col>
            <v-col clos="3" class="mt-5 ml-5">
                <v-img class="rounded-circle text-center mx-auto" :src="img" width="60" height="60"/>
            </v-col>

            <v-col cols="3" class="mt-5">
                <v-img class="rounded-circle text-center mx-auto" :src="img" width="60" height="60"/>
            </v-col>

            <v-col clos="3" class="mt-5">
                <v-img class="rounded-circle text-center mx-auto" :src="img" width="60" height="60"/>
            </v-col>

            <v-col cols="3" class="mt-5 mr-5">
                <v-img class="rounded-circle text-center mx-auto" :src="img" width="60" height="60"/>
            </v-col>
        </v-row>

        <v-row class="ma-auto mt-5">
            <v-col cols="12">
                <div  style="background-color: blue; height: 140px;" rounded>
                    <h2 class="text-center pt-12">coaching</h2>
                </div>
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
