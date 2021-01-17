<template>
    <div class= 'v-question-item'>
      <div v-if="question_data.type === 'selected' ">
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
          <div>
           <multiselect v-model="selectedAnswers" tag-placeholder="Add this as new tag" placeholder="Search" label="value" track-by="id" :options="question_data.answers" :multiple="true" :taggable="true" @tag="addTag"></multiselect>
      </div>
      </div>
      <div v-if="question_data.type === 'checkbox' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <radio-set label-name="checkbox" v-model="selectedAnswers" :options="question_data.answers"></radio-set>
        <span>Answer: {{ selectedAnswers }}</span>
      </div>
      <div v-if="question_data.type === 'message' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <input v-model="selectedAnswers" placeholder="write you useless opinion ">
        <p>Answer: {{ selectedAnswers }}</p>
      </div>
      <div v-if="question_data.type === 'range' ">
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
      <!-- <vue-range-slider ref="slider" v-model="value"></vue-range-slider> -->
      <vue-slider :min="question_data.answers[0]"
          :max="question_data.answers[1]"
          :interval="10"
          v-model="value"
          :marks="marks"
          :tooltip="'none'"
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
      <label></label>
    <input type="text" v-model="value[0]" placeholder="От" class="form-control" /><br>
    <label></label>
    <input type="text" v-model="value[1]"  placeholder="До" class="form-control" /><br>
    
      </div>
      </div>
      <div v-if="question_data.type === 'fill-checkbox' " >
        <p-check class="p-icon p-round p-smooth" color="success">
        <i slot="extra" class="icon mdi mdi-check"></i>
        Tuesday
    </p-check>
      </div>
      
   
      
    </div>
</template>

<script>
import RadioSet from "./v-radio-set.vue";
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import Multiselect from 'vue-multiselect'

export default {
  name: 'v-question-item',
  components: {
    RadioSet,
    VueSlider,
    Multiselect
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
      marks: val => val % 20 === 0,
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

.set-range {
        flex: 0 0 auto;

        display: flex;

        padding: 20px;

        input {
          width: 100%;
          padding: (20px / 2) 20px;
          border: 2px solid rgb(100, 100, 100);
          border-radius: 100px;
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