<template>
  <v-row no-gutters>
    <v-col cols="12">
        <h1 class="text-center mt-5">FAQ</h1>
        <v-card
            class="mx-auto mt-5"
            max-width="344"
        >
            <v-card-title dense @click="show = !show">
            Comment faire pour ?
            </v-card-title>

            <v-expand-transition>
            <div v-show="show">
                <v-divider></v-divider>

                <v-card-text>
                I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                </v-card-text>
            </div>
            </v-expand-transition>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            max-width="344"
        >
            <v-card-title dense @click="showQuestion2 = !showQuestion2">
            A quel moment faire pour ?
            </v-card-title>

            <v-expand-transition>
            <div v-show="showQuestion2">
                <v-divider></v-divider>

                <v-card-text>
                I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                </v-card-text>
            </div>
            </v-expand-transition>
        </v-card>

        <v-card
            class="mx-auto mt-5"
            max-width="344"
        >
            <v-card-title dense @click="showQuestion3 = !showQuestion3">
            Pourquoi faire ceci ?
            </v-card-title>

            <v-expand-transition>
            <div v-show="showQuestion3">
                <v-divider></v-divider>

                <v-card-text>
                I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
                </v-card-text>
            </div>
            </v-expand-transition>
        </v-card>
    </v-col>

    <v-col cols="12">
        <h2 class="text-left ml-5 mt-10">Contact</h2>
    </v-col>
        
    <v-col clos="2" class="mx-1">
        <v-icon large class="ma-5">mdi-phone-in-talk</v-icon>
    </v-col>

    <v-col clos="4" class="mt-2">
        <p class="text_infos">06 00 00 00 00</p>
        <p class="text_infos">06 00 00 00 00</p>
    </v-col>

    <v-col clos="2">
        <v-icon large class="mx-5 mt-5">mdi-at</v-icon>
    </v-col>

    <v-col clos="4" class="mr-3 mt-2">
        <p class="text_infos">email@email.fr</p>
        <p class="text_infos">email@email.fr</p>
    </v-col>

    <v-col cols="12">
        <h2 class="text-left ml-5 mt-10">Suivez-nous</h2>
    </v-col>

    <v-col clos="2" class="mx-1">
        <v-icon large class="ma-5">mdi-facebook</v-icon>
    </v-col>

    <v-col clos="4" class="mt-7">
        <p class="text_infos">featyou_officiel</p>
    </v-col>

    <v-col clos="2">
        <v-icon large class="mx-5 mt-5">mdi-instagram</v-icon>
    </v-col>

    <v-col clos="4" class="mr-3 mt-7">
        <p class="text_infos">featyou_officiel</p>
    </v-col>

    <v-col clos="2" class="mx-1">
        <v-icon large class="ma-5">mdi-pinterest</v-icon>
    </v-col>

    <v-col clos="4" class="mt-7">
        <p class="text_infos">featyou_officiel</p>
    </v-col>

    <v-col clos="2">
        <v-icon large class="mx-5 mt-5">mdi-twitter</v-icon>
    </v-col>

    <v-col clos="4" class="mr-3 mt-7">
        <p class="text_infos">featyou_officiel</p>
    </v-col>

    <v-col cols="10" class="mt-5 mx-auto">
        <div class="bg_news">
            <p class="pa-5">Abonnez vous à notre Newsletter pour suivre nos actus</p>
            <v-text-field color="white" solo placeholder="email@email.com" dense :rules="rulesValidEmail"></v-text-field>
        </div>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
      show: false,
      showQuestion2: false,
      showQuestion3: false
    }),
  }
</script>