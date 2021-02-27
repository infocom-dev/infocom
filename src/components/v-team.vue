<template>
  <div class="v-team">
    <div class="header-section">
      <h1>our<span>team</span></h1>
    </div>
    <div class="container-adapt">
      <div v-for="mate in team" :key="mate.name">
        <div class="container-item">
          <figure class="image">
            <img :src="mate.url" />
          </figure>
          <div class="cover">
            <h1>{{ mate.name }}</h1>
            <h4>{{ mate.prof }}</h4>
            <p>{{ mate.info }}</p>
            <div class="link">
              <div v-for="icon in mate.link" :key="icon">
                <i :class="icon"></i>
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
  name: "v-team",
  data() {
    return {
      team: [
        {
          name: "Vasily Pupkin",
          prof: "Web Designer",
          info:
            "text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever",
          link: ["fab fa-instagram insta-icon", "fab fa-vk vk-icon"],
          url: require("../assets/images/team2.jpg"),
        },
        {
          name: "Vasily Pupkin",
          prof: "Web Designer",
          info:
            "text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever",
          link: ["fab fa-instagram insta-icon", "fab fa-vk vk-icon"],
          url: require("../assets/images/team2.jpg"),
        },
        {
          name: "Vasily Pupkin",
          prof: "Web Designer",
          info:
            "text of the printing and typesetting industry. Lorem Ip sum has been the industry's standard dummy text ever",
          link: ["fa fa-envelope mail-icon", "fab fa-vk vk-icon"],
          url: require("../assets/images/team2.jpg"),
        },
      ],
    };
  },
};
</script>