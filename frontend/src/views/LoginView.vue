<template>
    <v-row no-gutters>
      <v-col>
        <div class="bg_login">
          <h2 class="text-center mt-10 Title_log">
            LOGIN
          </h2>

          <form
            class="form_login mx-auto"
          >
            <v-text-field
              v-model="email_log"
              outlined
              color="black"
              :rules="EmailRulesValidation"
              background-color="#F5F5F5"
              label="Email"
              required
            />

            <v-text-field
              v-model="password_log"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Name"
              required
            />

            <div class="text-center">
              <v-btn @click="loginAccount()" primary>
                Connexion
              </v-btn>
            </div>
          </form>
        </div>
      </v-col>
    </v-row>
</template>

<script>
  export default ({
    data: () => ({
      email_log: '',
      password_log: '',
      EmailRulesValidation: [
        value => !!value || 'Email is required.',
        value => value.indexOf('@') !== 0 || 'Email should have a username.',
        value => value.includes('@') || 'Email should have an @.',
        value => value.indexOf('.') - value.indexOf('@') > 1 || 'Email should contain a valid domain',
        value => value.indexOf('.') <= value.length - 3 || 'Email should contain a valid domain extention.',
      ],
      message: '',
      ValidatePasswordRules: [
        value => !!value || 'Password is required.',
      ],
    }),

    computed:{

    },

    methods: {
      loginAccount() {
        this.$store.dispatch('loginAccount', {
          email: this.email_log,
          password: this.password_log
        })
      }
    },
  })
</script>
