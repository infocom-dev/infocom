<template>
  <div class="NavBar">
    <b-navbar slot="header" toggleable="lg" fixed="top" class="nav">
      <b-navbar-brand class="mx-4">
        <h1 class="text-uppercase font-weight-bolder">INFO<span>com</span></h1>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav v-b-scrollspy:nav-scroller class="ml-auto">
          <div v-for="item in menu" :key="item">
            <b-nav-item size="lg" :href="item.href">
              <h4 class="text-uppercase font-weight-bolder">{{ item.id }}</h4>
            </b-nav-item>
          </div>
          <b-nav-item-dropdown right>
            <template #button-content>
              <i class="fa fa-user user-icon" aria-hidden="true"></i>
            </template>
            
              <b-dropdown-item href="#"><router-link to="login"> Sign In</router-link> </b-dropdown-item>
            
            <router-link to="logout">
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </router-link>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>
<script>
export default {
  name: "NavBar",
  data() {
    return {
      menu: [
        { id: "Home", href: "#home" },
        {
          id: "Services",
          href: "#services",
        },
        {
          id: "Team",
          href: "#team",
        },
        {
          id: "Contact-us",
          href: "#contact-us",
        },
      ],
    };
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.nav {
  text-align: center;
  background: $bg;
  .user-icon,
  .navbar-toggler-icon,
  .navbar-light .nav-link .navbar-nav {
    color: $ylw;
    -webkit-text-stroke-width: 1px;
    -webkit-text-stroke-color: black;
  }
}
</style>