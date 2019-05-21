<template>
  <div id="home">
    <articles>
      <banner />
    </articles>

    <!-- <about /> -->

    <subscribe />

    <!-- <social /> -->
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    name: 'Home',

    components: {
      // About: () => import('@/components/home/About'),
      Articles: () => import('@/components/home/Articles'),
      Banner: () => import('@/components/home/Banner'),
      // Social: () => import('@/components/home/Social'),
      Subscribe: () => import('@/components/home/Subscribe')
    },

    created() {
      this.buildArticles()
    },

    methods: {
      ...mapActions(['buildArticles'])
    }
  }
</script>
