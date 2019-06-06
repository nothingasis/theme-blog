<template>
  <v-container
    id="contact"
    tag="section"
  >
    <v-layout
      row
      wrap
    >
      <p class="text-xs-center font-weight-light display-2">Contact</p>
    </v-layout>
    <hr>
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
      Sacramento CA 95823<br/>
      <a href="mailto:roahcosmetics@gmail.com">roahcosmetics@gmail.com</a><br/>
      (916) 709-7537
    </p>
  </v-container>
</template>

<script>
export default {
  name: "Contact",
  components: {}
};
</script>

