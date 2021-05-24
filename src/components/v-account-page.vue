<template>
  <div class="v-account-page w-100 ">
    <b-row align-h="center" class="w-100 m-0">
      <b-container
        class="w-100  col-2 p-0"
      >
        <side-bar-account></side-bar-account>
      </b-container>
      <b-container fluid class="col p-0 m-0">
        <b-container fluid class="p-0 ml-0">
          <b-row align-v="center" class="mr-0 p-0">
            <b-col>
              <b-row
                align-v="center"
                class="text-center justify-content-center m-4"
              >
                <b-col class="col">
                  <i class="fa fa-user-circle user-icon"></i>
                </b-col>
                <b-col class="col-7  text-left d-none d-lg-block">
                  <h5>Hello, user!</h5>
                  <b-row align-v="center" class="ml-0">
                    <i class="text-center m-1 fa fa-envelope mail-icon"></i>
                    <p class="m-1">example.com</p>
                  </b-row>
                </b-col>
              </b-row>
            </b-col>
            <b-col class="d-none d-sm-block"></b-col>
            <b-col class='p-0'>
              <b-row align-h="center" align-v="center" class="text-left mr-3">
                <div class="bellhold">
                  <i class="text-center fa fa-bell bell-icon"></i>
                  <span class="badgex badge-danger">6</span>
                </div>
                <router-link to="/logout">
                  <div class="m-5">
                    <a
                      href="#"
                      class="btn text-uppercase w-100 mx-auto d-none d-lg-block"
                      >log out</a
                    >

                    <i
                      class="fas fa-sign-out-alt out-icon m-4 d-block d-lg-none"
                    ></i>
                  </div>
                </router-link>
              </b-row>
            </b-col>
          </b-row>
          <b-container fluid class="w-100 p-0 overview">
            <h3 class=" p-5">Overview</h3>
            <b-container fluid class="w-100 ml-0 justify-content-center">
              <b-row align-v="center" class="justify-content-center">
                <div
                  v-for="item in overview"
                  :key="item"
                  class="col ml-5 mr-5 text-center overview-box"
                  style="width: 100%; max-width: 300px; min-width: 200px"
                >
                  <h5 class="text-center pt-2">{{ item.title }}</h5>
                  <b-row align-v="center" class="justify-content-center">
                    <i class="text-left m-1" :class="item.icon"></i>
                    <h3 class="text-left pl-3 m-1">{{ item.number }}</h3>
                  </b-row>
                  <p class="text-center pt-2">{{ item.link }}</p>
                </div>
              </b-row>
            </b-container>
            <h3 class="p-5 text-left">Recent activity</h3>
            <div class="mr-5 ml-5 pb-5">
              <b-table
                style="background-color: white"
                responsive
                striped
                hover
                :items="activity"
              ></b-table>
            </div>
          </b-container>
        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
import SideBarAccount from "./side-bar-account.vue";
export default {
  name: "v-account",
  components: {
    SideBarAccount,
  },
  data() {
    return {
      activity: [
        {
          Project: "name",
          Budjet: "1 000 000",
          Status: "in progress",
          Date: "14/05/2001",
        },
        {
          Project: "name",
          Budjet: "1 000 000",
          Status: "in progress",
          Date: "14/05/2001",
        },
      ],

      overview: [
        {
          icon: "fa fa-hourglass-half icon",
          title: "Projects in progress",
          number: "1",
          link: "View details",
        },
        {
          icon: "fa fa-code icon",
          title: "Projects in analysis",
          number: "2",
          link: "View details",
        },
        {
          icon: "fa fa-check icon",
          title: "Finished projects",
          number: "0",
          link: "View details",
        },
      ],
    };
  },
};
</script>
<style lang='scss'>
@import "../assets/styles/base.scss";
.v-account-page{
  .icon{
    font-size: 30px;
    color: $blu;
    &:hover {
      color: $ylw;
    }
  }
}


.user-icon {
  font-size: 80px;
  color: $blu;
}
.mail-icon {
  color: $blu;
}
.bell-icon,
.out-icon {
  font-size: 30px;
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
.overview {
  background-color: #e7ecef;
  // height: 900px;
}
.overview-box {
  background-color: #ffffff;
}

</style>