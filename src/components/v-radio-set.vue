<template id="radio-set">
  <div>
    <label v-for="val in options" :key="val.id">
      <input type="checkbox" 
        :name="typeSet" 
        :value="val.value" 
        :checked="val.value == value"
        @change="$emit('input', val.value)"> 
      {{ val.value }}
    </label>
  </div>
</template>

<script>
export default {
  props: ["value", "options", "typeSet"],
  methods: {
    clicked(val) {
      this.$emit("input", val);
    }
  }
};
</script>
