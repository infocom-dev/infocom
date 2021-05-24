<template>
  <div class="v-home-page">
    <nav-bar></nav-bar>
    <div id="nav-scroller">
      <section
        id="home"
        class="home position-relative d-flex justify-content-center"
      >
        <b-container fluid class="">
          <b-row align-v="center" align-content="center" class="mx-auro">
            <b-col class="p-0">
              <b-container fluid class="">
                <b-row class="pt-5 m-5">
                  <b-col class="">
                    <div
                      data-aos="zoom-in"
                      data-aos-duration="1500"
                      class="text-left"
                    >
                      <p>Our Clients Are Our First Priority</p>
                      <h1 class="mt-4 text-uppercase font-weight-bolder">
                        WELCOME TO INFOCOM
                      </h1>

                      <p class="mt-4">
                        Lorem Ipsum is simply dummy text of the printing and
                        typesetting industry. Lorem Ipsum has been the
                        industry's standard dummy text ever since the 1500s,
                        when an unknown printer took a galley of type and
                        scrambled it to make a type specimen book.
                      </p>

                      <div class="w-50">
                        <!-- <router-link to="login"> -->
                        <a href="login" class="btn">LEARN MORE</a>
                        <!-- </router-link> -->
                      </div>
                    </div>
                  </b-col>
                </b-row>
              </b-container>
            </b-col>
            <b-col class="">
              <b-img
                style="min-width: 400px"
                fluid
                center
                class=""
                :src="require('../assets/images/bg.png')"
              />
            </b-col>
          </b-row>
        </b-container>
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
      <section>
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
import AOS from 'aos'
import 'aos/dist/aos.css'
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
.home {
  background: url("../assets/images/bg_technology.png");

  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}
</style>