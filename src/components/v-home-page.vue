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
      <section id="skills" class="skills">
        <v-skills></v-skills>
      </section>
      <section>
        <v-tecnology> </v-tecnology>
      </section>
      <section id="statistic">
        <statistic></statistic>
      </section>
      <section>
        <v-calculation></v-calculation>
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
import VSkills from "./v-skills.vue";
import NavBar from "./NavBar.vue";
import vCalculation from "./v-calculation";
import Footer from "./Footer.vue";
import vServicesVue from "./v-services.vue";
import vTecnology from "./v-tecnology";
// import VCalculation from "./v-calculation.vue";
import Statistic from "./statistic";
import VCalculation from "./v-calculation.vue";
// import ContactUs from "./contact-us.vue";
export default {
  name: "v-home-page",
  components: {
    NavBar,
    VSkills,
    vServicesVue,
    vCalculation,
    VHome,

    vTecnology,
    // VCalculation,
    Footer,
    Statistic,
    VCalculation,
    // ContactUs,
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