<template>
  <div class="v-statistic p-0">
    <b-container fluid class="w-100 justify-content-center p-0">
      <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          about company
        </h1>
      </div>
      <b-container fluid class="w-100  justify-content-center">
        <b-row
          align-v="center"
          class="w-100 justify-content-center mx-auto"
        >
          <!-- <hr> -->
          <div v-for="(item, index) in statistic" :key="index">
            <div
              class="col m-5 h-100 text-center box2"
              style="width: 280px"
              :style="{ 'background-color': statistic_colors[index] }"
            >
              <b-row align-h="center" class="m-1 justify-content-center">
                <i :class="statistic_icons[index]" class="m-1"></i>
                <h1 >
                  <animated-number
                    v-bind:max="item.max"
                    v-bind:top="top"
                  ></animated-number>
                </h1>
                <h4 class="">{{ item.name }}</h4>
              </b-row>
            </div>
          </div>
        </b-row>
      </b-container>
      <!-- <div class="mx-auto pt-3">
        <h1 class="text-center text-uppercase font-weight-bolder">
          most popular projects
        </h1>
      </div> -->
      <!-- <b-container fluid class="w-100 p-0 justify-content-center">
        <div class="m-5">
          <b-row align-v="center" class="m-5">
            <b-col class="col-3 p-0 text-center">
              <button
                v-for="(item, index) in popular"
                :key="index"
                class="box2 mb-5"
                style="width: 270px"
                @click="updateGraph(index, item.data)"
              >
                <b-row class="text-center justify-content-center p-1">
                  <h4>{{ item.stack }}</h4>
                </b-row>
                <b-row>
                  <b-col class="col text-center">
                    <b-row align-h="center">
                      <b-col class="col-2 text-center">
                        <i class="fas fa-dollar-sign icon"></i>
                      </b-col>
                      <b-col class="col-3">
                        <h1 class="m-0 p-0">{{ item.orders }}</h1>
                        <p>orders</p>
                      </b-col>
                    </b-row>
                  </b-col>
                </b-row>
              </button>
            </b-col>
            <b-col class="mr-5">
              <graph
                class=""
                v-bind:options="options"
                v-bind:series="series"
                :key="ind"
              ></graph>
            </b-col>
          </b-row>
        </div>
      </b-container> -->
    </b-container>
  </div>
</template>
<script>
import axios from "axios";
import animatedNumber from "./animated-number.vue";
export default {
  components: {
    animatedNumber,
  },

  data() {
    return {
      
      top: 0,
      s: "",
      ind: 0,
      popular: [
        {
          stack: "Vue + Django",
          orders: 400,
          data: [31, 40, 28, 51, 42, 109, 100],
        },
        {
          stack: "React.js + Django",
          orders: 200,
          data: [31, 50, 28, 40, 2, 1, 3],
        },
        {
          stack: "Django",
          orders: 500,
          data: [31, 30, 10, 51, 60, 5, 15],
        },
      ],

      statistic: [
        // { name: "Выполненных заказов", max: 500 },
        // { name: "Заказов в разработке", max: 200 },
        // { name: "Developers in the company", max: 0 },
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
    updateGraph(index, data) {
      console.log(index);
      this.ind = index;
      this.series[0].data = data;
    },
  },
  mounted() {
    window.addEventListener("scroll", this.onScroll);
    this.onScroll();
  },

  created() {
    let req = [{text : "Developers in the company", r:"/getDevelopers/"},
           {r:"/getCustomers/",text:"Users on our site"},
           {r:'/getProjects/',text:"Completed orders"}]
    for(let i = 0;i < req.length;i++){
      axios.get(req[i].r)
      .then((response) => {
        this.statistic.push({"name": req[i].text ,"max": response.data.length});
        console.log(this.statistic);
      })
      .catch((err) => {
        console.log(err);
      });
    }
    // axios.get("/getDevelopers/")
    //   .then((response) => {
    //     this.statistic[2].max = response.data.length;
    //     console.log(this.statistic.max[2]);
    //   })
    //   .catch((err) => {
    //     console.log(err);
    //   });

      
  }
};
</script>
<style lang="scss">
.v-statistic {
  .box2 {
    overflow: hidden;
    position: relative;
    margin: 0.25em auto;
    // max-width: 15em;
    // min-height: 10em;
    border-radius: 1em;

    &:before {
      // position: absolute;
      margin: 7em;
      padding: 7em;

      border-radius: 50%;
      box-shadow: 0 0 0 350px rgba(rgb(0, 51, 255), 0.65);
      content: "";
    }
    // border-radius: 0% 0% 20% 20% / 10% 10% 20% 20%
  }
  button {
    //  background-image: url("../assets/images/box.png");
    background-color: #a3cef1;
    .icon {
      color: #ffd037;
    }
    h1 {
      color: white;
    }
  }
}
</style>