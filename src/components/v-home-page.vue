<template>
  <div class="v-home-page">
      <div class = "navigation">
          <div class = "logo">
              <h1>INFO<span>COM</span></h1>
          </div>
           <div class="menu">
                <ul class="nav">
                   <li class="link">HOME</li>
                   <li class="link">SERVICE</li>
                   <li class="link">TEAM</li>
                   <li class="link">CONTACT</li>
                </ul>
            </div>
      </div>      
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
            <a class="button">Click here</a>
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
export default {
  name: 'v-home-page',
  components: {
    Slider,
    SliderItem,
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
  margin: 0;
  font-family: 'Lato', sans-serif;
  background: linear-gradient(rgba(32, 32, 32, 0.8),rgba(0, 1, 37, 0.4)),url('../assets/images/background.jpeg') no-repeat center center;;
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
  background: rgba(32, 26, 26, 0.6);
  padding-top: 20px;
  h1{
    font-size: 100px;
    letter-spacing:5px
  }
  span{
    font-size: 80px;
  }

}



</style>