<template>
    <div class="v-home p-5 position-relative d-flex justify-content-center">
        <b-container fluid class="p-0 ">
          <b-row align-v="center" align-content="center" class="p-5 mx-auto">
            <b-col class="p-0">
              <b-container fluid class="p-0">
                <b-row class="">
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
                right
                class=""
                :src="require('../assets/images/bg.png')"
              />
            </b-col>
          </b-row>
        </b-container>
    </div>
</template>
<script>
export default {
    name:"v-home"
}
</script>
<style lang="scss">
.v-home {
  background: url("../assets/images/bg_technology.png") no-repeat center;

  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}
</style>