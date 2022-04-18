<template>
    <v-row no-gutters>
        <v-col cols="12" class="mt-10">
            <v-img class="rounded-circle text-center mx-auto" :src="img" width="170" height="170"></v-img>
            <div class="profile_text ma-auto mt-5">
            </div>
            <v-btn class="btn_profile">TEXT</v-btn>
            <div class="profile_text ma-auto mt-5">
                <div class="div_action">
                </div>
                <div class="div_action_btn">
                    <v-btn block class="mt-3">Text</v-btn>
                    <v-btn block class="mt-3">Text</v-btn>
                </div>


            </div>
        </v-col>
    </v-row>
</template>

<script>
export default ({
    data: () => ({
        img: require("@/assets/img/halt.jpeg")
    })
})
</script>