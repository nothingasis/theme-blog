<template>
  <base-card dark>
    <v-carousel hide-delimiters>
      <v-carousel-item>
        <v-img
          class="grey lighten-2"
          height="500"
          width="100%"
          :src="require('@/assets/makeup-powders-and-brush.jpg')"
        >
          <v-layout
            align-center
            justify-end
            pa-3
            my-4
            ml-4
          >
            <v-flex
              xs12
              md4
            >
              <h1 class="display-3 font-weight-light">
                COMING SOON
              </h1>
              <div class="subheading text-uppercase">
                <v-icon dark>
                  mdi-map-marker
                </v-icon>
                9645 E. Stockton Blvd, Elk Grove CA 95624
              </div>
            </v-flex>
          </v-layout>
        </v-img>
      </v-carousel-item>
      <v-carousel-item>
        <v-img
          class="grey lighten-2"
          height="500"
          width="100%"
          :src="require('@/assets/banner.jpg')"
        >
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
                <v-icon dark>
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
      </v-carousel-item>
    </v-carousel>
  </base-card>
</template>
