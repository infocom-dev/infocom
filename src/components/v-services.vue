<template>
  <div class="v-services">
    <b-container fluid class="w-100">
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          our<span>services</span>
        </h1>
      </div>
      <b-container fluid class="p-0 w-100 justify-content-center">
        <b-row align-v="center" class="w-100 justify-content-center">
          <div v-for="service in services" :key="service">
            <div
              class="col m-5 text-center box2 "
              style="width: 300px"
              :style="service.h"
            >
              <i class="m-3" :class="service.icon"></i>
              <h4 class="text-uppercase font-weight-bolder m-2">
                {{ service.title }}
              </h4>
              <p>{{ service.text }}</p>
              <div class="w-50 mx-auto">
                <a href="#" class="btn">LEARN MORE</a>
              </div>
            </div>
          </div>
        </b-row>
      </b-container>
    </b-container>
  </div>
</template>
<script>
export default {
  name: "v-services",
  data() {
    return {
      services: [
        {
          // url: require("../assets/images/stat1.png"),
          title: "calculate",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-calculator icon",
          h: "height:350px",
        },
        {
          // url: require("../assets/images/stat2.png"),
          title: "web development",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesettinCDSSbvjdin dfbidjvidbvkf sduivsivgs  svisvbskhbbvis cvsbh industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-laptop icon",
          h: "height:450px",
        },
        {
          // url: require("../assets/images/stat1.png"),
          title: "chat-bot",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-comments icon",
          h: "height:350px",
        },
      ],
    };
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.icon {
  font-size: 45px;
  color: $blu;
  &:hover {
    color: $ylw;
  }
}

.box2 {
  background-color: #FFE480;
    overflow: hidden;
    position: relative;
    margin: 0.25em auto;
    // max-width: 15em;
    // min-height: 10em;
    border-radius: 1em;
    &:before {
      // position: absolute;
      margin: 8em;
      padding: 7em;

      border-radius: 50%;
      box-shadow: 0 0 0 350px rgba(#A3CEF1, 1);
      content: "";
    }
}
</style>