<template>
    <div>
        <router-link to="conseils">
            <div class="container_btn_back mt-5 ml-5">
                <v-btn>
                    <v-icon>
                        mdi-arrow-left
                    </v-icon>
                </v-btn>
            </div>
        </router-link>
        
        <v-row class="ma-auto">


            <v-col cols="4">
                <router-link to="/conseils_nutri">
                    <div class="div_conseil_sportif">
                    </div>
                 </router-link>
            </v-col>

            <v-col cols="4">
                <div  style="background-color: lightblue; height: 170px;" rounded>
                </div> 
            </v-col>

            <v-col cols="4">
                <div  style="background-color: lightblue; height: 170px;" rounded>
                </div>       
            </v-col>
        </v-row>

        <v-row class="ma-auto">
            <v-col cols="4">
                <div  style="background-color: lightblue; height: 170px;" rounded>
                </div>
            </v-col>

            <v-col cols="4">
                <div  style="background-color: lightblue; height: 170px;" rounded>
                </div> 
            </v-col>

            <v-col cols="4">
                <div  style="background-color: lightblue; height: 170px;" rounded>
                </div>       
            </v-col>
        </v-row>

    </div>
</template>

<script>
export default ({

})
</script>
