<template>
  <v-container
    id="about"
    tag="section"
  >
    <v-layout>
      <v-flex
        xs12
        sm4
      >
        <v-card>
          <v-img
            :src="require('@/assets/full_logo.png')"
            aspect-ratio="1"
          ></v-img>
        </v-card>
      </v-flex>
      <v-flex
        xs12
        sm4
        offset-sm1
        my-4
      >
        <div class="display-2 font-weight-light">About Us</div>
        <hr><br />
        <p class="subheading font-weight-light">
          Roah cosmetics!<br />
          Your cosmetics professional in Sacramento.<br />
          Come on in!<br />
          We're located inside SF Supermarket on Mack road through the left door enterance.
        </p>

        <v-list>
          <v-list-tile
            v-for="item in items"
            :key="item.title"
            :href="item.href"
            avatar
          >
              <v-icon
                v-if="item.icon"
                :color="item.color"
              >{{item.icon}}</v-icon>

            <v-list-tile-content>
              <v-list-tile-title
                class="ml-5"
                v-text="item.title"
              ></v-list-tile-title>
            </v-list-tile-content>

          </v-list-tile>
        </v-list>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      items: [
        {
          icon: "mdi-check",
          title: "Removal",
          color: "green"
        },
        {
          icon: "mdi-check",
          title: "Classic Lashes",
          color: "green"
        },
        {
          icon: "mdi-check",
          title: "Full Volume Set",
          color: "green"
        },
        {
          icon: "mdi-check",
          title: "Russian Volume (Fan)",
          color: "green"
        },
        {
          icon: "mdi-check",
          title: "Combo Volume Set",
          color: "green"
        },
        {
          icon: "mdi-calendar",
          title: "Online Booking",
          color: "red",
          href:
            "https://square.site/book/FH4JMT69VE5JE/roah-cosmetics-lashes-sacramento-ca"
        }
        // },
        // {
        //   icon: "mdi-check",
        //   title: "Promotions"
        //   // active: true,
        //   // items: [{ title: "List Item" }]
        // }
      ]
    };
  }
};
</script>

