<template>
  <v-container
    id="subscribe"
    tag="section"
  >
    <base-card
      color="rgba(203, 170, 92, 0.51)"
      class="pa-3"
    >
      <v-container
        grid-list-xl
        pa-0
      >
        <v-layout wrap>
          <v-flex
            xs12
            md5
          >
            <base-subheading class="mb-3">
              Subscribe
            </base-subheading>
            <p>
              Enter your email address to subscribe
              and receive notifications of newsletters by email.
            </p>

            <v-layout
              wrap
              pa-2
            >
              <v-text-field
                solo
                hide-details
                style="max-width: 400px;"
              />
              <v-btn
                id="subscribe"
                :block="$vuetify.breakpoint.xsOnly"
                class="ma-0"
                color="secondary"
                style="height: 48px"
                @click="subscribe()"
              >
                Subscribe
              </v-btn>

              <v-snackbar v-model="showSubscribe" bottom :timeout="3600">
                Not available, please try again later.
                <v-btn color="#cbaa5c" flat @click="showSubscribe = false">
                  Close
                </v-btn>
              </v-snackbar>
            </v-layout>
          </v-flex>
          <v-flex
            xs12
            md6
            offset-md1
          >
            <base-subheading>Contact</base-subheading>
            <v-list class="transparent">
              <v-list-tile>
                <v-list-tile-avatar color="primary">
                  <v-icon
                    class="elevation-4"
                    dark
                  >
                    mdi-email-outline
                  </v-icon>
                </v-list-tile-avatar>
                <v-list-tile-title>EMAIL</v-list-tile-title>
                <v-list-tile-sub-title>
                  ROAHCOSMETICS@GMAIL.COM
                </v-list-tile-sub-title>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-avatar color="primary">
                  <v-icon
                    class="elevation-4"
                    dark
                  >
                    mdi-map-marker
                  </v-icon>
                </v-list-tile-avatar>
                <v-list-tile-title>ADDRESS</v-list-tile-title>
                <v-list-tile-sub-title>
                  4562 MACK ROAD, SACRAMENTO CA 95823
                </v-list-tile-sub-title>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-avatar color="primary">
                  <v-icon
                    class="elevation-4"
                    dark
                  >
                    mdi-phone
                  </v-icon>
                </v-list-tile-avatar>
                <v-list-tile-title>PHONE</v-list-tile-title>
                <v-list-tile-sub-title>
                  916-709-7537
                </v-list-tile-sub-title>
              </v-list-tile>
              <v-list-tile>
                <v-list-tile-avatar color="primary">
                  <v-icon
                    class="elevation-4"
                    dark
                  >
                    mdi-clock
                  </v-icon>
                </v-list-tile-avatar>
                <v-list-tile-title>HOURS</v-list-tile-title>
                <v-list-tile-sub-title>
                  MOTUWE 11-6 THU CLOSED FR 11-6 SA 11-630 SU 11-6
                </v-list-tile-sub-title>
              </v-list-tile>
            </v-list>
          </v-flex>
        </v-layout>
      </v-container>
    </base-card>
  </v-container>
</template>

<script>
  export default {
    name: 'Subscribe',
    data () {
      return {
        showSubscribe: false,
      }
    },
    methods: {
      subscribe () {
        this.showSubscribe = true;
      }
    }
  }
</script>
