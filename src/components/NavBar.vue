<template>
  <div class="NavBar">
    <b-navbar toggleable="lg" fixed="top" class="nav">
      <b-navbar-brand class="mx-4">
        <h1 class="text-uppercase font-weight-bolder">INFO<span>com</span></h1>
      </b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav class="ml-auto">
          <div v-for="item in menu" :key="item">
            <b-nav-item size="lg" href="#">
              <h4 class="text-uppercase font-weight-bolder">{{ item }}</h4>
            </b-nav-item>
          </div>
          <b-nav-item-dropdown right>
            <template #button-content>
              <i class="fa fa-user user-icon" aria-hidden="true"></i>
            </template>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Sign Out</b-dropdown-item>
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
      menu: ["Home", "Services", "Team", "Contact-us"],
    };
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.nav {
  text-align:center;
  background: $bg;
  .user-icon, .navbar-toggler-icon, .navbar-light .nav-link .navbar-nav{
    color: $ylw;
  }
}
</style>