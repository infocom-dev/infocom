<template>
  <div class="v-home-page">
    <section class="home">
      <div class="home-skew-border">
        <v-navigation-wrapper></v-navigation-wrapper>
        <div class="container">
          <h3>Our Clients Are Our First Priority</h3>
          <h1>WELCOME TO INFOCOM</h1>
          <div class="separator"></div>
          <p>
            Lorem Ipsum is simply dummy text of the printing and typesetting
            industry. Lorem Ipsum has been the industry's standard dummy text
            ever since the 1500s, when an unknown printer took a galley of type
            and scrambled it to make a type specimen book.
          </p>
          <div class="home_btn">
            <button>GET STARTED NOW</button>
          </div>
        </div>
      </div>
    </section>
    <section class="service">
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
    </section>
    <!-- <section class="promo-banner">
      <div class="promo-container">
        <h2>Displaying the Result</h2>
        <p class="promo-banner-text">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo.
        </p>
      </div>
    </section> -->
    <section class="team">
      <!-- <div class="team-skew-border"> -->
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
    </section>
    <section class="skills">
      <div class="header-section">
        <h1>STACK<span>skills</span></h1>
      </div>
      <div class="container-adapt">
        <div class="container-item">
          <v-skills></v-skills>
          <!-- <figure class="image">
            <img class="animated-img" src="../assets/images/skills.jpg" />
          </figure> -->
        </div>
        <div class="container-item">
          <h1>
            We support challenges on all the latest stacks. Console, web or
            mobile.
          </h1>
        </div>
      </div>
    </section>
    <section class="contact-us">
      <div class="header-section">
        <h1>contact<span>us</span></h1>
      </div>
      <div class="box">
        <v-contact-us></v-contact-us>
      </div>
    </section>
  </div>
</template>

<script>
import VSkills from "./v-skills.vue";
import VNavigationWrapper from "./v-navigation-wrapper.vue";
import VContactUs from "./v-contact-us-form.vue";

export default {
  name: "v-home-page",
  components: {
    VContactUs,
    VSkills,
    VNavigationWrapper,
  },
  data() {
    return {
      skills: [
        { lang: "PYTHON", percent: 90, color: "#FFD037" },
        { lang: "MYSQL", percent: 76, color: "#FFD037" },
        { lang: "JAVASCRIPT", percent: 84, color: "#FFD037" },
      ],
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
  methods: {},
};
</script>

<style lang="scss" >
@import "../assets/styles/base.scss";
@import "../assets/styles/button.scss";
@import "../assets/styles/fonts.scss";
@import "../assets/styles/navigation.scss";
.v-home-page {
  margin: 0 auto;
  font-family: "Lato", sans-serif;
}
.home {
  background: url("../assets/images/09.jpg") no-repeat center center;
  background-size: cover;
  position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}
.home-skew-border {
  // position: relative;
}
.home-skew-border:after {
  position: absolute;
  left: 0;
  bottom: 0;
  content: "";
  width: 0;
  height: 0;
  border-bottom: 86px solid $wht;
  border-right: 680px solid transparent;
}
.home-skew-border:before {
  position: absolute;
  right: 0;
  bottom: 0;
  content: "";
  width: 0;
  height: 0;
  border-bottom: 86px solid $wht;
  border-left: 580px solid transparent;
}

.container {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;

  padding-top: 170px;
  padding-bottom: 1500px;
  text-align: center;
  box-sizing: border-box;
  padding-right: 15px;
  padding-left: 15px;
  h3 {
    -webkit-text-stroke-width: 1px;

    -webkit-text-stroke-color: black;
    font-size: 1.714em;
    line-height: 2.5rem;
    color: $blu;
  }
  h1 {
    font-size: 5.143rem;
    line-height: 5.5rem;
    color: $ylw;
    letter-spacing: 0.4rem;
  }
  .separator {
    width: 10px;
    height: 10px;
    margin: 20px auto;
    background: $ylw;
    position: relative;
    display: inline-block;
    border-radius: 50%;
  }
  .separator::before {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    direction: rtl;
    position: absolute;
    right: 5%;
    bottom: 4px;
    height: 1px;
    width: 80px;
    background: $wht;
    content: "";
    display: inline-block;
    margin-right: 20px;
  }
  .separator::after {
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    direction: rtl;
    position: absolute;
    left: 5%;
    bottom: 4px;
    height: 1px;
    width: 80px;
    background: $wht;
    content: "";
    display: inline-block;
    margin-left: 20px;
  }
  p {
    color: $wht;
    max-width: 60%;
    margin: 0 auto;
    padding-bottom: 30px;
    font-size: 1.125rem;
    line-height: 2rem;
  }
}
@media (max-width: 991px) {
  html {
    font-size: 70%;
    .team,
    .skills,
    .contact-us {
      padding-right: 50px;
      padding-left: 50px;
    }
  }
}
.service,
.skills {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  background: $wht;
  background-size: auto;
  background-size: cover;
  min-height: 100%;
  color: $wht;
  
  margin: 0 auto;
  align-content: center;
  margin-right: auto;
  margin-left: auto;
}
.header-section {
  text-transform: uppercase;
  text-align: center;
  padding: 25px;
}

.container-adapt {
  margin: 1.5em 0;
  padding: 0;
  column-gap: 0em; /* Общее расстояние между колонками */
  font-size: 0.85em;
  -moz-column-gap: 1.5em; /* Расстояние между колонками для Firefox */
  -webkit-column-gap: 1.5em; /* Расстояние между колонками  для Safari, Chrome и iOS */
  margin-bottom: 0;
}
.row {
  width: 100%;
  display: flex;
}
.text {
  text-align: left;
  width: 80%;
  float: left;
}
.icon {
  text-align: center;
  align-self: center;
  width: 20%;
  float: right;
}
/* Элементы в виде плиток с содержанием */
.container-item {
  display: inline-block;
  padding: 1em;
  margin: 0 0 1.5em;
  width: 100%;
  box-sizing: border-box; /* Изменения алгоритма расчета ширины и высоты элемента.*/
  -moz-box-sizing: border-box; /* Для Firefox */
  -webkit-box-sizing: border-box; /* Для Safari, Chrome, iOS иAndroid */
  height: 100%;
  transition: all 0.6s;
  background-color: $wht;
  p {
    line-height: 24px;
    color: $blu;
    font-size: 15px;
    margin: 0 0 10px;
  }
  h4 {
    font-size: 18px;
    color: $rs;
    padding-bottom: 10px;
    margin-top: 10px;
    text-transform: uppercase;
  }
}
img,
iframe {
  width: 100%;
  height: auto;
  display: block;
  text-align: center;
  align-self: center;
}
.laptop-icon,
.data-icon,
.chart-icon,
.chat-icon {
  font-size: 70px;
  color: $blu;
  line-height: 50px;
  padding: 10px;
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

@keyframes up-down {
  0% {
    transform: translateY(10px);
  }
  100% {
    transform: translateY(-10px);
  }
}
.skew-border {
  display: inline-block;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 0 200px 98.77vw;
  border-color: transparent transparent #f0f0f0 transparent;
  margin-bottom: -10px;
}
.promo-banner {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  // background: url(../assets/images/05.jpg) center center no-repeat fixed;
  background-size: auto;
  background-size: cover;
  min-height: 100%;
  .promo-container {
    text-align: center;
    color: $wht;
    width: 750px;
    padding-right: 15px;
    padding-left: 15px;
    margin-right: auto;
    margin-left: auto;
    padding-top: 100px;
    padding-bottom: 100px;
    h2 {
      font-weight: 700;
      color: $wht;
      margin: 0 0 15px;
    }
    p {
      font-size: 15px;
      font-weight: 400;
      color: #a6a7aa;
      margin-bottom: 15px;
    }
  }
}
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
  -moz-border-radius: $radius;
  -ms-border-radius: $radius;
  border-radius: $radius;
}
.team {
  margin: 0 auto;
  padding-bottom: 70px;
  align-content: center;
  padding-right: 150px;
  padding-left: 150px;
  // margin-right: auto;
  // margin-left: auto;
  position: relative;
  // z-index: 1;
  box-sizing: border-box;
  background: url(../assets/images/03.jpg) center center no-repeat fixed;
  background-size: auto;
  background-size: cover;
  min-height: 100%;
  color: $wht;
}
.contact-us {
  background: url(../assets/images/06.jpg);
  padding-left: 150px;
  padding-right: 150px;
  margin: 0 auto;
  padding-bottom: 70px;
  align-content: center;
    // background-image: linear-gradient(135deg, transparent 66%, white 67%),
    //                 linear-gradient(45deg, white 33%, gray 34%, transparent 44%);

}
.box {
  // width: 800px;
  // padding: 40px;
  box-shadow: 3px 3px 10px 3px rgba(0, 0, 0, 0.1);
}

ul li {
  list-style-type: none;
  padding: 10px;
}

.lang {
  margin: 5px;
  font-size: 20px;
}

.bar {
  background: $wht;
  position: relative;
  width: 100%;
  height: 5px;
  margin-top: 5px;
  display: block;
  @include border-radius(5px);
}
.progress {
  position: absolute;
  width: 0%;
  height: 100%;
  @include border-radius(5px);
  -webkit-animation-duration: 2s;
  animation-duration: 2s;
  -webkit-animation-timing-function: ease-out;
  animation-timing-function: ease-out;
  -webkit-animation-fill-mode: both;
  animation-fill-mode: both;
}
@keyframes progress {
  0% {
    width: 0%;
  }
}

.percent {
  float: right;
  font-weight: 600;
  height: 30px;
  line-height: 30px;
}
.team {
  .insta-icon,
  .vk-icon,
  .mail-icon {
    font-size: 70px;
    color: $blu;
    line-height: 50px;
    padding: 10px;
    &:hover {
      color: $ylw;
    }
  }
  .link {
    display: flex;
    justify-content: center;
  }
  img {
    width: 100%;
    height: auto;
    // display: block;
  }
  .container-item {
    position: relative;
  }
  .cover {
    position: absolute;
    left: 0;
    bottom: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.7);
    padding: 20px;
    display: none;
  }

  .container-item:hover .cover {
    display: block;
  }
}
.skills {

  padding-left: 150px;
  padding-right: 150px;
}

@media only screen and (min-width: 900px) {
  .container-adapt {
    -moz-column-count: 2;
    -webkit-column-count: 2;
    column-count: 2;
    display: flex;
    justify-content: center;
    align-items: center;
  }
}

@media only screen and (min-width: 1280px) {
  .service,
  .skills {
    width: 100%;
  }
}
</style>