<template>
  <v-toolbar
    app
    flat
  >
    <v-toolbar-side-icon
      class="hidden-md-and-up"
      @click="toggleDrawer"
    />
    <v-container
      mx-auto
      py-0
    >
      <v-layout>
        <v-img
          :src="require('@/assets/logo_icon.png')"
          class="mr-5"
          style="cursor: pointer;"
          contain
          height="48"
          width="48"
          max-width="48"
          @click="$vuetify.goTo(0)"
        />
        <v-btn
          v-for="(link, i) in links"
          :key="i"
          :to="link.to"
          :href="link.href"
          class="ml-0 hidden-sm-and-down"
          flat
          @click="onClick($event, item)"
        >
          {{ link.text }}
        </v-btn>
        <v-spacer />
        <v-text-field
          v-model="searchInput"
          append-icon="mdi-magnify"
          flat
          hide-details
          solo-inverted
          style="max-width: 300px;"
          @change="filterInput"
          @click:append="filterInput(searchInput)"
        />
      </v-layout>
    </v-container>
  </v-toolbar>
</template>

<script>
  // Utilities
  import { mapGetters, mapMutations, mapActions } from 'vuex'

  export default {
    data () {
      return {
        searchInput: ''
      };
    },
    computed: {
      ...mapGetters(['links'])
    },

    methods: {
      ...mapMutations(['toggleDrawer']),
      ...mapActions(['filterArticles']),
      onClick(e, item) {
        e.stopPropagation();
        if (item.to || !item.href) return;
        else {
          window.open(item.href, '_blank')
          // this.$vuetify.goTo(item.href);
        }
      },
      filterInput(value) {
        this.filterArticles(value);
      }
    }
  }
</script>
