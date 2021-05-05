<template>
  <div class="statistic">
    <b-container fluid class="w-100 justify-content-center">
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          about company
        </h1>
      </div>
      <b-row align-v="center" class="justify-content-center mx-auto">
        <div v-for="(item, index) in statistic" :key="index">
          <div
            class="col m-5 h-100 text-center box"
            style="width: 350px"
            :style="{ 'background-color': statistic_colors[index] }"
          >
            <b-row align-v="center" class="justify-content-center">
              <i :class="statistic_icons[index]" class="m-1"></i>
              <h1 class="mt-2">
                <animated-number
                  v-bind:max="item.max"
                  v-bind:top="top"
               
                ></animated-number>
              </h1>
            </b-row>
            <b-row align-v="center" class="justify-content-center text-center">
              <h4 class="">{{ item.name }}</h4>
            </b-row>
          </div>
        </div>
      </b-row>
    </b-container>
  </div>
</template>
<script>
import animatedNumber from "./animated-number.vue";
export default {
  components: {
    animatedNumber,
  },

  data() {
    return {
      top:0,
      
      statistic: [
        { name: "Выполненных заказов", max: 500 },
        { name: "Заказов в разработке", max: 200 },
        { name: "Сотрудников в компании", max: 3 },
      ],
      statistic_icons: [
        "fas fa-check-circle icon",
        "fas fa-clock icon",
        "fas fa-user-circle icon",
      ],
      statistic_colors: ["#A3CEF1", "#FFD349", "#A3CEF1"],
    };
  },
  // updated: function () {
  //   this.top = this.$el.offsetTop - this.$el.offsetHeight;
  // },
  methods: {
    onScroll() {
      this.top = this.$el.offsetTop - this.$el.offsetHeight;
    
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
    this.onScroll();
  },
};
</script>
<style lang="scss">
.statistic {
  .box {
    border-radius: 20% 15% 10% 15% / 0% 40% 0% 40%;
  }
}
</style>