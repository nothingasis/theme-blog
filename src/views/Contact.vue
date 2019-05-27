<template>
  <v-container
    id="contact"
    tag="section"
  >
    <base-subheading>Contact</base-subheading>
    <v-img
      class="grey lighten-2"
      height="400"
      width="100%"
      :src="require('@/assets/map.png')"
    >
      <v-layout
        fill-height
        align-center
        pa-3
      >
        <v-flex
          xs12
          md7
          offset-md4
        >
          <div class="subheading text-uppercase pl-2 mb-4">
          </div>
        </v-flex>
      </v-layout>
    </v-img>
    <p class="headline font-weight-light text-xs-center">
      Inside SF Supermarket at <br />
      4562 MACK RD<br />
      Sacramento CA 95823
    </p>
  </v-container>
</template>

<script>
export default {
  name: "Contact",
  components: {}
};
</script>

