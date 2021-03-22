<template>
  <div class="v-services">
    <b-container fluid class="w-100">
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          our<span>services</span>
        </h1>
      </div>
      <b-container fluid class="w-100 justify-content-center">
        <b-row align-v="center" class="justify-content-center">
          <div v-for="service in services" :key="service">
            <div
              class="col m-5 text-center box "
              style="width: 350px"
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
          icon: "fa fa-calculator chart-icon",
          h: "height:300px",
        },
        {
          // url: require("../assets/images/stat2.png"),
          title: "web development",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesettinCDSSbvjdin dfbidjvidbvkf sduivsivgs  svisvbskhbbvis cvsbh industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-laptop laptop-icon",
          h: "height:350px",
        },
        {
          // url: require("../assets/images/stat1.png"),
          title: "chat-bot",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-comments chat-icon",
          h: "height:300px",
        },
      ],
    };
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.laptop-icon,
.data-icon,
.chart-icon,
.chat-icon {
  font-size: 50px;
  color: $blu;
  &:hover {
    color: $ylw;
  }
}

.box {
  // background: url("../assets/images/stat.png") center;
  background-color: #A3CEF1;
  // border-radius: 0% 40% 10% 33% / 10% 30% 0% 33% ;
  // border-radius: 40% 23% 61% 35% / 38% 35% 43% 20%      ;
  border-radius: 40px;
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2)  ; 
	-webkit-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2)  ; 
	-moz-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2)  ; 
  
  
  justify-content: center;
  align-items: center;
}
</style>