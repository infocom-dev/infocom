<template>

    <div class= 'v-question-item'>
      <div clsass="selected" v-if="question_data.type === 'selected' ">
        <p class="v-question-item__text">{{question_data.text}} </p>
          <div>
           <multiselect v-model="selectedAnswers" 

                        placeholder="Search" 
                        label="value" track-by="id" 
                        :options="question_data.answers" 
                        :multiple="true" 
                        :taggable="true" 
                        @tag="addTag"

                        ></multiselect>
                        <h1></h1>
          </div>

      </div>

      <div v-if="question_data.type === 'checkbox' " >
        <p class="v-question-item__text">{{question_data.text}} </p>
        <label v-for="val in question_data.answers" :key="val.id">
          <p-check class="p-icon p-round p-pulse" >
             <i slot="extra" class="icon mdi mdi-check"></i>
               {{val.value}}
          </p-check>
        </label>
       </div>

      <div v-if="question_data.type === 'message' " >
        <div class="message">
        <p class="v-question-item__text">{{question_data.text}} </p>
        <input v-model="selectedAnswers" placeholder="Type here">
        </div>
      </div>

      <div v-if="question_data.type === 'range' ">
        <p class="v-question-item__text">{{question_data.text}} </p>
        <!-- <div class="set-range">
         <input type="text" v-model="value[0]" placeholder="От" class="form-control" /><br>
         <input type="text" v-model="value[1]" placeholder="До" class="form-control" /><br>
        </div>
        <br> -->
        <vue-slider :min="question_data.answers[0].value"
                    :max="question_data.answers[1].value"
                    :interval="10"
                    v-model="value"
                    :marks="marks"
                    :tooltip="'none'"
                    :process="process"
                    :process-style="{ backgroundColor: 'red' }"
                    :tooltip-style="{ backgroundColor: 'blue', borderColor: 'blue' }"
        >
          <div :class="['custom-dot', { focus }]"></div>
            <template v-slot:step="{ label, active }">
              <div :class="['custom-step', { active }]"></div>
            </template>
          <template v-slot:process="{ start, end, style, index }">
            <div class="vue-slider-process" :style="style">
              <div :class="[
                'merge-tooltip',
                'vue-slider-dot-tooltip-inner',
                'vue-slider-dot-tooltip-inner-top',
              ]">
               {{ value[index] }} - {{ value[index + 1] }}
              </div>
            </div>
          </template>
        </vue-slider>
        <br>
        
      </div>

      <div class="switch ex1" v-if="question_data.type === 'switch' " >
          <p class="v-question-item__text">{{question_data.text}} </p>
          <div class="labels">
          <label class="radio red" v-for="answer in question_data.answers"
          :key="answer.id">
          <input type="radio"
          name="selectedAnswers"
        :value="answer.value"
         v-model="selectedAnswers"/><span>{{answer.value}}</span>
         </label></div>
      </div>

      <div v-if="question_data.type === 'datapicker' " >
        <p class="v-question-item__text">{{question_data.text}} </p>
        <date-picker  v-model="selectedAnswers"
                      value-type="format"
                      format="DD.MM.YYYY"
                      range
                      placeholder="tip range"
                      confirm
                      range-separator=" - "
                      >
        </date-picker>


      </div>
      
      <div v-if="question_data.type === 'textarea'">
        <div class="message">
        <p class="v-question-item__text">{{question_data.text}} </p>
        <textarea v-model="selectedAnswers" placeholder="Type here"></textarea>
        </div>
      </div>
      <div class="actions">
              <button v-if="activeStep  < questions_len - 1 && activeStep + 1 >= 2" @click="prevStep">back</button>
              <button v-if="activeStep  < questions_len - 1" @click="nextStep"> next</button>
              <button v-if="activeStep  === questions_len - 1" @click="done">done</button>
      </div>
    </div>
</template>

<script>

 import VueSlider from 'vue-slider-component'
 import 'vue-slider-component/theme/default.css'
 import Multiselect from 'vue-multiselect'
 import DatePicker from 'vue2-datepicker';
 import 'vue2-datepicker/index.css';
//import PrettyCheckbox from 'pretty-checkbox-vue';
import 'vue-slider-component/theme/default.css'
// import 'pretty-checkbox/src/pretty-checkbox.scss';

export default {
  name: 'v-question-item',
  components: {
     VueSlider,
     Multiselect,
     DatePicker,
     //PrettyCheckbox
  },
  props:{
        question_data:{
            type:Object,
            default(){
                return{}
            }
        },
        questions_len:{
            type:Number,
        }
    },
  data(){ 
    return {
      activeStep: 0,
      value:[0,50],
      marks: val =>  val % ((this.question_data.answers[1].value-this.question_data.answers[0].value) /10) === 0,
      selectedAnswers:""
    }
  },
  methods: {
    addTag (newTag) {
      const tag = {
        value: newTag,
        id: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
      }
      this.question_data.push(tag)
      this.value.push(tag)
    },
    nextStep(){
      console.log(this.selectedAnswers)
      this.$emit('send-answer',this.selectedAnswers,this.activeStep + 1)
      this.activeStep += 1;
      this.selectedAnswers="";
    },
    prevStep(){
      console.log(this.selectedAnswers)
      this.$emit('send-answer',this.selectedAnswers,this.activeStep - 1)
      this.activeStep -= 1;
      this.selectedAnswers="";
    },
    done(){
      this.$emit('send-answer',this.selectedAnswers,this.questions_len)
      // this.activeStep = this.questions_len;
      this.selectedAnswers="";
    }
  }
} 
    
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss">
@import '../assets/styles/base.scss';
.v-question-item{
  margin:0 auto;
  // display: flex;
  align-items: center;
  padding:20px 30px;
}

.v-question-item__text{
  color:white;
  text-align: center;
  font-weight: normal;
  
}
.actions{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
      button{
        width: 200px;
        margin: 5% 10% 5% 10%;
        padding: 5px 20px;
        display:inline;
        justify-content: space-between;
      }
  }
.multiselect{
  width: 550px;
  margin:0 auto; 
}

.multiselect__input::placeholder {
    color : #555;
    
}
.multiselect__placeholder {
  color : red;
  border-radius: 0px;
}

.multiselect__content-wrapper {
  position: absolute;
  display: block;
  background: #ccc ;
  color:black;
  width: 550px;
  max-height: 240px;
  overflow: auto;
  border-top: none;
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
  z-index: 50;
  -webkit-overflow-scrolling: touch;
}
.multiselect__tag {
    position      : relative;
    display       : inline-block;
    border-radius : px;
    background    : black;
    white-space   : nowrap;
    overflow      : hidden;
    max-width     : 100%;
    text-overflow : ellipsis;
}
.multiselect__tag-icon:after {
    content   : "×";
    color     : red;
    font-size : 220%;
}
.multiselect__tag-icon:focus,
.multiselect__tag-icon:hover {
    background : none;

}
.multiselect__option--highlight {
    background : #555;
    color      : white;
}
.multiselect__option--highlight:after {
    content    : attr(data-select);
    background : black;
}




.set-range {
  
        flex: 0 0 auto;

        display: flex;

        padding: 20px;
        input {
          width: 300px;
          height: 40px;
          color: white;
          text-decoration: none;
          text-align: center;
          text-transform: capitalize;
          background-color: $bg;
          font: 700 20px tahoma;
          border: none;
          margin: 0 10px ;
          box-shadow: 0 4px 16px red; 
          &:hover, &:focus {
            border-color: red;
          }
        }
      }
.merge-tooltip {
      position: absolute;
      left: 50%;
      bottom: 100%;
      transform: translate(-50%, -15px);
    }
.custom-step {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    box-shadow: 0 0 0 3px #ccc;
    background-color: #fff;
  }
  .custom-step.active {
    box-shadow: 0 0 0 3px red;
    background-color: red;
  }
 .custom-dot {
    width: 100%;
    height: 100%;
    border-radius: 0;
    //background-color: rgb(49, 4, 194);
    transition: all .3s;
  }
  .custom-dot.focus {
    border-radius: 25%;
  }
.custom-step{
  color:red;
}
.vue-slider{
  padding:17px 20px;
}
.vue-slider-dot-tooltip-inner {
  border-color: red;
  background-color: red;
}
.vue-slider-marks{
  color:red;
}

.p-icon {
  color: white;
  align-items: center;
  columns: 60px 4;
  column-gap: 30px;
  margin: 0 auto;
  //left:5%;
}
.pretty.p-icon .state .icon{
  background-color: red;
  margin: 0 auto;
}

.message{
  margin: 0 auto;
  input,textarea{
  margin: 0 0 32px 0;
  width: 100%; 
  height: 50px;
  border-radius: 0px; 
  box-shadow: 0 4px 16px red; 
  border: none;  
  font-size: 35xp;
  color :#fff ; 
  background-color: $bg; 
  outline: none; 
  cursor: pointer; 

  }
}
.pretty{
  color:white;
}


.switch input {
  display: none;
  
}
.switch label {
  display:inline;
  justify-content: space-between;
  display: inline-block;
  cursor: pointer;
  color:white;
}

.ex1 span {
  display: block;
  padding: 5px 10px 5px 25px;
  border: 2px solid white; 
  border-radius: 5px;
  position: relative;
  transition: all 0.25s linear;
}
.ex1 span:before {
  content: '';
  position: absolute;
  left: 5px;
  top: 50%;
  -webkit-transform: translatey(-50%);
          transform: translatey(-50%);
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background-color: #ddd;
  transition: all 0.25s linear;
}
.ex1 input:checked + span {
  background-color: #fff;
  box-shadow: 0 0 5px 2px rgba(0, 0, 0, 0.1);
}
.ex1 .red input:checked + span {
  color: red;
  border-color: red;
}
.ex1 .red input:checked + span:before {
  background-color: red;
}
.labels{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
      label{
        margin: 5% 10% 5% 10%;
        padding: 5px 20px;
        display:inline;
        justify-content: space-between;
      }
}
.mx-datepicker-range {
    width: 550px;
}
.mx-calendar-content .cell.active {
    color: #fff;
    background-color: red;
}
.mx-calendar-content .cell.in-range {
    color: white;
    background-color:#555;
}
.mx-datepicker-main {
    color: black;
}
.mx-btn {
  color:black;
  background-color:transparent;
  // width:320px;
  background-image:none;
  display: initial;
  &:hover{
    color:red;
    border-color: red;
  }
}
.mx-table-date .today {
    color: red;
}

.mx-btn-text {
  border: 0;
  padding: 0 4px;
  text-align: left;
  line-height: inherit;
  &:hover{
    color:red;
  }
}
</style>