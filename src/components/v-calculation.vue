<template>
  <div class="v-calculation w-100 pb-5">
    <b-container fluid class="mx-auto pt-5 w-100 justify-content-center">
      <div class="mx-auto pb-5">
        <h1 class="text-center text-uppercase font-weight-bolder">
          how it works?
        </h1>
      </div>
      <b-row align-v="center" class="h-100 justify-content-center" style="">
        <div v-for="step in steps" :key="step.url">
          <div class="col">
            <b-img
            center
            class=""
            fluid

            style="width:300px;height:300px"
            :src="step.url"
          />
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>
<script>
export default {
  name: "v-calculation",
  data(){
    return{
      steps:[
        {
          url: require('../assets/images/step1.png'),
        },
        {
          url: require("../assets/images/step2.png"),
        },
        {
          url: require("../assets/images/step3.png"),
        },
        {
          url: require("../assets/images/step4.png"),
        }
      ]
    }
  }
};
</script>
<style lang="scss">
.v-calculation {
  background: url("../assets/images/step.jpg") no-repeat center;
  background-size: cover;
}
</style>