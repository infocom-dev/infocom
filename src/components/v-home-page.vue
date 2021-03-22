<template>
  <div class="v-home-page ">
    <nav-bar></nav-bar>
    <div id="nav-scroller">
      <section
        id="home"
        class="home p-5 position-relative d-flex justify-content-center"
      >
        <b-container fluid class="mx-auto">
          <b-row align-v="center" align-content="center">
            <b-col>
              <b-container fluid>
                <b-row class="pt-5 mx-5">
                  <b-col class="">
                    <div class="text-left">
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
                      <!-- <br> -->
                      <div class="w-50">
                        <a href="#" class="btn">LEARN MORE</a>
                      </div>
                    </div>
                  </b-col>
                 
                </b-row>
              </b-container>
            </b-col>
             <b-col class="">
                    <b-img
                    style="min-width:400px"
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
      <section id="technology" class="technology">
        <v-calculation></v-calculation>
      </section>
      <section >
        <v-tecnology> </v-tecnology>
      </section>

      <!-- <section id="contact-us" class="contact-us">
        <contact-us></contact-us>
      </section> -->
      <section class="links">
        <Footer></Footer>
      </section>
    </div>
  </div>
</template>

<script>
import VSkills from "./v-skills.vue";
import NavBar from "./NavBar.vue";
import vCalculation from "./v-calculation"
import Footer from "./Footer.vue";
import vServicesVue from "./v-services.vue";
import vTecnology from "./v-tecnology";
import VCalculation from './v-calculation.vue';

// import ContactUs from "./contact-us.vue";
export default {
  name: "v-home-page",
  components: {
    NavBar,
    VSkills,
    vServicesVue,
    vCalculation,

    vTecnology,
    VCalculation,
    Footer,
    // ContactUs,
  },
  data() {
    return {};
  },
};
</script>

<style lang="scss" >
@import "../assets/styles/base.scss";
@import "../assets/styles/button.scss";
@import "../assets/styles/fonts.scss";
.home {
  background: url("../assets/images/bg14.jpg");

  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}

</style>