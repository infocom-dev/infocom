<template>
  <div class="NavBar">
    <b-navbar
      slot="header"
      toggleable="lg"
      fixed="top"
      class="nav justify-content-center"
    >
      <b-navbar-brand class="">
        <h1 class="text-uppercase mx-5 font-weight-bolder my-auto">
          INFO<span>com</span>
        </h1>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav v-b-scrollspy:nav-scroller class="ml-auto pt-2">
          <div v-for="item in menu" :key="item">
            <b-nav-item size="lg" :href="item.href">
              <h4 class="text-uppercase font-weight-bolder">{{ item.id }}</h4>
            </b-nav-item>
          </div>
        </b-navbar-nav>
        <div v-show="this.$store.dispatch('auth/initialize') && on_site" class="">
          <router-link to="account">
            <div class="mr-5 ml-3">
              <a href="#" class="btn">ACCOUNT</a>
            </div>
          </router-link>
        </div>
        <div v-show="!on_site">
          <router-link to="login">
            <div class="mr-5 ml-3">
              <a href="#" class="btn">LOG IN</a>
            </div>
          </router-link>
        </div>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "NavBar",
  data() {
    return {
      menu: [
        { id: "Home", href: "/" },
        {
          id: "Services",
          href: "/#services",
        },
        {
          id: "Skills",
          href: "/#skills",
        },
        {
          id: "technology",
          href: "/#technology",
        },
      ],
    };
  },
  computed:{
    ...mapState("auth", [
      "on_site",
    ]),
  }
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
@import "../assets/styles/button.scss";

.nav {
  text-align: center;
  background: #a3cef1;

  .user-icon,
  .navbar-toggler-icon,
  .navbar-light .nav-link .navbar-nav {
    color: $ylw;
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: black;
  }
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.1);
  -webkit-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.1);
  -moz-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.1);
  span {
    color: white;
  }
}
</style>