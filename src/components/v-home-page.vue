<template>
  <div class="v-home-page">
    <section class="home">
      <div class="home-skew-border">
        <v-navigation-wrapper></v-navigation-wrapper>
        <div class="container">
          <h3>Our Clients Are Our First Priority</h3>
          <h1>WELCOME TO BINO</h1>
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
      <!-- <div class="slider-container">
        <div class="slider">
          <div class="slide">
            <div class="slide-text">
              <h1>Need a <span>chat bot</span>?</h1>

              <router-link :to="{ name: 'anketa' }">
                <button>Click here</button>
              </router-link>

              <p>Fill out the form and find out the price!</p>
            </div>
          </div>
          <div class="slide">
            <div class="slide-text">
              <h1>INFO<span>COM</span></h1>
              <h3>WEB DEVELOPMENT SOLUTIONS</h3>
              <p></p>
            </div>
          </div>
          <div class="slide">
            <div class="slide-text"></div>
          </div>
        </div>
      </div> -->
    </section>
    <section class="service">
      <div class="header-section">
        <h1>our<span>services</span></h1>
      </div>
      <div class="container-adapt">
        <div class="service-item">
          <div class="content-container">
            <div class="row">
              <div class="text">
                <h4>Calculate</h4>
                <p>
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ip sum has been the industry's
                  standard dummy text ever.
                </p>
              </div>
              <div class="icon">
                <i class="fa fa-calculator chart-icon"> </i>
              </div>
            </div>
          </div>
          <div class="content-container">
            <div class="row">
              <div class="text">
                <h4>web development</h4>
                <p>
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ip sum has been the industry's
                  standard dummy text ever.
                </p>
              </div>
              <div class="icon">
                <i class="fa fa-laptop laptop-icon"></i>
              </div>
            </div>
          </div>
          <div class="content-container">
            <div class="row">
              <div class="text">
                <h4>chat-bot</h4>
                <p>
                  Lorem Ipsum is simply dummy text of the printing and
                  typesetting industry. Lorem Ip sum has been the industry's
                  standard dummy text ever.
                </p>
              </div>
              <div class="icon">
                <i class="fa fa-comments chat-icon"></i>
              </div>
            </div>
          </div>
        </div>
        <div class="service-item">
          <figure class="image is-fullwidth">
            <img class="animated-img" src="../assets/images/home.svg" />
          </figure>
        </div>
        <!-- <div class="service-item">
          <i class="fa fa-laptop laptop-icon"></i>
          <hr />
          <h4>web development</h4>
          <p>lalaaa lalalffffal laalalal alalaalal lalall</p>
          <button>more</button>
        </div>
        <div class="service-item">
          <i class="fa fa-comments chat-icon" aria-hidden="true"></i>
          <hr />
          <h4>chat-bot</h4>
          <p>Telegram and vk bot development vvfff</p>
          <button>more</button>
        </div> -->

        <!-- <div class="service-item">
          <i class="fa fa-database data-icon" aria-hidden="true"></i>
          <h4>lalala</h4>
          <p>
             Какой то текстю.lalal all lal alalla fflflflf
          </p>
          <button>more</button>
        </div> -->
      </div>
    </section>
    <section class="promo-banner">
      <div class="promo-container">
        <h2>Displaying the Result</h2>
        <p class="promo-banner-text">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo.
        </p>
      </div>
    </section>
    <section class="skills">
      <div class="header-section">
        <h1>SKILLS<span></span></h1>
      </div>
      <div class="box">
        <ul>
          <li v-for="skill in skills" :key="skill">
            <div class="lang">{{ skill.lang }}</div>
            <div class="bar">
              <div
                class="progress"
                v-bind:style="{
                  background: skill.color,
                  width: skill.percent + '%',
                  'animation-name': 'progress',
                  'animation-delay': '0.7s',
                }"
              ></div>
              <span class="percent">{{ skill.percent }}%</span>
            </div>
          </li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
// import { Slider, SliderItem } from 'vue-easy-slider'
import vNavigationWrapper from "./v-navigation-wrapper";
import VNavigationWrapper from "./v-navigation-wrapper.vue";

export default {
  name: "v-home-page",
  components: {
    // Slider,
    // SliderItem,
    vNavigationWrapper,
    VNavigationWrapper,
  },
  data() {
    return {
      skills: [
        { lang: "PYTHON", percent: 90, color: "#ec407a" },
        { lang: "MYSQL", percent: 76, color: "#f4511e" },
        { lang: "JAVASCRIPT", percent: 84, color: "#512da8" },
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
  background: url("../assets/images/06.jpg") no-repeat center center;
  background-size: cover;
  position: relative;
  flex-direction: column;
  height: 770px;
  font-size: 1rem;
}
.home-skew-border{
    // position: relative;

}
.home-skew-border:after{
    position: absolute;
    left:0;
    bottom:0;
    content: "";
    width: 0;
    height: 0;
    border-bottom: 86px solid #fff;
    border-right: 680px solid transparent;

}
.home-skew-border:before{
    position: absolute;
    right:0;
    bottom:0;
    content: "";
    width: 0;
    height: 0;
    border-bottom: 86px solid #fff;
    border-left: 680px solid transparent;
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
    background: $rs;
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
    background: #eee;
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
    background: #eee;
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
  }
  // .service {
  //   padding-right: 150px;
  //   padding-left: 150px;
  // }
}
// .slider-container {
//   width: 100vw;
//   height: 50vh;
//   top: 25%;
//   position: relative;
//   .slider {
//     width: 300%;
//     height: 100%;
//     position: absolute;
//     transform: translateX(0);
//     animation: slide1 15s infinite;
//     button {
//       width: 200px;
//     }
//     .slide {
//       width: 33.333333333%;
//       height: 100%;
//       float: left;
//       position: relative;
//       display: flex;
//       justify-content: center;
//       // margin:60px auto;
//       // &:nth-child(1){
//       //   background: url(https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&fm=jpg&s=97cb7cd5e219e932365f3bcff3950eda) no-repeat center;
//       //       background-size: cover;
//       // }
//       // &:nth-child(2){
//       //   background: url(https://images.unsplash.com/photo-1432836431433-925d3cc0a5cd?q=80&fm=jpg&s=97a1e6c0e5adecf5dc6d53e17d6bc581) no-repeat center;
//       //       background-size: cover;
//       // }
//       // &:nth-child(3){
//       //   background: url(https://images.unsplash.com/photo-1428278953961-a8bc45e05f72?q=80&fm=jpg&s=24f29a71c4de9b922e7ee2cb5ee46f4b) no-repeat center;
//       //       background-size: cover;
//       // }
//       img {
//         display: block;
//         max-width: 100%;
//         height: auto;
//       }
//       .slide-text {
//         text-align: center;
//         display: inline-block;
//         position: absolute;
//         align-self: center;
//         justify-content: center;
//         top: 50%;
//         font-family: arial, Helvetica;
//         // text-transform: uppercase;
//         font-size: 2.5vw;
//         padding: 5px;
//         transform: translateY(-50%);
//         // h1 {
//         //   font-size: 70px;
//         //   letter-spacing: 5px;
//         // }
//         // span {
//         //   font-size: 50px;
//         // }
//         //opacity:0;
//         //animation-delay: 0.2s;
//       }
//     }
//   }
// }
@media all and (min-width: 200px) {
  .slide-text {
    h1,
    h3 {
      font-size: 25px;
      letter-spacing: 1px;
    }
    span {
      font-size: 20px;
    }
    p {
      font-size: 20px;
    }
    button {
      padding: 6px 10px 0;
      border-radius: 0;
      font-weight: 700;
      font-size: 18px;
    }
  }
}

@media all and (min-width: 400px) {
  .slide-text {
    h1,
    h3 {
      font-size: 50px;
      letter-spacing: 1px;
    }
    span {
      font-size: 40px;
    }
    p {
      font-size: 25px;
    }
    button {
      padding: 6px 10px 0;
      border-radius: 0;
      font-weight: 700;
      font-size: 25px;
    }
  }
}
@media all and (min-width: 1400px) {
  .slider-container {
    min-height: 80vh;
    top: 10%;
  }
  .slide-text {
    h1,
    h3 {
      font-size: 50px;
      letter-spacing: 1px;
    }
    span {
      font-size: 40px;
    }
    p {
      font-size: 25px;
    }
    button {
      padding: 6px 10px 0;
      border-radius: 0;
      font-weight: 700;
      font-size: 25px;
    }
  }
}

@keyframes slide1 {
  27% {
    transform: translateX(0);
  }
  33% {
    transform: translateX(-33.3333333333%);
  }
  60% {
    transform: translateX(-33.3333333333%);
  }
  66% {
    transform: translateX(-66.6666666666%);
  }

  94% {
    transform: translateX(-66.6666666666%);
  }

  100% {
    transform: translateX(0);
  }
}

.service {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  background: $wht;
  background-size: auto;
  background-size: cover;
  min-height: 100%;
  // background-color: url(../assets/images/10.jpg);
  color: $wht;
  // height: 400px;
  margin: 0 auto;
  align-content: center;
  // margin-bottom: 1px;
  // padding-right: 50px;
  // padding-left: 50px;
  margin-right: auto;
  margin-left: auto;
}
.header-section {
  text-transform: uppercase;
  text-align: center;
  padding: 25px;
}

.container-adapt {
  // display: flex;

  margin: 1.5em 0;
  padding: 0;
  column-gap: 0em; /* Общее расстояние между колонками */
  font-size: 0.85em;
  -moz-column-gap: 1.5em; /* Расстояние между колонками для Firefox */
  -webkit-column-gap: 1.5em; /* Расстояние между колонками  для Safari, Chrome и iOS */
  // margin-bottom: 0;
}
.row {
  width: 100%;
  display: flex;
}
.text {
  text-align: right;
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
.service-item {
  display: inline-block;
  padding: 1em;
  margin: 0 0 1.5em;
  width: 100%;
  box-sizing: border-box; /* Изменения алгоритма расчета ширины и высоты элемента.*/
  -moz-box-sizing: border-box; /* Для Firefox */
  -webkit-box-sizing: border-box; /* Для Safari, Chrome, iOS иAndroid */
  // box-shadow: 2px 2px 4px 0 #ccc; /* Внешняя тень плиток */
  // border: 2px solid $red;
  height: 100%;
  // margin-top: 50px;
  transition: all 0.6s;
  // text-align: right;
  background-color: $wht;
  p {
    line-height: 24px;
    // padding: 10px;
    color: $blu;
    font-size: 15px;
    margin: 0 0 10px;
  }
  h4 {
    // .service {
    //   padding-left: 150px;
    //   padding-right: 150px;
    // }
    // .skills {
    //   padding-right: 150px;
    //   padding-left: 150px;
    // }
    font-size: 18px;
    color: $rs;
    padding-bottom: 10px;
    margin-top: 10px;
    text-transform: uppercase;
  }
}
img,
iframe {
  width: 90%;
  height: auto;
  display: block;
  text-align: center;
}
.laptop-icon,
.data-icon,
.chart-icon,
.chat-icon {
  font-size: 70px;
  color: $rs;
  line-height: 50px;

  padding: 10px;
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

// @media only screen and (min-width: 700px) {
//   .container-adapt {
//     -moz-column-count: 3;
//     -webkit-column-count: 3;
//     column-count: 3;
//   }
// .service {
//   padding-left: 150px;
//   padding-right: 150px;
// }
// .skills {
//   padding-right: 150px;
//   padding-left: 150px;
// }
//}

// @media only screen and (min-width: 850px) {
//   .container-adapt {
//     -moz-column-count: 4;
//     -webkit-column-count: 4;
//     column-count: 4;
//   }
// }

@media only screen and (min-width: 1280px) {
  .service {
    width: 100%;
  }
}

.promo-banner {
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  background: url(../assets/images/05.jpg) center center no-repeat fixed;
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
.skills {
  // background-color: #fff;
  // color: #fff;
  // //height: 400px;
  margin: 0 auto;
  align-content: center;
  padding-right: 50px;
  padding-left: 50px;
  // margin-right: auto;
  // margin-left: auto;
  position: relative;
  z-index: 1;
  box-sizing: border-box;
  background: url(../assets/images/03.jpg) center center no-repeat fixed;
  background-size: auto;
  background-size: cover;
  min-height: 100%;
}
.box {
  // width: 800px;
  padding: 40px;
  // margin: 50px auto;
  background: #2d3e73;
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
  background: #555;
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
</style>