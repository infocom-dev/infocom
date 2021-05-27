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
                class="text-center my-auto justify-content-center ml-5"
              >
                <div class="col-4 p-0 text-left">
                  <i class="fa fa-folder-open pr-icon"></i>
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
                      <h5 class="m-3">{{ analysis_pr[0].name }}</h5>
                    </div>
                    <div
                      v-if="analysis_pr[0].status == 'in progress'"
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
                        {{ analysis_pr[0].old_budjet }}.
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
                          Cras mattis consectetur purus sit amet fermentum. Cras
                          justo odio, dapibus ac facilisis in, egestas eget
                          quam. Morbi leo risus, porta ac consectetur ac,
                          vestibulum at eros.
                        </p>
                      </b-modal>
                    </div>
                  </b-col>
                  <b-col
                    class="anketa-box d-flex justify-content-center offset-sm-1"
                  >
                    <div
                      v-if="analysis_pr[0].status == 'in progress'"
                      class="m-3"
                    >
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
                            <b-col v-if="analysis_pr[0].new_budjet">
                              <h5>
                                New budjet : {{ analysis_pr[0].new_budjet }}
                              </h5>
                            </b-col>
                          </b-row>
                        </b-container>
                      </b-row>
                    </div>
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
            <div v-for="(item, id) in analysis_pr" :key="id" class="w-100 p-0">
              <b-row class="pr-5 pl-5 m-0">
                <b-col class="p-0 mr-5 pr-box text-center" style="">
                  <h5 class="name-box p-3 m-4 mx-auto">Project info</h5>
                  <h5 class="pb-3 pl-3 pr-3 mx-auto">{{ item.info }}</h5>
                </b-col>
                <b-col class="p-0 mr-5 pr-box text-center" style="">
                  <h5 class="name-box p-3 m-4 mx-auto">Budjet</h5>
                  <h5>$ {{ item.old_budjet }}</h5>
                </b-col>
                <b-col
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
                  <b-button
                    v-b-modal.modal4
                    style="background-color: #ffd037"
                    class="mx-auto w-100"
                    >Set options</b-button
                  >
                  <b-modal
                    id="modal4"
                    size="lg"
                    scrollable
                    title="Set new options for this project"
                    header-bg-variant="primary"
                  >
                    <div v-if="item.answers" class="text-center">
                      <h5>
                        Наша нейронная сеть оценала заказ в $
                        {{ item.old_budjet }}.
                      </h5>
                      <p>Вы можете изменить настройки ниже</p>
                      <div v-for="(f, index) in feature" :key="index">
                        <b-row align-v="center" class="d-flex m-3">
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
                    </div>
                    <template #modal-footer="{ submit, cancel }">
                      <a href="#" @click="submit()" class="btn text-uppercase"
                        >Submit data
                      </a>
                      <!-- Emulate built in modal footer ok and cancel button actions -->
                      <a href="#" @click="cancel()" class="btn text-uppercase"
                        >Cancel
                      </a>

                      <!-- Button with custom close trigger value -->
                    </template>
                  </b-modal>
                  <b-button class="mx-auto w-100">Make order</b-button>
                </b-col>
              </b-row>
            </div>
          </b-container>
        </b-container>
      </b-container>
    </b-row>
  </div>
</template>
<script>
import sideBarAccount from "./side-bar-account.vue";
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/default.css";
import "vue-slider-component/theme/default.css";
import Graph from "./Graph.vue";
import VForm from "./v-form.vue";
import vAnswers from "./v-answers.vue";
import session from '../api/session';
export default {
  components: { sideBarAccount, Graph, VueSlider, VForm, vAnswers },
  name: "projects",

  data() {
    return {
      componentKey: 0,
      feature: ["Дешево", "Качественно", "Быстро"],
      answers: [50, 10, 20],
      questions:[],
      // questions: [
      //   {
      //     id: "1",
      //     text: "Какие задачи должен решать чат-бот?",
      //     type: "selected",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "обработка типовых сообщений ",
      //       },
      //       {
      //         id: 2,
      //         value: "рассылка подписчикам",
      //       },
      //       {
      //         id: 3,
      //         value: "фильтрация поступающих заявок",
      //       },
      //       {
      //         id: 4,
      //         value: "мгновенная реакция на сообщения ",
      //       },
      //     ],
      //   },
      //   {
      //     id: "2",
      //     text: "Где  должен размещаться чат-бот?",
      //     type: "checkbox",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "сайт",
      //       },
      //       {
      //         id: 2,
      //         value: "мессенджеры",
      //       },
      //       {
      //         id: 3,
      //         value: "личный кабинет",
      //       },
      //       {
      //         id: 4,
      //         value: "мобильное  приложение",
      //       },
      //       {
      //         id: 5,
      //         value: "гаджет",
      //       },
      //     ],
      //   },
      //   {
      //     id: "3",
      //     text:
      //       "Укажите минимальное и максимальное кол-во посетителей приложения, в котором планируется использование чат-бота (для каждого канала)?",
      //     type: "range",
      //     min: 0,
      //     max: 250,
      //     answers: [0, 250],
      //   },
      //   {
      //     id: "4",
      //     text: "Введидте ожидаемая нагрузку (кол-во обращений) на чат-бота",
      //     type: "message",
      //     answers: [],
      //   },
      //   {
      //     id: "5",
      //     text: "Какой формат диалога предпочтительнее?",
      //     type: "checkbox",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "Свободное общение",
      //       },
      //       {
      //         id: 2,
      //         value: "работа по фиксированному сценарию диалога ",
      //       },
      //     ],
      //   },
      //   {
      //     id: "6",
      //     text: "На каких языках должен вести диалог чат-бот?",
      //     type: "selected",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "English",
      //       },
      //       {
      //         id: 2,
      //         value: "Russian",
      //       },
      //     ],
      //   },
      //   {
      //     id: "7",
      //     text: "Добавить встроенную платёжную систёма",
      //     type: "switch",
      //     answers: [],
      //   },
      //   {
      //     id: "8",
      //     text: "Добавить безопасную сделку",
      //     type: "switch",
      //     answers: [],
      //   },
      //   {
      //     id: "9",
      //     text: "Добавить работу с геолокацией",

      //     type: "switch",
      //     answers: [],
      //   },
      //   {
      //     id: "10",
      //     text:
      //       "Добавить переключение диалога на оператора по запросу  пользователя",

      //     type: "switch",
      //     answers: [],
      //   },
      //   {
      //     id: "11",
      //     text:
      //       "Должен ли чат-бот взаимодействовать с другими ботами, сайтами?",
      //     type: "checkbox",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "Да",
      //       },
      //       {
      //         id: 2,
      //         value: "Нет",
      //       },
      //     ],
      //   },
      //   {
      //     id: "12",
      //     text: "Есть ли у этих систем API? ",
      //     type: "checkbox",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "Да",
      //       },
      //       {
      //         id: 2,
      //         value: "Нет",
      //       },
      //     ],
      //   },
      //   {
      //     id: "13",
      //     text: "Способ  поставки продукта:",
      //     type: "selected",
      //     answers: [
      //       {
      //         id: 1,
      //         value: "SaaS (облачный сервис Инфоком-НН)",
      //       },
      //       {
      //         id: 2,
      //         value: "азмещение интеграционного модуля на серверах Заказчика",
      //       },
      //       {
      //         id: 3,
      //         value: "олное размещение на серверах Заказчика",
      //       },
      //     ],
      //   },
      //   {
      //     id: "14",
      //     text: "Сроки выполнения проекта",
      //     type: "datapicker",
      //     answers: [],
      //   },
      //   {
      //     id: "15",
      //     text: "Укажите бюджет проекта (диапазон):",
      //     type: "range",
      //     answers: [0, 1000000],
      //   },
      //   {
      //     id: "16",
      //     text: "Ваши примечания, пожелания, которые не вошли в Бриф:",
      //     type: "textarea",
      //     answers: [],
      //   },
      // ],
      analysis_pr: [
        {
          name: "Infocom",
          info: "Web site on vuejs + django",
          status: "",
          old_budjet: "1 000 000",
          new_budjet: "1 500 000",
          answers: [
            {
              id: "1",
              type: "selected",
              answers: [{ id: 1, value: "обработка типовых сообщений " }],
            },
            { id: "2", type: "checkbox", answers: [{ id: 1, value: "сайт" }] },
            { id: "3", type: "range", answers: [100, 250] },
            { id: "4", type: "message", answers: ["52"] },
            {
              id: "5",
              type: "checkbox",
              answers: [{ id: 1, value: "Свободное общение" }],
            },
            {
              id: "6",
              type: "selected",
              answers: [{ id: 2, value: "Russian" }],
            },
            { id: "7", type: "switch", answers: [true] },
            { id: "8", type: "switch", answers: [false] },
            { id: "9", type: "switch", answers: [false] },
            { id: "10", type: "switch", answers: [false] },
            { id: "11", type: "checkbox", answers: [{ id: 1, value: "Да" }] },
            { id: "12", type: "checkbox", answers: [{ id: 1, value: "Да" }] },
            {
              id: "13",
              type: "selected",
              answers: [
                {
                  id: 2,
                  value:
                    "азмещение интеграционного модуля на серверах Заказчика",
                },
              ],
            },
            {
              id: "14",
              type: "datapicker",
              answers: ["04.05.2021", "20.05.2021"],
            },
            { id: "15", type: "range", answers: [600000, 1000000] },
            { id: "16", type: "textarea", answers: ["ghjklhy"] },
          ],
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
  created() {
    session
      .get("/getQuestions/")
      .then((response) => {
        
        this.questions = response.data;
        console.log(this.questions)
      })
      .catch((err) => {
        console.log(err);
      });
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
  // height: 150px;
  width: 150px;
  .icon {
    font-size: 20px;
  }
}
</style>