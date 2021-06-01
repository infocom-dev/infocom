<template>
  <div class="side-bar-account w-100 h-100">
    <div :style="window.height" class="sticky-top">
      <b-nav class="w-100 h-100" vertical align="left ">
        <b-navbar-brand class="d-none d-lg-block">
          <h3 class="p-3 text-uppercase font-weight-bolder my-auto">
            INFO<span>com</span>
          </h3>
        </b-navbar-brand>
        <div
          v-for="item in side_nav"
          class="justify-content-center"
          :key="item"
          align="left"
        >
          <b-nav-item>
            <router-link :to="item.path">
              <b-row
                align-v="center"
                class="text-center justify-content-center p-0"
              >
                <div class="col-4 p-0 text-center">
                  <i :class="item.icon"></i>
                </div>
                <div class="col text-left d-none d-lg-block">
                  <h5>{{ item.text }}</h5>
                </div>
              </b-row></router-link
            >
          </b-nav-item>
        </div>
      </b-nav>
    </div>
  </div>
</template>
<script>
export default {
  name: "side-bar",
  data() {
    return {
      side_nav: [
        {
          icon: "fa fa-home icon",
          text: "Home    ",
          path: "/",
        },
        {
          icon: "fa fa-folder-open icon",
          text: "Projects",
          path: "/account/projects",
        },
        {
          icon: "fa fa-credit-card icon",
          text: "Purchase",
          path: "/account/purchase",
        },
        {
          icon: "fa fa-cog icon",
          text: "Settings",
          path: "/account/settings",
        },
        {
          icon: "fa fa-question-circle icon",
          text: "Help",
          path: "/account/help",
        },
      ],
      window: {
        height: "",
      },
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.window.height = "height:" + window.innerHeight + "px";
    },
  },
};
</script>
<style lang='scss'>
@import "../assets/styles/base.scss";
.side-bar-account {
  .icon {
    font-size: 30px;
    color: $blu;
    &:hover {
      color: $ylw;
    }
  }
}
</style>