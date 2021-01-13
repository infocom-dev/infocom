<template>
    <div class= 'v-question-item'>
      <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
      <div v-if="question_data.type === 'selected' ">
          <select v-model="selectedAnswers">
            <option v-for="answer in question_data.answers" 
                    v-bind:key="answer.id"
                    v-bind:value="answer.value"
                    >{{answer.value}}</option>
          </select>
          <span>Answer: {{selectedAnswers}}</span>
      </div>
      <div v-if="question_data.type === 'checkbox' " >
        <radio-set label-name="checkbox" v-model="selectedAnswers" :options="question_data.answers"></radio-set>
        <span>Answer: {{ selectedAnswers }}</span>
      </div>
      <div v-if="question_data.type === 'message' " >
        <input v-model="selectedAnswers" placeholder="write you useless opinion ">
        <p>Answer: {{ selectedAnswers }}</p>
      </div>
      <div v-if="question_data.type === 'range' ">
      <vue-range-slider ref="slider" v-model="value"></vue-range-slider>
      <div>Посетители: {{ value[0]}} - {{value[1]}}</div>
      <vue-slider :min="question_data.answers[0]"
          :max="question_data.answers[1]"
          :interval="10"
          v-model="value"
          :marks="marks"
          :process-style="{ backgroundColor: 'pink' }"
      :tooltip-style="{ backgroundColor: 'pink', borderColor: 'pink' }"
    >
      <div :class="['custom-dot', { focus }]"></div>
      <template v-slot:step="{ label, active }">
        <div :class="['custom-step', { active }]"></div>
      </template>
      </vue-slider>


      </div>
    </div>
</template>

<script>
import RadioSet from "./v-radio-set.vue";
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'

export default {
  name: 'v-question-item',
  components: {
    RadioSet,
    VueSlider

  },
  props:{
        question_data:{
            type:Object,
            default(){
                return{}
            }
        }
    },
  data(){ return {
      value:[0,50],
      marks: val => val % 20 === 0,
      selectedAnswers:""
  }
} 
    
}
</script>
<style lang="scss">
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
.custom-tooltip {
    transform: translateY(5px);
  }
  .custom-tooltip.focus {
    font-weight: bold;
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