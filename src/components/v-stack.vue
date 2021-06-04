<template>
  <div class="v-stack p-5">
    <div class="p-5">
      <b-container fluid class="p-0">
        <b-row align-v="center" class="mx-auto justify-content-center">
          <b-col class="p-0">
            <b-img
              style="min-width: 300px"
              left
              class=""
              fluid
              alt="Responsive image"
              :src="require('../assets/images/skills.png')"
            />
          </b-col>
          <b-col data-aos-duration="1500" data-aos="fade-left" class="p-0 text-right">
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
  name: "v-stack",
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.v-stack {
  background: url("../assets/images/bg_stack.png") no-repeat center;
  background-size: cover;

}
</style>