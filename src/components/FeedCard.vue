<template>
  <v-flex
    xs12
    :class="classes"
  >
    <v-dialog
      v-model="dialog"
      max-width="600px"
    >
      <template v-slot:activator="{ on }">
        <base-card
          :height="350"
          color="grey lighten-1"
          dark
          href="#!"
          v-on="on"
        >
          <v-img
            :src="require(`@/assets/articles/${value.hero}`)"
            height="100%"
            gradient="rgba(0, 0, 0, .42), rgba(0, 0, 0, .42)"
          >
            <v-layout
              v-if="!value.prominent"
              fill-height
              wrap
              text-xs-right
              ma-0
            >
              <v-flex xs12>
                <v-chip
                  label
                  class="mx-0 mb-2 text-uppercase"
                  color="grey darken-3"
                  text-color="white"
                  small
                  @click.stop=""
                >
                  {{ value.category }}
                </v-chip>
                <h3 class="subheader font-weight-light mb-2">
                  {{ value.title }}
                </h3>
                <div class="caption">
                  {{ value.author }}<br>
                </div>
              </v-flex>
              <v-flex align-self-end>
                <!-- <v-chip
              class="text-uppercase ma-0"
              color="primary"
              label
              small
              @click.stop=""
            >
              Read More
            </v-chip> -->
              </v-flex>
            </v-layout>
          </v-img>
        </base-card>
      </template>
      <v-card>
        <v-img :src="require(`@/assets/articles/${value.hero}`)">
        </v-img>
      </v-card>
    </v-dialog>
  </v-flex>
</template>

<script>
export default {
  props: {
    size: {
      type: Number,
      required: true
    },
    value: {
      type: Object,
      default: () => ({})
    }
  },

  data () {
    return {
      dialog: ''
    }
  },

  computed: {
    classes() {
      return {
        md6: this.size === 2,
        md4: this.size === 3
      };
    }
  }
};
</script>

<style>
.v-image__image {
  transition: 0.3s linear;
}
</style>
