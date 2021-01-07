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
      <div v-if="question_data.type === 'radio' " >
        <radio-set label-name="radio" v-model="selectedAnswers" :options="question_data.answers"></radio-set>
        <span>Answer: {{ selectedAnswers }}</span>
      </div>
      <div v-if="question_data.type === 'message' " >
        <input v-model="selectedAnswers" placeholder="write you useless opinion ">
        <p>Answer: {{ selectedAnswers }}</p>
      </div>

    </div>
</template>

<script>
import RadioSet from "./v-radio-set.vue";
export default {
  name: 'v-question-item',
  components: {
    RadioSet
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
      selectedAnswers:""
    }
    },
    computed:{},
  }
</script>
<style lang="scss">
</style>