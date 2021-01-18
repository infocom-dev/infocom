<template>

    <div class= 'v-question-item'>
      <div clsass="selected" v-if="question_data.type === 'selected' ">
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
          <div>
           <multiselect v-model="selectedAnswers" tag-placeholder="Add this as new tag" placeholder="Search" label="value" track-by="id" :options="question_data.answers" :multiple="true" :taggable="true" @tag="addTag"></multiselect>
          </div>
      </div>

      <div v-if="question_data.type === 'checkbox' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <label v-for="val in question_data.answers" :key="val.id">
          <p-check class="p-icon p-round p-pulse" color="success">
             <i slot="extra" class="icon mdi mdi-check"></i>
               {{val.value}}
          </p-check>
        </label>
       </div>

      <div v-if="question_data.type === 'message' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <input v-model="selectedAnswers" placeholder="Type here">
        <p>Answer: {{ selectedAnswers }}</p>
      </div>

      <div v-if="question_data.type === 'range' ">
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <vue-slider :min="question_data.answers[0]"
                    :max="question_data.answers[1]"
                    :interval="10"
                    v-model="value"
                    :marks="marks"
                    :tooltip="'none'"
                    :process="process"
                    :process-style="{ backgroundColor: 'blue' }"
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
        <div class="set-range">
         <input type="text" v-model="value[0]" placeholder="От" class="form-control" /><br>
         <input type="text" v-model="value[1]" placeholder="До" class="form-control" /><br>
        </div>
      </div>
      <div v-if="question_data.type === 'switch' " >
          <p-check class="p-switch" color="primary">{{question_data.text}}</p-check>
      </div>
      <div v-if="question_data.type === 'datapicker' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <date-picker  v-model="selectedAnswers"
                      value-type="format"
                      format="DD.MM.YYYY"
                      range
                      placeholder="tip range"
                      confirm
                      range-separator=" - "
                      >
        </date-picker>
>
      </div>
   
      
    </div>
</template>

<script>

import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import Multiselect from 'vue-multiselect'
import DatePicker from 'vue2-datepicker';
import 'vue2-datepicker/index.css';



export default {
  name: 'v-question-item',
  components: {
    VueSlider,
    Multiselect,
    DatePicker
  },
  props:{
        question_data:{
            type:Object,
            default(){
                return{}
            }
        }
    },
  data(){ 
    return {
      value:[0,50],
      marks: val =>  val % ((this.question_data.answers[1]-this.question_data.answers[0]) /10) === 0,
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
    }
  }
} 
    
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss">
.v-question-item{
  position: relative;
  padding: 10px;
  background: #bfe6f8; 
  text-align: left;
  color:rgb(1, 1, 112)
}

.multiselect__tags{
  min-height: 32px;
  display: block;
  padding: 3px 40px 0 8px;
  border-radius: 10px;
  border: 1px solid #0329ff;
  background: rgb(255, 255, 255);
  font-size: 14px;
}
// .multiselect__wrapper-dropdown{
//   position: relative;
//  width: 200px;
//  padding: 10px;
//  margin: 0 auto;

//  /*Общие стили */
//  background: #9bc7de;
//  color: #fff;
//  outline: none;
//  cursor: pointer;

//  /* Настройки шрифтов */
//  font-weight: bold;
// }
.wrapper-dropdown-1 .dropdown {
 /* размер и позиция */
 position: absolute;
 top: 100%;
 left: 0; /* Size */
 right: 0; /* Size */

 /* Стили */
 background: #fff;
 font-weight: normal;

 opacity: 0;
 pointer-events: none;
}
.set-range {
        flex: 0 0 auto;

        display: flex;

        padding: 20px;

        input {
          width: 100%;
          padding: (20px / 2) 20px;
          border: 2px solid rgb(100, 100, 100);
          border-radius: 5px;
          transition: border-color .2s ease-out;

          &:hover, &:focus {
            border-color: rgb(30, 30, 30);
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
    box-shadow: 0 0 0 3px #3498db;
    background-color: #3498db;
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
</style>