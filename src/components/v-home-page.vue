<template>
  <div class="v-home-page"> 
    <v-navigation-wrapper></v-navigation-wrapper>  
       <div class="carousel">
        <slider autoplay="false" animation="fade"  width="1200px" height="500px"  >
  <slider-item 
   >
   <div class="carousel-content">
     <h1>INFO<span>COM</span></h1>
     <h3>WEB DEVELOPMENT SOLUTIONS</h3>
     <p></p>
   </div>
  </slider-item>
  <slider-item >
    <div class="carousel-content-second">
      <h1>Need a <span>chat bot</span>?</h1>
      <div class="button">
        <router-link :to="{name : 'anketa'}">
            <button>Click here</button>
        </router-link>
      </div>
      <p>Fill out the form and find out the price!</p>
   </div>
  </slider-item>
</slider>
      </div>  
       <div class="slider-container">
  <div class="slider">
    <div class="slide">
      <div class="slide-text">Slide 1 text</div>
    </div>
    <div class="slide">
      <div class="slide-text">Slide 2 text</div>
    </div>
    <div class="slide">
      <div class="slide-text">Slide 3 text</div>
    </div>
  </div>
</div> 
<section class="service">
  <h2>OUR <span>SERVICeS</span></h2>
</section>
  </div>
</template>

<script>

import { Slider, SliderItem } from 'vue-easy-slider'
import vNavigationWrapper from './v-navigation-wrapper'
import VNavigationWrapper from './v-navigation-wrapper.vue'

export default {
  name: 'v-home-page',
  components: {
    Slider,
    SliderItem,
    vNavigationWrapper,
    VNavigationWrapper
  },
  data(){
    return {  
    }
  },
  methods:{
  },

}
</script>

<style lang="scss" >


@import '../assets/styles/base.scss';
@import '../assets/styles/button.scss';
@import '../assets/styles/fonts.scss';
@import '../assets/styles/navigation.scss';
.v-home-page{
  margin: 0 auto;
  font-family: 'Lato', sans-serif;
  background: url('../assets/images/10.jpg') no-repeat center center;
  background-size: cover;
  position: relative;
  justify-content: center;
  flex-direction: column;
  //display: flex;
  height: 700px;

}
// .slider{
//   margin:0 auto; 
// }
// .slider-item{
//   display: flex;
//   justify-content: center;
//   margin:60px auto;
//   text-align: center;
//   background: $bg;
//   // background: rgba(#262626,0.3);
//   padding-top: 20px;
//   h1{
//     font-size: 100px;
//     letter-spacing:5px
//   }
//   span{
//     font-size: 80px;
//   }

// }
// .button{
//   button{
//     width: 200px;
//   }
// }

*{
  box-sizing: border-box;
}

body{
  margin:0;
}

.slider-container{
  width: 100vw;
  height: 50vh;
  overflow: hidden;
  position: relative;
  .slider{
    width: 300%;
    height: 100%;
    position: absolute;
    top:0;
    left:0;
    transform: translateX(0);
    animation: slide1 15s infinite;
    
    .slide{
      width: 33.333333333%;
      height: 100%;
      float: left;
      background: #eee;
      position: relative;
      
      &:nth-child(1){
        background: url(https://images.unsplash.com/photo-1433838552652-f9a46b332c40?q=80&fm=jpg&s=97cb7cd5e219e932365f3bcff3950eda) no-repeat center;
            background-size: cover;
      }
      
      &:nth-child(2){
        background: url(https://images.unsplash.com/photo-1432836431433-925d3cc0a5cd?q=80&fm=jpg&s=97a1e6c0e5adecf5dc6d53e17d6bc581) no-repeat center;
            background-size: cover;
      }
      &:nth-child(3){
        background: url(https://images.unsplash.com/photo-1428278953961-a8bc45e05f72?q=80&fm=jpg&s=24f29a71c4de9b922e7ee2cb5ee46f4b) no-repeat center;
            background-size: cover;
      }
      
      
      img{
        display: block;
        max-width: 100%;
        height: auto;
      }
      
      .slide-text{
        display: inline-block;
        position: absolute;
        left: 20px;
        top: 50%;
        font-family: arial, Helvetica;
        text-transform: uppercase;
        font-size: 2.5vw;
        background: #fff;
        padding: 5px;
        transform: translateY(-50%);
        //opacity:0;
        //animation-delay: 0.2s;
      }
    }
  }
}


@media all and (min-width: 1400px){
  .slider-container{
    min-height:80vh; 
  }
  
}

@keyframes slide1{
 27%{
    transform: translateX(0);
  }  
 33%{
    transform: translateX(-33.3333333333%);
  }  
  60%{
    transform: translateX(-33.3333333333%);
  }
  66%{
    transform: translateX(-66.6666666666%);
  }
  
  94%{
    transform: translateX(-66.6666666666%);
  }
  
  100%{
    transform: translateX(0);
  }
 
}

.service{
  padding: 80px 0 160px;
	background-color: #000;
	color: #fff;
}


</style>