<template>
  <section id="feed">
    <feed>
      <slot>
        stuff
      </slot />
    </feed>
  </section>
</template>

<script>
export default {
  components: {
    Feed: () => import("@/components/Feed")
  }
};
</script>
