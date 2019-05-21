<template>
  <base-card dark>
    <v-img
      class="grey lighten-2"
      height="400"
      width="100%"
      :src="require('@/assets/banner.jpg')"
    >
      <!-- <v-layout
        fill-height
        align-left
        pa-3
      >
        <v-img
          :src="require('@/assets/logo_icon.png')"
          class="mr-5"
          style="cursor: pointer;"
          contain
          height="128"
          width="128"
          max-width="128"
          @click="$vuetify.goTo(0)"
        />
      </v-layout> -->
      <v-layout
        fill-height
        align-center
        pa-3
      >
        <v-flex
          xs12
          md7
          offset-md5
        >
          <h1 class="display-3 font-weight-light">
            Roah Cosmetics & Lashes
          </h1>
          <div class="subheading text-uppercase pl-2 mb-4">
            <!-- <v-list-tile>
              <v-list-tile-avatar color="primary">
                <v-icon
                  class="elevation-4"
                  dark
                >
                  mdi-map-marker
                </v-icon>
              </v-list-tile-avatar>
              <v-list-tile-title>4562 MACK ROAD, SACRAMENTO CA 95823</v-list-tile-title>
            </v-list-tile> -->
            <v-icon
              dark
            >
              mdi-map-marker
            </v-icon>
            4562 MACK ROAD, SACRAMENTO CA 95823
          </div>
          <v-btn
            color="primary"
            depressed
            round
            @click="$vuetify.goTo('#subscribe')"
          >
            Subscribe
          </v-btn>
        </v-flex>
      </v-layout>
    </v-img>
  </base-card>
</template>
