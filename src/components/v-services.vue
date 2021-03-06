<template>
  <div class="v-services">
    <div class="container">
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          our<span>services</span>
        </h1>
      </div>
      <b-container fluid class="p-0 w-100">
        <b-row align-v="center" class="justify-content-center">
          <b-col lg >
            <b-img center
            
              class="animated-img w-75"
              :src="require('../assets/images/home.svg')"
            />
          </b-col>
          <b-col lg sm>
            <div v-for="service in services" :key="service">
              <b-container fluid >
                <b-row align-v="center" class="justify-content-center">
                  <b-col cols="2" md="2"  class="text-center ">
                    <i :class="service.icon"></i>
                  </b-col>
                  <b-col cols="14" md="10" >
                    <h4 class="text-uppercase font-weight-bolder">{{ service.title }}</h4>
                    <p>{{ service.text }}</p>
                  </b-col>
                </b-row>
              </b-container>
            </div>
          </b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<script>
export default {
  name: "v-services",
  data() {
    return {
      services: [
        {
          title: "calculate",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-calculator chart-icon",
        },
        {
          title: "web development",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-laptop laptop-icon",
        },
        {
          title: "chat-bot",
          text:
            "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever.",
          icon: "fa fa-comments chat-icon",
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
  font-size: 4.5vw;
  color: $blu;
  &:hover {
    color: $ylw;
    animation: up-down 1s ease-in-out infinite alternate-reverse both;
  }
}
.animated-img {
  animation: up-down 2s ease-in-out infinite alternate-reverse both;
}
@-webkit-keyframes up-down {
  0% {
    transform: translateY(10px);
  }
  100% {
    transform: translateY(-10px);
  }
}
</style>