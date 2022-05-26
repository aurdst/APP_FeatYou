<template>
    <v-row no-gutters>
      <v-col>
        <div class="bg_login">
          <h3 class="text-center mt-16 mb-5 Title_log">
            Nous sommes ravi de te revoir parmis nous
          </h3>

          <v-alert type="error" v-if="status == 'failed_log'" class="mt-5 mx-auto" width="300">
            Invalid username or password !
          </v-alert>

          <form
            class="form_login mx-auto mt-10"
          >
            <v-text-field
              v-model="user_log"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Identifiant"
              required
            />

            <v-text-field
              v-model="password_log"
              outlined
              type="password"
              color="black"
              background-color="#F5F5F5"
              label="Mot de passe"
              required
            />

            <div class="text-center">
              <v-btn @click="loginAccount()" class="btn_log mb-3" v-if="status == 'loading'">
                Connexion en cours ...
              </v-btn>

              <v-btn @click="loginAccount()" class="btn_log mb-3" v-else>
                Connexion
              </v-btn>

              <router-link to="/register">
                <p>
                  S'inscrire ici
                </p>
              </router-link>
            </div>


          </form>
        </div>
      </v-col>
    </v-row>
</template>

<script>
import { mapState } from 'vuex'
import router from '../router'

  export default ({
    data: () => ({
      user_log: '',
      password_log: '',
      message: '',
      ValidatePasswordRules: [
        value => !!value || 'Password is required.',
      ],
    }),

    mounted: function () {
      if (this.$store.state.user.id != -1){
        router.push('profile')
      }
    },

    computed:{
      // For get the status into store
      ...mapState(['status'])
    },

    methods: {
      loginAccount() {
        this.$store.dispatch('loginAccount', {
          username: this.user_log,
          password: this.password_log,
        })
      }
    },
  })
</script>
