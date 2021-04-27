<template>
  <div class="projects">
    <b-row align-h="center" class="w-100 m-0">
      <b-container class="w-100 d-flex align-items-stretch col-2 p-0">
        <side-bar-account></side-bar-account>
      </b-container>
      <b-container class="col p-0 ml-0">
        <b-container fluid class="p-0 ml-0">
          <b-row align-v="center" class="ml-0">
            <b-col>
              <b-row
                align-v="center"
                class="text-center justify-content-center ml-5"
              >
                <div class="col-2 p-0 text-left">
                  <i class="fa fa-folder-open projects-icon"></i>
                </div>
                <div class="col text-left">
                  <h3>Projects</h3>
                </div>
              </b-row>
            </b-col>
            <b-col class="d-none d-sm-block"></b-col>
            <b-col>
              <b-row align-h="center" align-v="center" class="text-left mr-3">
                <div class="bellhold">
                  <i class="text-center fa fa-bell bell-icon"></i>
                  <span class="badgex badge-danger">6</span>
                </div>
                <router-link to="logout">
                  <div class="m-5">
                    <a
                      href="#"
                      class="btn text-uppercase w-100 mx-auto d-none d-md-block"
                      >log out</a
                    >

                    <i
                      class="fas fa-sign-out-alt out-icon m-4 d-block d-md-none"
                    ></i>
                  </div>
                </router-link>
              </b-row>
            </b-col>
          </b-row>
          <b-container fluid class="w-100 ml-0 overview">
              
          </b-container>

        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
import sideBarAccount from "./side-bar-account.vue";

export default {
  components: { sideBarAccount },
  name: "projects",
};
</script>