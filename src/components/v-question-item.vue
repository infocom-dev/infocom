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
      <div v-if="question_data.type === 'range' " >
         <!-- <div class="range-slider">
        <input
            type="range"
            min="0"
            max="1000"
            step="10"
            v-model.number="minPrice"
            @change="setRangeSlider"
        >
        <input
            type="range"
            min="0"
            max="1000"
            step="10"
            v-model.number="maxPrice"
            @change="setRangeSlider"
        >
      </div>
      <div class="range-values">
        <p>Min: {{minPrice}}</p>
        <p>Max: {{maxPrice}}</p>
      </div> -->
      <h1>Example vue-double-range</h1>

    <div>
      <label>From:
        <input type="number"
               v-model="slider.from"
               :min="initData.slider.min" :max="slider.to"
               :step="initData.slider.step"
               @keydown="onKeyDownInputSlider"/>
      </label>
      <label>To:
        <input type="number"
               v-model="slider.to"
               :min="slider.from" :max="initData.slider.max"
               :step="initData.slider.step"
               @keydown="onKeyDownInputSlider"/>
      </label>
    </div>

    <vue-double-range
      :min="initData.slider.min"
      :max="initData.slider.max"
      :step="initData.slider.step"
      v-model="slider"
      @input="onSliderChange" @update="onSliderUpdate"></vue-double-range>

    <div class="info">
      On move data:
      <pre class="info-code">{{dynamicSlider}}</pre>
      On the end of move data:
      <pre class="info-code">{{slider}}</pre>
    </div>
      </div>
    </div>
</template>

<script>
import RadioSet from "./v-radio-set.vue";
import VueDoubleRange from './VueDoubleRange.vue';
const AVAILABLE_KEY_CODES = [9, 35, 36, 37, 38, 39, 40];
const DEFAULT_SLIDER_DATA = {
  from: 15000,
  to: 500000
};
export default {
  name: 'v-question-item',
  components: {
    RadioSet,VueDoubleRange
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
      selectedAnswers:"",
      minPrice: null,
      maxPrice:null,
      initData: {
        slider: {
          min: 1000,
          max: 1000000,
          step: 1000
        }
      },
      slider: DEFAULT_SLIDER_DATA,
      dynamicSlider: DEFAULT_SLIDER_DATA
    }
    },
    methods: {
    onKeyDownInputSlider (event = window.event) {
      const keyCode = (event.which) ? event.which : event.keyCode;
      if (AVAILABLE_KEY_CODES.indexOf(keyCode) >= 0) return true;
      event.preventDefault();
      return false;
    },
    onSliderChange (event) {
      console.log('onSliderChange:event', event);
    },
    onSliderUpdate (event) {
      this.dynamicSlider = event;
    }
  }
  }
</script>
<style lang="scss">
</style>