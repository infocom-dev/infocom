<template>
  <div>
    <apexchart :width="width" :options="options" :series="series"> </apexchart>
  </div>
</template>
<script>
export default {
  name: "Graph",
  data: () => ({}),
  props: {
    options: {
      type: Object,
      default() {
        return {};
      },
    },
    series: [],
    width: Number,
    
  },
};
</script>


