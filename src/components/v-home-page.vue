<template>
  <div class="v-home-page">
    <section class="home">
      <v-navigation-wrapper></v-navigation-wrapper>
      <div class="slider-container">
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
      </div>
    </section>
    <section class="service">
      <div class="header-section">
        <h1>our<span>services</span></h1>
      </div>
      <div class="container-adapt">
        <div class="service-item">
          <i class="fa fa-calculator chart-icon" aria-hidden="true"></i>
          <hr>
          <h4>Calculate </h4>
          <p>Calculate current cost of your own project</p>
          <button>more</button>
        </div>
        <div class="service-item">
          <i class="fa fa-laptop laptop-icon"></i>
          <hr />
          <h4>web development</h4>
          <p>
            lalaaa lalalffffal  laalalal alalaalal lalall
          </p>
          <button>more</button>
        </div>
        <div class="service-item">
          <i class="fa fa-comments chat-icon" aria-hidden="true"></i>
          <hr />
          <h4>chat-bot </h4>
          <p>
             Telegram and vk bot development vvfff
          </p>
          <button>more</button>
        </div>

        <div class="service-item">
          <i class="fa fa-database data-icon" aria-hidden="true"></i>
          <h4>lalala</h4>
          <p>
             Какой то текстю.lalal all lal alalla fflflflf
          </p>
          <button>more</button>
        </div>
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
    return {};
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
  background: url("../assets/images/10.jpg") no-repeat center center;
  background-size: cover;
  position: relative;
  flex-direction: column;
  height: 700px;
}

.slider-container {
  width: 100vw;
  height: 50vh;
  top: 25%;
  position: relative;
  .slider {
    width: 300%;
    height: 100%;
    position: absolute;

    transform: translateX(0);
    animation: slide1 15s infinite;

    button {
      width: 200px;
    }

    .slide {
      width: 33.333333333%;
      height: 100%;
      float: left;
      position: relative;
      display: flex;
      justify-content: center;
      // margin:60px auto;
      // &:nth-child(1){
      //   background: url(https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&fm=jpg&s=97cb7cd5e219e932365f3bcff3950eda) no-repeat center;
      //       background-size: cover;
      // }

      // &:nth-child(2){
      //   background: url(https://images.unsplash.com/photo-1432836431433-925d3cc0a5cd?q=80&fm=jpg&s=97a1e6c0e5adecf5dc6d53e17d6bc581) no-repeat center;
      //       background-size: cover;
      // }
      // &:nth-child(3){
      //   background: url(https://images.unsplash.com/photo-1428278953961-a8bc45e05f72?q=80&fm=jpg&s=24f29a71c4de9b922e7ee2cb5ee46f4b) no-repeat center;
      //       background-size: cover;
      // }

      img {
        display: block;
        max-width: 100%;
        height: auto;
      }

      .slide-text {
        text-align: center;
        display: inline-block;
        position: absolute;
        align-self: center;
        justify-content: center;
        top: 50%;
        font-family: arial, Helvetica;
        // text-transform: uppercase;
        font-size: 2.5vw;

        padding: 5px;
        transform: translateY(-50%);
        // h1 {
        //   font-size: 70px;
        //   letter-spacing: 5px;
        // }
        // span {
        //   font-size: 50px;
        // }
        //opacity:0;
        //animation-delay: 0.2s;
      }
    }
  }
}
@media all and (min-width: 200px) {
  .slide-text {
  h1, h3 {
    font-size: 25px;
    letter-spacing: 1px;
  }
  span {
    font-size: 20px;
  
  }
  p{
    font-size: 20px;
  }
  button{
    padding: 6px 10px 0;
    border-radius: 0;
    font-weight: 700;
    font-size:18px;
  }
  }
}

@media all and (min-width: 400px) {
  .slide-text {
  h1, h3 {
    font-size: 50px;
    letter-spacing: 1px;
  }
  span {
    font-size: 40px;
  
  }
  p{
    font-size: 25px;
  }
  button{
    padding: 6px 10px 0;
    border-radius: 0;
    font-weight: 700;
    font-size:25px;
  }
  }
}
@media all and (min-width: 1400px) {
  .slider-container {
    min-height: 80vh;
    top: 10%;
  }
  .slide-text {
  h1, h3 {
    font-size: 50px;
    letter-spacing: 1px;
  }
  span {
    font-size: 40px;
  
  }
  p{
    font-size: 25px;
  }
  button{
    padding: 6px 10px 0;
    border-radius: 0;
    font-weight: 700;
    font-size:25px;
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
  background-color: #EBEEEE;
  color: #fff;
  // height: 400px;
  margin: 0 auto;
  align-content: center;
  padding-right: 50px;
  padding-left: 50px;
  margin-right: auto;
  margin-left: auto;
}
.header-section{
  text-transform: uppercase;
  text-align: center;
  padding:25px;
}

.container-adapt {
  margin: 1.5em 0;
  padding: 0 ;
  column-gap: 1.5em; /* Общее расстояние между колонками */
  font-size: 0.85em;
  -moz-column-gap: 1.5em; /* Расстояние между колонками для Firefox */
  -webkit-column-gap: 1.5em; /* Расстояние между колонками  для Safari, Chrome и iOS */
  // margin-bottom: 0;
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
  box-shadow: 2px 2px 4px 0 #ccc; /* Внешняя тень плиток */
  border: 2px solid $red;
  // margin-top: 50px;
  transition: all 0.6s;
  text-align: center;
  p {
    line-height: 24px;
    // padding: 10px;
    color: #1438A6;
    font-size: 15px;
    margin: 0 0 10px;
  }
  h4 {
    font-size: 18px;
    color:$white;
    padding-bottom: 10px;
    margin-top: 10px;
    text-transform: uppercase;
  }
  button {
    padding: 6px 10px 0;
    border-radius: 0;
    font-weight: 700;
    text-transform: uppercase;
  }
}
img,
iframe {
  max-width: 100%;
  height: auto;
  display: block;
}
.laptop-icon,
.data-icon,
.chart-icon,
.chat-icon {
  font-size: 80px;
  color: $red;
  line-height: 50px;
  padding:10px;
}
@media only screen and (min-width: 400px) {
  .container-adapt {
    -moz-column-count: 2;
    -webkit-column-count: 2;
    column-count: 2;
  }
}

// @media only screen and (min-width: 600px) {
//   .container-adapt {
//     -moz-column-count: 3;
//     -webkit-column-count: 3;
//     column-count: 3;
//   }
// }

@media only screen and (min-width: 850px) {
  .container-adapt {
    -moz-column-count: 4;
    -webkit-column-count: 4;
    column-count: 4;
  }
}

@media only screen and (min-width: 1280px) {
  .service {
    width: 100%;
  }
}
</style>