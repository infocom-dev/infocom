<template>
    <div class = "v-question">
      <!-- <v-navigation-wrapper></v-navigation-wrapper>
      <div class="container">
        <article>
          <header>
            <div class="progress">
          <div class="progress-step"
          :class='{
            "active": index === activeStep
            }'
          v-for="(step, index) in questions"
          :key="'step'+index">
            {{ index + 1 }}
          </div>
        </div>

          </header>
          
          <section :class="animation">
            <div v-if="done" class="done_page">
              <h1>Thank you</h1>
            </div>
            <div v-else-if="!start" class="start_page">
              <h1>Welcome to our form</h1>
              <button @click="startForm">Start</button>
            </div>
            <h2 v-else-if="start"><v-question-item v-bind:question_data="questions[activeStep]"
                                 v-bind:questions_len="questions.length"
                                 v-model="checkedValue"
                                 v-on:send-answer="userAnswers"
                                 >
            </v-question-item></h2>
              
          </section>
          
        </article>
      </div> -->
      
    

    </div>
</template>

<script>
// import vNavigationWrapper from './v-navigation-wrapper'
import axios from 'axios'
// import VQuestionItem from './v-question-item.vue'

export default {
  name: 'v-question',
  props: {},
  components:{
    // vNavigationWrapper,
    // VQuestionItem
  },
  data(){
    return {
      start:false,
      done:false,
      questions:[],
      activeStep :0,
    }
  },
  mounted () {
    axios
    .get('hello/')
    .then(response => {
      this.questions = response.data;
    })
  },
 
  methods:{
    userAnswers(answers,step){    
      if(this.activeStep > step){
        this.activeStep -=1;
      } else if (step === this.questions.length) {
        this.start = !this.start;
        this.done = !this.done;
      } else {
        this.activeStep +=1;
      } 

      
    },
    checkFields(){
      
    },
    startForm(){
      this.start = !this.start;
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
@import '../assets/styles/base.scss';
@import '../assets/styles/fonts.scss';

@import '../assets/styles/button.scss';
@mixin flexbox(){
  display: flex;
  justify-content: center;
  align-items: center;
}
.v-question{
  @include flexbox();
  position: relative;
  flex-direction: column;
  margin: 0 auto;
  width: 100%;
  min-height: 100vh;
  font-family: 'Lato', sans-serif;
  // background: linear-gradient(rgba(32, 32, 32, 0.8),rgba(0, 1, 37, 0.4)),url('../assets/images/background.jpeg') no-repeat center center;

}
.container{
  align-items: center;

}
article{
  //align-items: center;
  display: flex;
  
  width: 1000px;
  margin: 10px;
  // width: calc(100% - 20 px);
  max-width: 800px;
  min-height: 480px;
  perspective: 1000px;

  header{
    
    @include flexbox();
    right: 100px;
    //align-items: center;
    margin: 0 auto;
    width: 60px;
    height: 500px;
    align-items: center;
    text-align: center;
    background-color:  rgba(32, 26, 26, 0.8);
    border-right: 2px dotted $blu;
    box-shadow: 0 15px 30px rgba(0,0,0,.2),
                0 15px 10px rgba(0,0,0,.2);
  }
  .progress-step{
    @include flexbox();
    
    position: relative;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    margin-bottom: 10px;
    color: $wht;
    background-color: black;
    font-weight: bold;
    &.active {
      background-color:$blu;
    
      ~ .progress-step {
        color: black;
        background-color: #ccc;
      }
      ~ .progress-step::before {
        background-color: #ccc;
      }
    
    }
  }
    section{
      @include flexbox();
      // flex-direction: column;
      width:1200px;
      background:  rgba(32, 26, 26, 0.8);
      box-shadow: 0 15px 30px rgba(0,0,0,.2),
                  0 15px 10px rgba(0,0,0,.2);
  }
}
.start_page {
  button{
    width:  200px;
  }
}
</style>
