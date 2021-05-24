<template>
  <div class="v-tecnology p-5">
    <b-container fluid class="p-0">
      <b-row align-v="center" class='mx-auto p-5 w-100'>
        <b-col class="p-0">
          <b-img
           style="min-width:300px"
           fluid
           
            right
            class=""
            :src="require('../assets/images/technology.png')"
          />
        </b-col>
        <b-col data-aos="fade-right" data-aos-duration="1500" class="p-0 order-first text-left mr-5">
          <h1 class=" text-uppercase font-weight-bolder">
            WELCOME TO INFOCOM
          </h1>

          <p class="">
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book.
          </p>
          <div class="w-25 mr-auto">
                <a href="#" class="btn">LEARN MORE</a>
              </div>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>


<script>
export default {
  name: "v-tecnology",
};
</script>




<style lang="scss">
.v-tecnology {
  background: url("../assets/images/bg_technology.png") no-repeat center;
  background-size: cover;
  // height: 600px;
}
</style>