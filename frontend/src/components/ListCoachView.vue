<template>
  <v-card
    max-width="450"
    class="mx-auto"
  >
    <v-spacer></v-spacer>
    <v-btn class="btn_list ma-3" to="/conseils">Go -></v-btn>
    <v-list three-line>
      <template v-for="(item, index) in items">
        <v-subheader
          v-if="item.header"
          :key="item.header"
          v-text="item.header"
        ></v-subheader>

        <v-divider
          v-else-if="item.divider"
          :key="index"
          :inset="item.inset"
        ></v-divider>

        <v-list-item
          v-else
          :key="item.title"
        >
          <v-list-item-avatar>
            <v-img :src="item.avatar"></v-img>
          </v-list-item-avatar>

          <v-list-item-content>
            <v-list-item-title v-html="item.title"></v-list-item-title>
            <v-list-item-subtitle v-html="item.subtitle"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<script>
import router from "../router";

  export default ({
    data: () => ({
      items: [
        { header: 'Coach' },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Bruno M',
          subtitle: `<span class="text--primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Hugo F',
          subtitle: `<span class="text--primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Brithney B',
          subtitle: '<span class="text--primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        { divider: true, inset: true },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Rebecca F',
          subtitle: '<span class="text--primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
    }),

    mounted: function() {
    //* If not connect
    if (this.$store.state.user.id == -1) {
        router.push('/');
        return
    }

    //* Get user info
    this.$store.dispatch('getUserInfos').then((rs) => {
        console.log(rs)
    }).catch((error) => {
        console.log(error)
    }),

    this.$store.dispatch('updateData').then((rs) => {
        console.log(rs)
    }).catch((error) => {
        console.log(error)
    })
  },
})
</script>