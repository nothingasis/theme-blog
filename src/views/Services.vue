<template>
  <v-container
    id="services"
    tag="section"
  >
    <v-container
      fluid
      grid-list-md
    >
      <v-layout
        row
        wrap
      >
        <p class="text-xs-center font-weight-light display-2">Services</p>
      </v-layout>
      <hr>
      <v-layout
        row
        wrap
      >
        <v-flex
          v-for="(card, i) in cards"
          :key="card.title + i"
          v-bind="{ [`xs${card.flex}`]: true }"
        >
          <v-card>
            <v-card-title>
              <p class="title font-weight-medium bg-dark">{{card.title}}</p>
            </v-card-title>
            <v-card-text>{{card.text}}
            </v-card-text>
            <v-card-actions>
              <v-btn color="primary">
                {{card.cost}}
              </v-btn>
              <v-spacer></v-spacer>
              <v-btn
                fab
                flat
                :href="card.href"
                target="_blank"
              >
                <v-icon>mdi-calendar</v-icon>
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
const services = require("../data/services.json");
export default {
  name: "Services",
  data() {
    return {
      cards: services,
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

