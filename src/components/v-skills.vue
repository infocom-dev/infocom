<template>
  <div class="v-skills p-5">
    <div class="">
      <b-container fluid class="mx-auto">
        <b-row align-v="center" class="justife-content-center w-100">
          <b-col class="">
            <b-img
              style="min-width: 300px"
              center
              class=""
              fluid
              alt="Responsive image"
              :src="require('../assets/images/skills.png')"
            />
          </b-col>
          <b-col class="text-right mr-5">
            <h1 class="mt-4 text-uppercase font-weight-bolder">
              WELCOME TO INFOCOM
            </h1>

            <p class="mt-4">
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book.
            </p>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<script>
export default {
  name: "v-skills",
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.v-skills {
  background: url("../assets/images/bg_skills4.png") no-repeat center;
  background-size: cover;
  // width: 1440px;
  // height: 750px;
}
</style>