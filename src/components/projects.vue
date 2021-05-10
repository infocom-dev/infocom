<template>
  <div class="projects">
    <b-row align-h="center" class="w-100 m-0">
      <b-container class="w-100 d-flex align-items-stretch col-2 p-0">
        <side-bar-account></side-bar-account>
      </b-container>
      <b-container class="col p-0 ml-0">
        <b-container fluid class="p-0 ml-0">
          <b-row align-v="center" class="ml-0">
            <b-col>
              <b-row
                align-v="center"
                class="text-center justify-content-center ml-5"
              >
                <div class="col-4 p-0 text-left">
                  <i class="fa fa-folder-open user-icon"></i>
                </div>
                <div class="col text-left">
                  <h3>Projects</h3>
                </div>
              </b-row>
            </b-col>
            <b-col class="d-none d-sm-block"></b-col>
            <b-col>
              <b-row align-h="center" align-v="center" class="text-left mr-3">
                <div class="bellhold">
                  <i class="text-center fa fa-bell bell-icon"></i>
                  <span class="badgex badge-danger">6</span>
                </div>
                <router-link to="logout">
                  <div class="m-5">
                    <a
                      href="#"
                      class="btn text-uppercase w-100 mx-auto d-none d-lg-block"
                      >log out</a
                    >

                    <i
                      class="fas fa-sign-out-alt out-icon m-4 d-block d-lg-none"
                    ></i>
                  </div>
                </router-link>
              </b-row>
            </b-col>
          </b-row>
          

          <b-container fluid class="w-100 overview pb-5">
            <v-form></v-form>
            <b-row
              align-v="center"
              class="text-center justify-content-center m-5"
            >
              <div class="col-1 pl-2 text-left">
                <i class="fas fa-chart-area projects-icon"></i>
              </div>
              <div class="col-4 p-0 text-left">
                <h3>Projects in analysis</h3>
              </div>
              <div class="col"></div>
            </b-row>
            <div v-for="(item, id) in analysis_pr" :key="id">
              <b-row>
                <div class="w-100 ml-5 mr-5">
                  <b-row align-h="center d-flex align-items-stretch m-1 w-100">
                    <b-col class="col-lg-3 w-100 anketa-box">
                      <div
                        class="name-box text-center d-flex justify-content-center m-4 mx-auto"
                      >
                        <h5 class="m-3">{{ item.name }}</h5>
                      </div>
                      <div
                        v-if="item.status == 'in progress'"
                        class="text-center"
                      >
                        <p>
                          Наша нейронная сеть пытается обработать запрос.
                          Пожалуйста подождите
                        </p>
                      </div>
                      <div v-else class="text-center">
                        <h5>
                          Наша нейронная сеть оценала заказ в $
                          {{ item.old_budjet }}.
                        </h5>
                        <p>Вы можете изменить настройки в меня справа</p>
                        <div class="m-3" v-b-modal.modal-scrollable>
                          <a href="#" class="btn text-uppercase w-100 mx-auto"
                            >View details
                          </a>
                        </div>
                        <b-modal
                          id="modal-scrollable"
                          scrollable
                          centered
                          size="lg"
                          title="Details"
                        >
                          <p class="my-4" v-for="i in 20" :key="i">
                            Cras mattis consectetur purus sit amet fermentum.
                            Cras justo odio, dapibus ac facilisis in, egestas
                            eget quam. Morbi leo risus, porta ac consectetur ac,
                            vestibulum at eros.
                          </p>
                        </b-modal>
                      </div>
                    </b-col>
                    <b-col
                      class="anketa-box d-flex justify-content-center offset-sm-1"
                    >
                      <div v-if="item.status == 'in progress'" class="m-3">
                        <graph
                          class="mx-auto"
                          v-bind:options="options"
                          v-bind:series="series"
                          v-bind:width="500"
                          :key="componentKey"
                        ></graph>
                        <div @click="fillData()" ref="submitBtn"></div>
                      </div>
                      <div v-else class="w-100 m-3 justify-content-center">
                        <div v-for="(f, index) in feature" :key="index">
                          <b-row align-v="center" class="d-flex">
                            <b-col class="col-4">
                              <div
                                class="name-box d-flex justify-content-center text-center m-3 mx-auto"
                              >
                                <p class="m-1">{{ f }}</p>
                              </div>
                            </b-col>
                            <b-col class="col w-100">
                              <vue-slider
                                v-model="answers[index]"
                                :adsorb="true"
                                :interval="10"
                                :marks="true"
                              ></vue-slider>
                            </b-col>
                          </b-row>
                        </div>

                        <b-row>
                          <b-container fluid class="p-0 ml-0">
                            <b-row align-v="center" class="">
                              <b-col class="mx-auto">
                                <div
                                  class="m-3 d-flex"
                                  v-b-modal.modal-scrollable
                                >
                                  <a href="#" class="btn text-uppercase mx-auto"
                                    >Submit data
                                  </a>
                                </div>
                              </b-col>
                              <b-col v-if="item.new_budjet">
                                <h5>New budjet : {{ item.new_budjet }}</h5>
                              </b-col>
                            </b-row>
                          </b-container>
                        </b-row>
                      </div>
                    </b-col>
                  </b-row>
                </div>
              </b-row>
            </div>
            <b-row align-v="center" class="text-center m-5">
              <div class="col-1 pl-2 text-left">
                <i class="fas fa-tasks projects-icon"></i>
              </div>
              <div class="col-4 p-0 text-left">
                <h3>Current projects</h3>
              </div>
            </b-row>
            <div class="row ml-5 mr-5 justify-content-between">
              <div v-for="(pr, index) in projects" :key="index">
                <div class="col">
                  <b-row align-v="center d-flex align-items-stretch ">
                    <b-col class="p-0 mr-2 pr-box text-center" style="">
                      <h5 class="name-box p-3 m-4 mx-auto">{{ pr.name }}</h5>
                      <h5>{{ pr.info }}</h5>
                    </b-col>
                    <b-col class="pr p-0 ml-2 text-center">
                      <b-row class="mb-3">
                        <h5
                          class="name-box p-3 mx-auto"
                          style="background-color: #fff"
                        >
                          {{ pr.status }}
                        </h5>
                      </b-row>
                      <b-row class="mb-3">
                        <h5
                          class="name-box p-3 mx-auto"
                          style="background-color: #ffd334"
                        >
                          ${{ pr.budjet }}
                        </h5>
                      </b-row>
                      <b-row class="">
                        <h5
                          class="name-box p-3 mx-auto"
                          style="background-color: #274c77"
                        >
                          till {{ pr.data }}
                        </h5>
                      </b-row>
                    </b-col>
                  </b-row>
                  <b-row
                    align-v="center d-flex align-items-stretch mt-3"
                    class="justify-content-center"
                  >
                    <b-col class="p-0 pr-box text-center mr-2" style="">
                      <h5 class="name-box p-3 m-4 mx-auto">Project manager</h5>
                      <h3>{{ pr.manager }}</h3>
                      <h5>
                        Contacts: <i class="fas fa-envelope-open icon"></i>
                      </h5>
                      <h5>Github:<i class="fab fa-github icon"></i></h5>
                    </b-col>
                    <b-col class="p-0 pr-box text-center ml-2" style="">
                      <h5 class="pt-3 mx-auto">Team</h5>
                      <div class="text-left m-3">
                        <h5 class="pb-2">
                          <i class="fas fa-thumbs-up icon mr-3"></i>Качество:
                          {{ pr.t_qualty }}/10
                        </h5>
                        <h5 class="pb-2">
                          <i class="fas fa-hourglass-half icon mr-3"></i>Время:
                          {{ pr.t_time }}
                        </h5>
                        <h5>
                          <i class="fas fa-smile icon mr-3"></i>Надежность:
                          {{ pr.reliability }}/10
                        </h5>
                      </div>
                    </b-col>
                  </b-row>
                </div>
              </div>
            </div>
          </b-container>
        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
import sideBarAccount from "./side-bar-account.vue";
import VueSlider from 'vue-slider-component'
import "vue-slider-component/theme/default.css";
import "vue-slider-component/theme/default.css";
import Graph from "./Graph.vue";
import VForm from './v-form.vue';
export default {
  components: { sideBarAccount, Graph,VueSlider,  VForm },
  name: "projects",

  data() {
    return {
      componentKey: 0,
      feature: ["Дешево", "Качественно", "Быстро"],
      answers: [50, 10, 20],

      analysis_pr: [
        {
          name: "Infocom",
          status: "in pro",
          old_budjet: "1 000 000",
          new_budjet: "1 500 000",
        },
      ],
      projects: [
        {
          name: "MyProject",
          info: "Web site on vuejs + django",
          budjet: "1 000 000",
          status: "in progress",
          data: "15.05.2022",
          manager: "Vistor Keng",
          contacts: [{ mail: "fhhfhf", github: "ddjd" }],
          t_qualty: 8,
          t_time: "7 years",
          reliability: 10,
        },
        {
          name: "MyWebsite",
          info: "Web site on vuejs + django",
          budjet: "1 000 000",
          status: "in progress",
          data: "15.05.2022",
          manager: "Vistor Keng",
          contacts: [{ mail: "fhhfhf", github: "ddjd" }],
          t_qualty: 8,
          t_time: "7 years",
          reliability: 10,
        },
      ],

      options: {
        chart: {
          type: "area",
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
        },
        xaxis: {
          categories: [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
          ],
        },
        title: {
          align: "center",
          style: {
            fontSize: "20px",
          },
        },
        colors: ["#274C77", "#FFD334"],
      },

      series: [
        {
          name: "series1",
          data: [31, 40, 28, 51, 42, 109, 100],
        },
        {
          name: "series2",
          data: [11, 32, 45, 32, 34, 52, 41],
        },
      ],
    };
  },
  mounted() {
    this.$refs.submitBtn[0].click();
  },
  methods: {
    forceRerender() {
      this.componentKey += 1;
    },
    getRandomInt() {
      return Math.floor(Math.random() * 100) + 5;
    },
    fillData() {
      for (let i = 0; i < this.series.length; i++) {
        for (let j = 0; j < this.series[i].data.length; j++) {
          this.series[i].data[j] = this.getRandomInt();
        }
      }
      this.forceRerender();
      console.log(this.series);
      console.log(this.series[1].data);
      setTimeout(() => {
        console.log(this);
        this.$refs.submitBtn[0].click();
      }, 3000);
    },
  },
};
</script>
<style lang="scss">
.anketa-box {
  background-color: white;
  border-radius: 40px;
}
.name-box {
  background-color: #e7ecef;
  border-radius: 40px;
  display: inline-block;
}
.pr {
  .name-box {
    width: 255px;
  }
}
.pr-box {
  background-color: white;
  border-radius: 40px;
  height: 225px;
  width: 225px;
  .icon {
    font-size: 20px;
  }
}
</style>