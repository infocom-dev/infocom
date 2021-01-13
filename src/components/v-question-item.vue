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
      <div>value: {{ value[0]}} - {{value[1]}}</div>
      <vue-slider :min="0"
          :max="500"
          :interval="10"
           v-model="value"></vue-slider>


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
    }
    }
  }
</script>
<style lang="scss">
</style>