<template>
    <div>
        <v-col cols="12">
            <h2 class="text-center">NOS CONSEILS</h2>
        </v-col>

        <v-col cols="12">
            <router-link to="/conseils_details">
                <div style="background-color: lightblue; height: 170px;">
                    <h2 class="text-center pt-16 text_conseil">SPORTIF</h2>
                </div>
            </router-link>

            <router-link to="/conseils_details">
                <div class="mt-5" style="background-color: lightblue; height: 170px;">
                    <h2 class="text-center pt-16 text_conseil">NUTRITION</h2>
                </div>
            </router-link>

            <router-link to="/conseils_details">
                <div class="mt-5" style="background-color: lightblue; height: 170px;">
                    <h2 class="text-center pt-16 text_conseil">PARTIQUE DE VIE</h2>
                </div>
            </router-link>
            <router-link to="/conseils_details">
                <div class="mt-5" style="background-color: lightblue; height: 170px;">
                    <h2 class="text-center pt-16 text_conseil">AUTRE</h2>
                </div>
            </router-link>
        </v-col>
    </div>
</template>
<script>

export default ({

})
</script>
