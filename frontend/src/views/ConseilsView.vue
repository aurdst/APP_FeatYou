<template>
    <v-row no-gutters>
        <v-col cols="12">
            <h2 class="text-center">NOS CONSEILS</h2>
        </v-col>

        <v-col cols="12">
            <router-link to="/conseils_details">
                <div style="height: 170px;" class="bg_conseils_sport">
                </div>
            </router-link>

            <router-link to="/conseils_details">
                <div class="mt-5 bg_conseils_pratique" style="height: 170px;">
                </div>
            </router-link>

            <router-link to="/conseils_details">
                <div class="mt-5 bg_conseils_nutritif" style="height: 170px;">
                </div>
            </router-link>
        </v-col>
    </v-row>
</template>
<script>

export default ({

})
</script>
