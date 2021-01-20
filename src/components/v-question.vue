<template>
    <div class = "v-question">
      <v-question-item
        v-for="question in questions"
        :key="question.id"
         v-bind:question_data="question"
         v-model="checkedValue">
      </v-question-item>
    

    </div>
</template>

<script>
import vQuestionItem from './v-question-item'
import axios from 'axios'

export default {
  name: 'v-question',
  props: {},
  components:{
    vQuestionItem
  },
  data(){
    return {
      questions:[]
    }
  },
  mounted () {
    axios
    .get('/hello/')
    .then(response => {
      this.questions = response.data;
    })
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
