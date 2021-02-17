
<template>
  <div class="v-navigation-wrapper">
    <div class="menu-wrap">
      <div class="logo">
        <h1>INFO<span>com</span></h1>
      </div>

      <nav v-if="!(state && small)">
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Services</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
      <div class="button">
        <button @click="myFunction">
          <i class="fa fa-bars menu-icon"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script >
export default {
  name: "v-navigation-wrapper",
  data() {
    return {
      state: true,
      small: false,
    };
  },
  created() {
    window.addEventListener("resize", this.onResize);
    this.onResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.onResize);
  },
  methods: {
    myFunction() {
      this.state = !this.state;
    },
    onResize() {
      this.small = window.innerWidth <= 768;
    },
  },
};
</script>
<style lang="scss" >
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: sans-serif;
}
</style>