<template>
  <div class="v-services">
    <div class="header-section">
      <h1>our<span>services</span></h1>
    </div>
    <div class="container-adapt">
      <div class="container-item">
        <figure class="image">
          <img class="animated-img" src="../assets/images/home.svg" />
        </figure>
      </div>
      <div class="container-item">
        <div v-for="service in services" :key="service">
          <div class="content-container">
            <div class="row">
              <div class="icon">
                <i :class="service.icon"></i>
              </div>
              <div class="text">
                <h4>{{ service.title }}</h4>
                <p>{{ service.text }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
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
</style>