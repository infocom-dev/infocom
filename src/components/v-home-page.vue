<template>
  <div class="v-home-page">
    <nav-bar></nav-bar>
    <div id="nav-scroller">
      <section id="home">
        <v-home></v-home>
      </section>
      <section id="services" class="service">
        <v-services-vue></v-services-vue>
      </section>
      <section id="stack" class="stack">
        <v-stack></v-stack>
      </section>
      <section>
        <v-tecnology> </v-tecnology>
      </section>
      <section id="statistic">
        <v-statistic></v-statistic>
      </section>
      <section>
        <v-steps></v-steps>
      </section>
      <section class="links">
        <Footer></Footer>
      </section>
    </div>
  </div>
</template>

<script>
import AOS from "aos";
import "aos/dist/aos.css";
import VHome from "./v-home";
import VStack from "./v-stack.vue";
import NavBar from "./NavBar.vue";
import Footer from "./Footer.vue";
import vServicesVue from "./v-services.vue";
import vTecnology from "./v-tecnology";
import VStatistic from "./v-statistic";
import VSteps from "./v-steps.vue";
export default {
  name: "v-home-page",
  components: {
    NavBar,
    VStack,
    vServicesVue,
    VSteps,
    VHome,
    vTecnology,
    Footer,
    VStatistic,
  },
  data() {
    return {};
  },
  created() {
    AOS.init();
  },
};
</script>

<style lang="scss" >
@import "../assets/styles/base.scss";
@import "../assets/styles/button.scss";
@import "../assets/styles/fonts.scss";
// .home {
//   background: url("../assets/images/bg_technology.png") no-repeat center;

//   background-size: cover;
//   // position: relative;
//   flex-direction: column;
//   height: 770px;
//   font-size: 1rem;
// }
</style>