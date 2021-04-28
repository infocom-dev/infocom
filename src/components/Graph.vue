<template>
  <div>
    <apexchart width="500" :options="options" :series="series"> </apexchart>
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
  },
};
</script>


