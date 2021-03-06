<template>
  <div class="v-home-page">
    <nav-bar></nav-bar>
    <div
      data-spy="scroll"
      data-target="#list-example"
      data-offset="0"
      class="scrollspy-example"
    >
      <section class="home position-relative d-flex justify-content-center">
        <div class="home-skew-border">
          <div class="w-75 mx-auto text-center">
            <p>Our Clients Are Our First Priority</p>
            <h1 class="text-uppercase font-weight-bolder">
              WELCOME TO INFOCOM
            </h1>
            <div class="separator"></div>
            <p class="font-weight-bolder">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book.
            </p>
            <b-button size="lg" variant="outline-warning"
              >GET STARTED NOW</b-button
            >
          </div>
        </div>
      </section>
      <section class="service">
        <v-services-vue></v-services-vue>
      </section>
      <section class="team">
        <v-team></v-team>
      </section>
      <section class="skills">
        <v-skills></v-skills>
      </section>
      <section class="links">
        <Footer></Footer>
      </section>
    </div>
  </div>
</template>

<script>
import VSkills from "./v-skills.vue";
import NavBar from "./NavBar.vue";
import Footer from "./Footer.vue";
import vServicesVue from "./v-services.vue";
import VTeam from "./v-team.vue";
export default {
  name: "v-home-page",
  components: {
    NavBar,
    VSkills,
    vServicesVue,
    VTeam,
    Footer,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>

<style lang="scss" >
@import "../assets/styles/base.scss";
@import "../assets/styles/button.scss";
@import "../assets/styles/fonts.scss";
.home {
  background: url("../assets/images/09.jpg") no-repeat center center;
  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}
.home-skew-border:after {
  position: absolute;
  left: 0;
  bottom: 0;
  content: "";
  width: 0;
  height: 0;
  border-bottom: 86px solid $wht;
  border-right: 680px solid transparent;
}
.home-skew-border:before {
  position: absolute;
  right: 0;
  bottom: 0;
  content: "";
  width: 0;
  height: 0;
  border-bottom: 86px solid $wht;
  border-left: 680px solid transparent;
}
.separator {
  width: 10px;
  height: 10px;
  margin: 20px auto;
  background: $ylw;
  position: relative;
  display: inline-block;
  border-radius: 50%;
}
.separator::before {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  direction: rtl;
  position: absolute;
  right: 5%;
  bottom: 4px;
  height: 1px;
  width: 80px;
  background: $wht;
  content: "";
  display: inline-block;
  margin-right: 20px;
}
.separator::after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  direction: rtl;
  position: absolute;
  left: 5%;
  bottom: 4px;
  height: 1px;
  width: 80px;
  background: $wht;
  content: "";
  display: inline-block;
  margin-left: 20px;
}
</style>