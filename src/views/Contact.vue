<template>
  <v-container
    id="contact"
    tag="section"
  >
    <base-subheading>Contact</base-subheading>
    <under-construction/>
  </v-container>
</template>

<script>
export default {
  name: "Contact",
  components: {
    UnderConstruction: () => import('@/components/core/UnderConstruction.vue'),
  }
}
</script>

