<template>
  <v-row no-gutters>
    <List/>
  </v-row>
</template>

<script>
  import List from '../components/ListCoachView.vue'

  export default {
    name: 'HomeView',

    components: {
      List,
    },
  }
</script>