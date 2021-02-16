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
  display: flex;
  height: 700px;
}
.slider{
  margin:0 auto; 
}
.slider-item{
  display: flex;
  justify-content: center;
  margin:60px auto;
  text-align: center;
  background: $bg;
  // background: rgba(#262626,0.3);
  padding-top: 20px;
  h1{
    font-size: 100px;
    letter-spacing:5px
  }
  span{
    font-size: 80px;
  }

}
.button{
  button{
    width: 200px;
  }
}



</style>