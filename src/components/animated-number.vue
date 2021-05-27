<template>
  <div>
    <div>{{ val }}</div>
  </div>
</template>
<script>
export default {
  props: {
    max: {
      type: Number,
      default() {
        return;
      },
    },
    top: {
      type: Number,
      default() {
        return;
      },
    },
  },
  data: () => ({
    val: 0,
  }),
  methods: {
    onScroll() {
      if (
        this.top <
        window.scrollY && this.top != 0
      ) {
        this.removeScrollHandler();
        const interval = setInterval(() => {
          if (++this.val === this.max) {
            clearInterval(interval);
          }
        }, 3000 / this.max);
      }
    },
    removeScrollHandler() {
      window.removeEventListener("scroll", this.onScroll);
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
    this.$on("hook:beforeDestroy", this.removeScrollHandler);
    this.onScroll();
  },
};
</script>