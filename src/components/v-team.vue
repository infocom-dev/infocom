<template>
  <div class="v-team">
    <b-container >
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          our<span>team</span>
        </h1>
      </div>

      <b-container fluid>
        <b-row align-v="center" class="justify-content-center">
          <div v-for="mate in team" :key="mate.name">
            <b-card
              :title="mate.name"
              :img-src="mate.url"
              img-alt="Image"
              img-top
              tag="article"
              style="max-width: 20rem"
              class="mb-2"
            >
              <b-card-text>
                <h4>{{ mate.prof }}</h4>
                <p>{{ mate.info }}</p>
              </b-card-text>
              <b-row align-v="center" class="justify-content-center">
                <div v-for="icon in mate.link" :key="icon">
                  <i :class="icon"></i></div
              ></b-row>
            </b-card>
          </div>
        </b-row>
      </b-container>
      
    </b-container>
    <b-container fluid class="after w-100 mx-0 px-0"></b-container>
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
<style lang="scss">
@import "../assets/styles/base.scss";
.v-team {
  background: url(../assets/images/03.jpg) center center no-repeat fixed;
  background-size: auto;
  background-size: cover;
  .after {
  content: "";
  background-image: url('data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1" preserveAspectRatio="none"><polygon style="fill:white;" points="0.5,0.5 1,1 0,1 "/></svg>');
  background-size: 30px 30px;
  height: 30px;
  background-color:transparent;
}
}
.insta-icon,
.vk-icon,
.mail-icon,
.twitter-icon,
.facebook-icon,
.google-icon {
  font-size: 70px;
  color: $blu;
  line-height: 50px;
  padding: 10px;
  &:hover {
    color: $ylw;
  }
}

</style>