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
        <a href="#" class="button">Click here</a>
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

<style lang="scss">
@import url('https://fonts.googleapis.com/css?family=Lato:400,700');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:400,700,600');
h1,h3{
  color:white;
  font-size: 40px;
}
h1 span{
  color:red;
  font-size: 30px;
}
// h3{
//   color:white;
//   font-size: 30px;
// }
p{
  color:white;
  font-size:30px;
}
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
.navigation{
    background: rgba(32, 26, 26, 0.65) !important;
    position: absolute;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    //margin: 0 ;
    top: 0%;
    color: #ffffff;
    
}
menu{
  display: flex;
}
.nav{
  display: flex;
  list-style: none;
}
.nav li{
  color: red;
  text-decoration: none;
  min-height: 0 30px 0 0;
  font-size: 20px;
  padding: 28px 15px;
  //padding: 40px 15px 30px;
  margin: 0 50px 0 0;
}
.logo{
  //padding: 28px 15px;
  padding: 0 100px;
  //font-size: 700;
  
}
.logo span {
  //color: #f20101;
	font-weight: 700;
}

.nav li {
    display: inline-block;
   // color: #76431f;
    line-height: 1;
    text-decoration: none;
    cursor: pointer;
    position: relative;
}
.nav li:after {
    display: block;
    content: "";
    background-color: red;;
    height: 1px;
    width: 0%;
    left: 50%;
    position: absolute;
    -webkit-transition: width .3s ease-in-out;
    -moz--transition: width .3s ease-in-out;
    transition: width .3s ease-in-out;
    -webkit-transform: translateX(-50%);
    -moz-transform: translateX(-50%);
    transform: translateX(-50%);
}
.nav li:hover:after,
.nav li:focus:after {
    width: 100%;
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
  //opacity:0.6;
  h1{
    font-size: 100px;
    letter-spacing:5px
  }
  span{
    font-size: 80px;
  }

}
a.button{
 color:red;
 padding: 20px 30px;
 width:200px;
 text-decoration:none;
 text-align:center;
 margin:0 auto;
 display: block;
 background-image: linear-gradient(to left,transparent,transparent 50%,red 50%,red);
 background-position: 100% 0;
 background-size: 200% 100%;
 transition: all .25s ease-in;
 font: 400 18px tahoma;
 border: 1px solid red;
}
a.button:hover {
background-position: 0 0;
color:#fff;
}


</style>