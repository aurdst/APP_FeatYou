<template>
  <v-row no-gutters>
    <v-col cols="12">
        <div class="container_faq">
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
        </div>
    </v-col>

    <v-col cols="12">
        <h2 class="text-left ml-5 mt-10">Contact</h2>
    </v-col>
        
    <v-col clos="2" class="mx-1">
        <v-avatar
            class="ml-5 mt-3"
            size="46"
        >
            <img
            :src="icon_tel"
            alt="tel"
            >   
        </v-avatar>
    </v-col>

    <v-col clos="4" class="mt-2">
        <p class="text_infos">07.98.67.59.00</p>
        <p class="text_infos">07.96.08.77.43</p>
    </v-col>

    <v-col clos="2">
        <v-avatar
            class="ml-5 mt-3"
            size="46"
        >
            <img
            :src="icon_mail"
            alt="mail"
            >   
        </v-avatar>
    </v-col>

    <v-col clos="4" class="mr-6 mt-2">
        <p class="text_infos">featyou@outlook.fr</p>
        <p class="text_infos">featyou@gmail.com</p>
    </v-col>

    <v-col cols="12">
        <h2 class="text-left ml-5 mt-10">Suivez-nous</h2>
    </v-col>

    <v-col clos="2">
        <v-avatar
            class="ml-5 mt-3"
            size="46"
        >
            <img
            :src="icon_tiktok"
            alt="mail"
            >   
        </v-avatar>
    </v-col>

    <v-col clos="4" class="mr-6 mt-2">
        <p class="text_infos mt-5">featyou_officiel</p>
    </v-col>

    <v-col clos="2">
        <v-avatar
            class="ml-5 mt-3"
            size="46"
        >
            <img
            :src="fb_icon"
            alt="mail"
            >   
        </v-avatar>
    </v-col>

    <v-col clos="4" class="mr-6 mt-2">
        <p class="text_infos mt-5">featyou_officiel</p>
    </v-col>

    <v-col cols="12">
    </v-col>

        <v-avatar
            class="mx-auto mt-3"
            size="46"
        >
            <img
            :src="icon_instagram"
            alt="mail"
            >   
        </v-avatar>

    <v-col clos="4" class="mr-6 mt-2">
        <p class="text_infos mt-5">featyou_officiel</p>
    </v-col>




    <v-col cols="10" class="mt-5 mb-5 mx-auto">
        <div class="bg_news bg_fields_mail">
            <p class="pa-5">Abonnez vous à notre Newsletter pour suivre nos actus</p>
            <v-text-field color="white" class="v_fields_mail mx-auto" solo placeholder="email@email.com" dense :rules="rulesValidEmail"></v-text-field>
            <v-btn icon class="btn_news">
                <v-icon>mdi-send-circle</v-icon>
            </v-btn>
        </div>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data: () => ({
        show: false,
      showQuestion2: false,
      showQuestion3: false,
      fb_icon: require("@/assets/img/fb_icon.png"),
      icon_tel: require("@/assets/img/icon_tel.png"),
      icon_mail: require("@/assets/img/icon_mail.png"),
      icon_conseil: require("@/assets/img/icon_conseil.png"),
      icon_faq: require("@/assets/img/icon_faq.png"),
      icon_instagram: require("@/assets/img/icon_insta.png"),
      icon_tiktok: require("@/assets/img/icon_tiktok.png"),
    }),
  }
</script>