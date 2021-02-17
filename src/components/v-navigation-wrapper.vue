
<template>
<div class="v-navigation-wrapper">
    <div class="menu-wrap">
       <div class = "logo">
              <h1>INFO<span>com</span></h1>
          </div>
          <!-- <input type="checkbox" id="checkbox"> -->
       <nav v-if="state">
           <ul>
               <li><a href="#">Home</a></li>
               <li><a href="#">About</a></li>
               <li><a href="#">Services</a></li>
               <li><a href="#">Contact</a></li>
               <!-- <button @click="myFunction"></button> -->
           </ul>
       </nav>
       <!-- <button @click="myFunction"></button> -->
       
       <button @click="myFunction">
           <i  class="fa fa-bars menu-icon"  ></i>
       </button>

   </div>
    <!-- <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <div class = "navigation">
          <div class = "logo">
              <h1>INFO<span>com</span></h1>
          </div>
          <input type="checkbox" id="checkbox">
           <div class="menu">
                <ul class="nav">
                   <li><a class="link">HOME</a></li>
                   <li><a class="link">SERVICE</a></li>
                   <li><a class="link">TEAM</a></li>
                   <li><a class="link">CONTACT</a></li>
                </ul>
            </div>
            
            <i class="fa fa-bars menu-icon"><input type="checkbox" id="checkbox"></i>
      </div>
       -->
    
</div>
    
</template>

<script >

export default {
name:"v-navigation-wrapper",
data(){
    return{
        state:true
    }
},
methods:{
    myFunction() {
    this.state = !this.state;
}
}
}


</script>
<style lang="scss" >
* {
   margin: 0;
   padding: 0;
   box-sizing: border-box;
   font-family: sans-serif;
   
}
</style>