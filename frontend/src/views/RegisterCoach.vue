<template>
    <v-row no-gutters>
      <v-col>
        <div class="bg_login">
          <h2 class="text-center mt-10 mb-5 Title_log">
            Inscription pour devenir Coach FeatYou
          </h2>

          <router-link to='/register'>
            <v-btn class="btn_log mb-5 btn_alignement" rounded>Vous êtes Sportif ?</v-btn>
          </router-link>

          <form
            class="form_login mx-auto"
          >
            <v-text class="text-center">Données Personnelles</v-text>

            <v-checkbox
              v-model="checkbox"
              label="Coaching exterieur"
              required
            ></v-checkbox>

            <v-checkbox
              v-model="checkbox_interieur"
              label="Coaching interieur"
              required
            ></v-checkbox>
            
            <v-text-field
              v-model="username_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="Username"
              required
            />

            <v-text-field
              v-model="firstname_reg"
              outlined
              color="black"
              background-color="#F5F5F5"
              label="FirstName"
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
              :rules="phoneNumberValidation"
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
              :rules="zipCodeValidation"
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

            <v-select
              v-model="selectSport"
              :items="sports"
              label="Sport"
              required
              multiple
              @change="$v.select.$touch()"
              @blur="$v.select.$touch()"
            ></v-select>

            <v-select
              v-model="selectLieux"
              :items="lieux"
              label="Lieux"
              required
              multiple
              @change="$v.select.$touch()"
              @blur="$v.select.$touch()"
            ></v-select>

            <div class="text-center">
              <v-btn @click="createAccount()" primary mb-5 class="btn_log">
                Créer un compte
              </v-btn>

                <v-alert type="success" v-if="status == 'created'" class="mt-5 mx-auto" width="300">
                  Account has been create !
                </v-alert>

                <v-alert type="error" v-if="status == 'failed_create'" class="mt-5 mx-auto" width="300">
                  Error: Please check all fields !
                </v-alert>

              <router-link to="/">
                <p class="mt-5">             
                  Already have an account ? Login here
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
      email_reg     : '',
      adress_reg    : '',
      lastname_reg  : '',
      username_reg  : '',
      firstname_reg : '',
      postal_reg    : '',
      phone_reg     : '',
      password_reg  : '',
      selectSport   : '',
      selectLieux   : '',
      message       : '',
      sports        : [
        'Musculation',
        'Yoga',
        'Running',
        'Zumba',
        'Step',
        'Crossfit'
      ],
      lieux: [
        'Lille',
        'Lomme',
        'La Madeleine',
        'Marcq en Baroeul',
        'Hellemes',
        'Villeneuve d\'ascq',
        'Mons en Baroeul',
        'Loos'
      ],
      checkbox            : false,
      checkbox_interieur  : false,
      EmailRulesValidation: [
        value => !!value || 'Email is required.',
        value => value.indexOf('@') !== 0 || 'Email should have a username.',
        value => value.includes('@') || 'Email should have an @.',
        value => value.indexOf('.') - value.indexOf('@') > 1 || 'Email should contain a valid domain',
        value => value.indexOf('.') <= value.length - 3 || 'Email should contain a valid domain extention.',
      ],
      ValidatePasswordRules: [
        value => !!value || 'Password is required.',
      ],
      zipCodeValidation : [
        value => /^(?:0[1-9]|[1-8]\d|9[0-8])\d{3}$/.test(value) || 'Please enter a valid zipcode (e.g : 59117)'
      ],
      phoneNumberValidation : [
        value => /^((\+)33|0)[1-9](\d{2}){4}$/.test(value) || 'Please enter a valid phone number (e.g : +336 10 42 37 65)'
      ]
    }),

    computed:{
      ...mapState(['status'])
    },

    methods: {
      createAccount() {
        this.$store.dispatch('createAccount', {
          firstName      : this.firstname_reg,
          lastName       : this.lastname_reg,
          username       : this.username_reg,
          phone          : this.phone_reg,
          adress         : this.adress_reg,
          postalCode     : this.postal_reg,
          mail           : this.email_reg,
          hashed_password: this.password_reg,
          iscoach        : true,
          sports         : JSON.stringify(this.selectSport),
          lieux          : JSON.stringify(this.selectLieux),
          coin           : 0,
        }).then(
          () => {
            //* Login user registered
            this.$store.dispatch('loginAccount', { 
              username : this.username_reg,
              password : this.password_reg,
            });
          }, 
          (error) => {
            console.log(error);
          }
        )
      }
    },
  })
</script>