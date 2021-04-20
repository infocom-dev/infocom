<template>
  <div class="v-account-page w-100">
    <!-- <router-link to="logout">
      <div class="mr-5 ml-3">
        <a href="#" class="btn">logout</a>
      </div>
    </router-link> -->
    <b-row >
      <b-container class="col-2 p-0 ml-0">
        <b-nav class="w-100 h-100" vertical align="left">
          <b-navbar-brand class="d-none d-md-block">
            <h4 class="p-4 text-uppercase font-weight-bolder my-auto">
              INFO<span>com</span>
            </h4>
          </b-navbar-brand>
          <div
            v-for="item in side_nav"
            class="justify-content-center"
            :key="item"
            align="left"
          >
            <b-nav-item>
              <b-row
                align-v="center"
                class="text-center justify-content-center p-2"
              >
                <div class="col-4 p-0">
                  <i :class="item.icon"></i>
                </div>
                <div class="col text-left d-none d-md-block">
                  <h4>{{ item.text }}</h4>
                </div>
              </b-row>
            </b-nav-item>
          </div>
        </b-nav>
      </b-container>

      <b-container class="col p-0 ml-0">
        <b-container fluid class='p-0 ml-0'>
          <b-row align-v="center">
            <b-col>
              <b-row
                align-v="center"
                class="text-center justify-content-center m-4"
              >
                <b-col class="col-5">
                  <i class="fa fa-user-circle user-icon"></i>
                </b-col>
                <b-col class="text-left d-none d-md-block">
                  <h3>Hello, user!</h3>
                  <b-row align-v="center" class="ml-0">
                    <i class="text-center m-1 fa fa-envelope mail-icon"></i>
                    <p class="m-1">example.com</p>
                  </b-row>
                </b-col>
              </b-row>
            </b-col>
            <b-col class='d-none d-md-block'></b-col>
            <b-col>
              <b-row align-v="center" class="text-left m-4">
                <div class="bellhold">
                  <i class="text-center fa fa-bell bell-icon"></i>
                  <span class="badgex badge-danger">6</span>
                </div>
                <a href="#" class="btn text-uppercase w-50 mx-auto">log out</a>
              </b-row>
            </b-col>
          </b-row>
          <b-container fluid class="w-100 ml-0 overview">
            <h3 class="ml-5 pt-3">Overview</h3>
            <b-row>
              <div v-for="item in overview" :key="item">
                <b-col style="width: 300px" class="m-5 text-left overview-box  ">
                  <h5 class='p-2'>{{item.title}}</h5>
                  <i class="" :class="item.icon"></i>
                </b-col>
              </div>
            </b-row>
          </b-container>
        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
export default {
  name: "v-account",
  data() {
    return {
      side_nav: [
        {
          icon: "fa fa-home home-icon",
          text: "Home    ",
        },
        {
          icon: "fa fa-folder-open projects-icon",
          text: "Projects",
        },
        {
          icon: "fa fa-credit-card card-icon",
          text: "Purchase",
        },
        {
          icon: "fa fa-cog cog-icon",
          text: "Settings",
        },
        {
          icon: "fa fa-question-circle help-icon",
          text: "Help",
        },
      ],
      overview: [
        {
          icon: "fa fa-hourglass-half clock-icon",
          title: "Projects in progress",
          number: "1",
          link: "",
        },
        {
          icon: "fa fa-code code-icon",
          title: "Projects in analysis",
          number: "2",
          link: "",
        },
        {
          icon: "fa fa-check check-icon",
          title: "Finished projects",
          number: "0",
          link: "",
        },
      ],
    };
  },
};
</script>
<style lang='scss'>
@import "../assets/styles/base.scss";
.help-icon,
.clock-icon,
.check-icon,
.code-icon,
.home-icon,
.cog-icon,
.projects-icon,
.card-icon {
  font-size: 30px;
  color: $blu;
  &:hover {
    color: $ylw;
  }
}
.user-icon {
  font-size: 100px;
  color: $blu;
}
.mail-icon {
  color: $blu;
}
.bell-icon {
  font-size: 29px;
  color: $blu;
}
.badgex {
  padding: 0px 5px 1px;
  position: absolute;
  top: -5px;
  right: -10px;
  display: inline-block;
  min-width: 10px;
  font-size: 18px;
  box-sizing: border-box;
  font-weight: bold;
  color: #ffffff;
  line-height: 1;
  white-space: nowrap;
  text-align: center;
  border-radius: 50%;
}
.badge-danger {
  background-color: #db5565;
}
.bellhold {
  position: relative;
  cursor: pointer;
}
.overview{
  background-color: #E7ECEF;

}
.overview-box {
   background-color:#ffffff;
}
</style>