<template>
  <div id="app">
    <p>KILao</p>
  <v-question/>
  <!-- <label id="fruitLabel">Choose a fruit: </label>
    <combobox :items="[ 'Apple', 'Banana', 'Orange', 'Mango', 'Pear', 'Peach', 'Grape', 'Tangerine', 'Pineapple']" aria-labelled-by="fruitLabel" />

    <br>
    <hr>
    <br> -->


  </div>
</template>

<script>
import vQuestion from './components/v-question.vue'
// import combobox from './components/combobox.vue'
export default {
  name: 'App',
  components: {
    vQuestion
    // combobox
  },
  data(){
    return {
    }
  },
  methods:{
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>