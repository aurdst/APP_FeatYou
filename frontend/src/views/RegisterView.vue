<template>
    <v-row no-gutters>
      <v-col>
        <div class="bg_login">
          <h2 class="text-center mt-10 Title_log">
            Register
          </h2>

          <form
            class="form_login mx-auto"
          >

            <v-text-field
              v-model="username_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Username"
              required
            />

            <v-text-field
              v-model="name_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Name"
              required
            />

            <v-text-field
              v-model="lastname_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="LastName"
              required
            />

            <v-text-field
              v-model="email_reg"
              outlined
              color="black"
              :rules="EmailRulesValidation"
              background-color="#F5F5F5"
              label="Email"
              required
            />

            <v-text-field
              v-model="phone_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Phone Number"
              required
            />

            <v-text-field
              v-model="adress_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Adress"
              required
            />

            <v-text-field
              v-model="postal_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="PostalCode"
              required
            />

            <v-text-field
              v-model="password_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Password"
              required
            />

            <div class="text-center">
              <v-btn @click="createAccount()" primary mb-5>
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
      email_reg: '',
      adress_reg:'',
      lastname_reg: '',
      username_reg: '',
      name_reg: '',
      postal_reg: '',
      phone_reg: '',
      password_reg: '',
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
      createAccount() {
        console.log(this.username_reg);

        this.$store.dispatch('createAccount', {
          firstName: this.username_reg,
          lastName: this.lastname_reg,
          username: this.username_reg,
          phone: this.phone_reg,
          adress: this.adress_reg,
          postalCode: this.postal_reg,
          email: this.email_reg,
          hashed_password: this.password_reg,
        })
      }
    },
  })
</script>
