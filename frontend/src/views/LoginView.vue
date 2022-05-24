<template>
    <v-row no-gutters>
      <v-col>
        <div class="bg_login">
          <h2 class="text-center mt-10 Title_log">
            LOGIN
          </h2>

          <v-alert type="error" v-if="status == 'failed_log'" class="mt-5 mx-auto" width="300">
            Invalid username or password !
          </v-alert>

          <form
            class="form_login mx-auto"
          >
            <v-text-field
              v-model="user_log"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Email"
              required
            />

            <v-text-field
              v-model="password_log"
              outlined
              type="password"
              color="black"
              background-color="#F5F5F5"
              label="Password"
              required
            />

            <div class="text-center">
              <v-btn @click="loginAccount()" primary class="mb-3" v-if="status == 'loading'">
                Connexion en cours ...
              </v-btn>

              <v-btn @click="loginAccount()" primary class="mb-3" v-else>
                Connexion
              </v-btn>

              <router-link to="/register">
                <p>
                  Register
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

  export default ({
    data: () => ({
      user_log: '',
      password_log: '',
      message: '',
      ValidatePasswordRules: [
        value => !!value || 'Password is required.',
      ],
    }),

    computed:{
      // For get the status into store
      ...mapState(['status'])
    },

    methods: {
      loginAccount() {
        // const self = this;
        this.$store.dispatch('loginAccount', {
          username: this.user_log,
          password: this.password_log,
        })
      }
    },
  })
</script>
