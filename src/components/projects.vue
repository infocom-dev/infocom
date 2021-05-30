<template>
  <div class="projects">
    <b-row align-h="center" class="w-100 m-0">
      <b-container class="w-100 d-flex align-items-stretch col-2 p-0">
        <side-bar-account></side-bar-account>
      </b-container>

      <b-container class="col p-0 ml-0">
        <b-container fluid class="p-0 ml-0">
          <b-row align-v="center" class="mr-0 p-0">
            <b-col>
              <b-row
                align-v="center"
                class="text-center justify-content-center m-4"
              >
                <b-col class="col">
                  <i class="fa fa-user-circle user-icon"></i>
                </b-col>
                <b-col class="col-9 text-left d-none d-lg-block">
                  <h5>Hello, {{ user_username }}!</h5>
                  <b-row align-v="center" class="ml-0">
                    <i class="text-center m-1 fa fa-envelope mail-icon"></i>
                    <p class="m-1">{{ user_mail }}</p>
                  </b-row>
                </b-col>
              </b-row>
            </b-col>

            <b-col class="p-0">
              <b-row align-h="center" align-v="center" class="text-left mr-3">
                <div class="bellhold">
                  <i class="text-center fa fa-bell bell-icon"></i>
                  <span class="badgex badge-danger">6</span>
                </div>
                <router-link to="/logout">
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
          <p>{{ projects }}</p>
          <b-container fluid class="w-100 overview p-0 pb-5">
            <b-row align-v="center" class="text-center ml-5">
              <div class="col-1 mt-5 text-left">
                <i class="fas fa-search icon"></i>
              </div>
              <div class="col mt-5 p-0 text-left">
                <h3>Guide to start new project</h3>
              </div>
            </b-row>
            <v-form :questions="questions"></v-form>
            <b-row
              align-v="center"
              class="text-center justify-content-center mr-5 ml-5 mb-5"
            >
              <div class="col-1 pl-2 text-left">
                <i class="fas fa-chart-area icon"></i>
              </div>
              <div class="col-4 p-0 text-left">
                <h3>Last project in analysis</h3>
              </div>
              <div class="col"></div>
            </b-row>
            <b-row class="p-0 m-0">
              <div class="w-100 p-0">
                <b-row class="pr-5 pl-5 m-0">
                  <b-col class="col-lg-3 w-100 anketa-box">
                    <div
                      class="name-box text-center d-flex justify-content-center m-4 mx-auto"
                    >
                      <h5 class="m-3">
                        {{ projects[projects.length - 1].name }}
                      </h5>
                    </div>
                    <div
                      v-if="
                        projects[projects.length - 1].predicted_price == null
                      "
                      class="text-center"
                    >
                      <p>
                        Наша нейронная сеть пытается обработать запрос.
                        Пожалуйста, обновите страницу
                      </p>
                    </div>
                    <div v-else class="text-center">
                      <h5>
                        Наша нейронная сеть оценала заказ в $
                        {{ projects[projects.length - 1].predicted_price }}.
                      </h5>
                    </div>
                  </b-col>
                  <b-col
                    class="anketa-box d-flex justify-content-center offset-sm-1"
                  >
                    <div
                      v-if="
                        projects[projects.length - 1].predicted_price == null
                      "
                      class="m-3 justify-content-center d-flex align-item-center"
                    >
                      <graph class=""></graph>
                    </div>
                    <div v-else class="w-100 m-3 justify-content-center"></div>
                  </b-col>
                </b-row>
              </div>
            </b-row>
            <b-row align-v="center" class="text-center m-5">
              <div class="col-1 pl-2 text-left">
                <i class="fas fa-tasks projects-icon"></i>
              </div>
              <div class="col p-0 text-left">
                <h3>ALL PROJECTS FINISHED ANALYSIS</h3>
              </div>
            </b-row>
            <div
              v-for="(item, index) in projects"
              :key="index"
              class="w-100 p-0"
            >
              <div v-if="item.predicted_price != null" class="box2 ml-5 mr-5">
                <b-row align-v="center" class="p-3 m-0">
                  <b-col class="col-4 p-2 mr-5" style="">
                    <h5 class="name-box w-100 text-center p-2 mx-auto">
                      {{ item.name }}
                    </h5>
                    <p class="m-0 pt-4">Status</p>
                    <div v-if="item.is_active">
                      <h1>In develop</h1>
                    </div>
                    <div
                      v-else-if="!item.is_active && item.real_end_date != null"
                    >
                      <h1>Finnished</h1>
                    </div>
                    <div v-else>
                      <h1>From analysis</h1>
                    </div>
                  </b-col>
                  <b-col class="col-2 p-0 mr-5" style="">
                    <p class="m-0">
                      <small>Predicted price</small>
                    </p>
                    <h1>$ {{ item.predicted_price }}</h1>
                    <p class="m-0">Real price</p>
                    <div v-if="!item.is_active && item.real_end_date != null">
                      
                      <h1>$ {{ item.real_price }}</h1>
                    </div>
                    <div v-else>
                      <h1>Soon</h1>
                    </div>
                  </b-col>
                  <b-col class="p-0 mr-5" style="">
                    <p class="m-0">
                      <small>Predicted date</small>
                    </p>
                    <h1>{{ item.predict_end_date }}</h1>
                    <p class="m-0">Real date</p>
                    <div v-if="!item.is_active && item.real_end_date != null">
                      
                      <h1>{{ item.real_end_date }}</h1>
                    </div>
                    <div v-else>
                      <h1>Soon</h1>
                    </div>
                  </b-col>
                </b-row>
              </div>

              <!-- <b-col
                  style="
                    display: flex;
                    flex-direction: column;
                    justify-content: space-between;
                    background-color: transparent;
                  "
                  class="p-0 mr-5 text-center"
                >
                  <b-button
                    style="background-color: #ccc"
                    class="mx-auto w-100"
                    v-b-modal.modal3
                  >
                    View details
                  </b-button>
                  <b-modal
                    id="modal3"
                    size="lg"
                    scrollable
                    ok-only
                    title="Your answers"
                    header-bg-variant="primary"
                  >
                    <v-answers
                      :answers="item.answers"
                      :questions="questions"
                    ></v-answers>
                  </b-modal>
                 
                  <b-button class="mx-auto w-100">Make order</b-button>
                </b-col> -->
            </div>
          </b-container>
        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
import sideBarAccount from "./side-bar-account.vue";

import Graph from "./Graph.vue";
import VForm from "./v-form.vue";
// import vAnswers from "./v-answers.vue";
import session from "../api/session";
import axios from "axios";
export default {
  components: {
    sideBarAccount,
    Graph,
    VForm,
    //  vAnswers
  },
  name: "projects",

  data() {
    return {
      componentKey: 0,
      user_mail: "",
      user_id: "",
      user_username: "",
      feature: ["Дешево", "Качественно", "Быстро"],
      answers: [50, 10, 20],
      questions: [],
      // analysis_pr: [
      //   {
      //     name: "Infocom",
      //     info: "Web site on vuejs + django",
      //     status: "in progress",
      //     old_budjet: "1 000 000",
      //     new_budjet: "1 500 000",
      //     answers: [
      //       {
      //         id: "1",
      //         type: "selected",
      //         answers: [{ id: 1, value: "обработка типовых сообщений " }],
      //       },
      //       { id: "2", type: "checkbox", answers: [{ id: 1, value: "сайт" }] },
      //       { id: "3", type: "range", answers: [100, 250] },
      //       { id: "4", type: "message", answers: ["52"] },
      //       {
      //         id: "5",
      //         type: "checkbox",
      //         answers: [{ id: 1, value: "Свободное общение" }],
      //       },
      //       {
      //         id: "6",
      //         type: "selected",
      //         answers: [{ id: 2, value: "Russian" }],
      //       },
      //       { id: "7", type: "switch", answers: [true] },
      //       { id: "8", type: "switch", answers: [false] },
      //       { id: "9", type: "switch", answers: [false] },
      //       { id: "10", type: "switch", answers: [false] },
      //       { id: "11", type: "checkbox", answers: [{ id: 1, value: "Да" }] },
      //       { id: "12", type: "checkbox", answers: [{ id: 1, value: "Да" }] },
      //       {
      //         id: "13",
      //         type: "selected",
      //         answers: [
      //           {
      //             id: 2,
      //             value:
      //               "азмещение интеграционного модуля на серверах Заказчика",
      //           },
      //         ],
      //       },
      //       {
      //         id: "14",
      //         type: "datapicker",
      //         answers: ["04.05.2021", "20.05.2021"],
      //       },
      //       { id: "15", type: "range", answers: [600000, 1000000] },
      //       { id: "16", type: "textarea", answers: ["ghjklhy"] },
      //     ],
      //   },
      // ],
      // projects: [
      //   {
      //     name: "MyProject",
      //     info: "Web site on vuejs + django",
      //     budjet: "1 000 000",
      //     status: "in progress",
      //     data: "15.05.2022",
      //     manager: "Vistor Keng",
      //     contacts: [{ mail: "fhhfhf", github: "ddjd" }],
      //     t_qualty: 8,
      //     t_time: "7 years",
      //     reliability: 10,
      //   },
      //   {
      //     name: "MyWebsite",
      //     info: "Web site on vuejs + django",
      //     budjet: "1 000 000",
      //     status: "in progress",
      //     data: "15.05.2022",
      //     manager: "Vistor Keng",
      //     contacts: [{ mail: "fhhfhf", github: "ddjd" }],
      //     t_qualty: 8,
      //     t_time: "7 years",
      //     reliability: 10,
      //   },
      // ],
      projects: [],

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
  created() {
    session
      .get("/getQuestions/")
      .then((response) => {
        this.questions = response.data;
        console.log(this.questions);
      })
      .catch((err) => {
        console.log(err);
      });
    const token = localStorage.getItem("TOKEN_STORAGE_KEY");
    // console.log(token)
    axios
      .get("/auth/user/", { headers: { Authorization: `Token ${token}` } })
      .then((response) => {
        this.user_mail = response.data["email"];
        this.user_id = response.data["id"];
        this.user_username = response.data["username"];
        axios.get(`/getCustomerById/${this.user_id}`).then((response) => {
          this.projects = response.data.projects;
        });
        console.log(this.user_mail);
      })
      .catch((err) => {
        console.log(err);
      });
    // axios
    // .get(`/getCustomerById/${this.user_id}`)
    // .then((response) => {
    //   this.projects = response.data
    //   console.log(this.user_mail)
    // })
    // .catch((err) => {
    //   console.log(err);
    // });
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
@import "../assets/styles/base.scss";
.projects {
  .pr-icon {
    font-size: 50px;
    color: $blu;
  }
  .icon {
    font-size: 30px;
    color: $blu;
    &:hover {
      color: $ylw;
    }
  }
}
.anketa-box {
  background-color: white;
  border-radius: 20px;
}
.name-box {
  background-color: #e7ecef;
  border-radius: 20px;
  display: inline-block;
}
.box2 {
  background-color: white;
  margin: 0em auto;
  border-radius: 20px;
  &:before {
    margin: 0em;
    padding: 0em;
    border-radius: 50%;
    box-shadow: 0 0 0 350px rgba(#a3cef1, 1);
    content: "";
  }
}
.pr {
  .name-box {
    width: 255px;
  }
}
.pr-box {
  background-color: white;
  border-radius: 20px;
  // height: 150px;
  // width: 150px;
  .icon {
    font-size: 20px;
  }
}
</style>