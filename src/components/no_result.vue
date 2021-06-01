<template>
  <b-row align-v="center m-3">
    
    <b-col class="text-center">
      <p>It seems that you don't have projects</p>
      <h3>Start filling the form in the upper block</h3>
    </b-col><b-col>
      <b-img
        style="max-width: 200px"
        fluid
        center
        class=""
        :src="require('../assets/images/no_result.gif')"
      />
    </b-col>
  </b-row>
</template>
<script>
export default {
    name:"no-result"
}
</script>