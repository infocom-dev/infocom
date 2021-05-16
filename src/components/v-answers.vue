<template>
  <div class="v-answers">
    <div>
      <b-table sticky-header bordered table-variant="info" hover  responsive :items="items"></b-table>
    </div>
  </div>
</template>
<script>
export default {
  name: "v-answers",
  props: {
    answers: {
      type: Array,
      default() {
        return {};
      },
    },
    questions: {
      type: Array,
      default() {
        return {};
      },
    },
  },
  computed: {
    items() {
      let v = [];
      for (let i = 0; i < this.answers.length; i++) {
        if (
          this.answers[i].type == "range" ||
          this.answers[i].type == "datapicker"
        ) {
          let s =
            this.answers[i].answers[0] + " - " + this.answers[i].answers[1];
          v[i] = { Question: this.questions[i].text, Answers: s };
        } else if (
          this.answers[i].type == "checkbox" ||
          this.answers[i].type == "selected"
        ) {
          v[i] = {
            Question: this.questions[i].text,
            Answers: this.answers[i].answers[0].value,
          };
        } else {
          v[i] = {
            Question: this.questions[i].text,
            Answers: this.answers[i].answers[0],
          };
        }
      }
      return v;
    },
  },
};
</script>
<style scoped>
</style>