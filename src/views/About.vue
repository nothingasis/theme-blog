<template>
  <v-container id="about" tag="section">
    <v-layout>
      <v-flex xs12 sm4>
        <v-card>
          <v-img
            :src="require('@/assets/full_logo.png')"
            aspect-ratio="1"
          ></v-img>
        </v-card>
      </v-flex>
      <v-flex xs12 sm4 offset-sm1 my-4>
        <div class="display-2 font-weight-light">About Us</div>
        <p class="body-1">
          Roah cosmetics! Your cosmetics professional in Sacramento. Come on in!
          We're located inside SF Supermarket on Mack road through the left door enterance.
          <a href="https://square.site/book/FH4JMT69VE5JE/roah-cosmetics-lashes-sacramento-ca">Book your appointment</a> today!
        </p>
      </v-flex>
    </v-layout>
  </v-container>
</template>
