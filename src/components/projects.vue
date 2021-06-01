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
          <!-- <p>{{ projects }}</p> -->
          <b-container fluid class="w-100 overview p-0 pb-5">
            <b-row align-v="center" class="text-center ml-5">
              <b-col cols="2" md="1" class="mt-5 text-left">
                <i class="fas fa-search icon"></i>
              </b-col>
              <div class="col mt-5 p-0 text-left">
                <h3>Guide to start new project</h3>
              </div>
            </b-row>
            <v-form :questions="questions"></v-form>
            <b-row
              align-v="center"
              class="text-center justify-content-center mr-5 ml-5"
            >
              <b-col cols="2" md="1" class="pl-2 text-left">
                <i class="fas fa-chart-area icon"></i>
              </b-col>
              <b-col cols="10" md="11" class="p-0 text-left">
                <h3>Last project in analysis</h3>
              </b-col>
              <div class="col"></div>
            </b-row>
            <b-container v-if="projects.length" class="p-0" fluid>
              <b-row class="p-0 m-0">
                <div class="w-100 p-0">
                  <b-row align-h="center" class="p-0 m-0">
                    <b-col cols="9" md="3" class="m-5 anketa-box">
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
                      <div v-else class="text-center mb-4">
                        <h5>
                          Наша нейронная сеть оценала заказ в $
                          {{ projects[projects.length - 1].predicted_price }}.
                        </h5>
                      </div>
                    </b-col>
                    <b-col
                      style="background-color: #a3cef1"
                      class="anketa-box m-5 d-flex justify-content-center offset-sm-1"
                    >
                      <div
                        v-if="
                          projects[projects.length - 1].predicted_price == null
                        "
                        class="m-3 justify-content-center d-flex align-item-center"
                      >
                        <loading></loading>
                      </div>
                      <div
                        v-else
                        class="w-100 m-3 p-4 justify-content-center m-auto"
                      >
                        <div>
                          <h5 class="text-center forward">
                            Почему получилась такая стоимость?
                          </h5>
                          <hr class="forward" />
                          <div class="graph__wrapper m-auto">
                            <svg
                              width="315px"
                              height="107px"
                              viewBox="0 0 315 107"
                              version="1.1"
                              style="overflow: visible"
                            >
                              <g
                                id="Page-1"
                                stroke="none"
                                stroke-width="1"
                                fill="none"
                                fill-rule="evenodd"
                                sketch:type="MSPage"
                              >
                                <path
                                  d="M2.10546875,95.75 L40.5546875,68.3476562 L55.2109375,81.1796875 L65.2148437,76.3945312 L96.1835937,86.8320312 L131.023438,19.9414062 L142.15625,23.7226562 L183.605469,2.1953125 L211.007812,22.3320312 L234.320312,71.5664062 L234.667969,83.0039062 L244.019531,83.0039062 L247.105469,88.8320312 L312.695312,104.839844"
                                  id="Path-1"
                                  stroke="#e7ecef"
                                  stroke-width="4"
                                  sketch:type="MSShapeGroup"
                                  class="path"
                                ></path>

                                <polyline
                                  id="arrow"
                                  points="0,-5 10,0 0,5 1,0"
                                  fill="#e7ecef"
                                >
                                  <animateMotion
                                    rotate="auto"
                                    begin="1s"
                                    dur="15s"
                                    repeatCount="1"
                                    fill="freeze"
                                  >
                                    <mpath xlink:href="#Path-1" />
                                  </animateMotion>
                                </polyline>
                              </g>
                            </svg>
                          </div>
                          <b-row align-v="center" class="w-100 forward">
                            <b-col cols="9" md="10">
                              <p class="m-auto">
                                Средняя цена на приложение со стеком
                                {{ projects[projects.length - 1].stack }}:
                              </p>
                            </b-col>
                            <b-col cols="3" md="2">
                              <h3 class="m-auto">${{ avg_price }}</h3>
                            </b-col>
                          </b-row>

                          <b-row align-v="center" class="forward pt-3">
                            <b-col cols="9" md="10"
                              ><p class="m-auto">
                                Средняя продолжительность проекта (в днях):
                              </p></b-col
                            >
                            <b-col cols="3" md="2">
                              <h3 class="m-auto">{{ avg_days }}</h3>
                            </b-col>
                          </b-row>
                        </div>
                      </div>
                    </b-col>
                  </b-row>
                </div>
              </b-row>
            </b-container>

            <b-row align-v="center" v-else class="p-0 m-0 no-result">
              <div class="mr-5 ml-5 w-100 box2">
                <no-result></no-result>
              </div>
            </b-row>
            <b-row
              v-if="projects.length > 1"
              align-v="center"
              class="text-center mr-5 ml-5"
            >
              <b-col cols="2" md="1" class="pl-2 text-left">
                <i class="fas fa-tasks projects-icon icon"></i>
              </b-col>
              <div class="col p-0 text-left">
                <h3>ALL PROJECTS FINISHED ANALYSIS</h3>
              </div>
            </b-row>
            <div v-if="projects.length > 1">
              <div
                v-for="(item, index) in projects"
                :key="index"
                class="w-100 p-0"
              >
                <div
                  v-if="
                    item.predicted_price != null && index != projects.length - 1
                  "
                  class="m-5"
                >
                  <b-row align-v="stretch" class="p-0 m-0 anketa-box">
                    <b-col cols="12" md="4" class="p-4  pr-col">
                      <h5 class="name-box w-100 text-center p-2 mx-auto">
                        {{ item.name }} on {{ item.stack }}
                      </h5>
                      <p class="m-0 pt-">Status</p>
                      <div v-if="item.is_active">
                        <h1>In develop</h1>
                      </div>
                      <div
                        v-else-if="
                          !item.is_active && item.real_end_date != null
                        "
                      >
                        <h1>Finnished</h1>
                      </div>
                      <div v-else>
                        <h1>From analysis</h1>
                      </div>
                    </b-col>
                    <b-col cols="12" md="3" class=" p-4 " style="">
                      <p class="m-0">
                        <small>Predicted price</small>
                      </p>
                      <h3>$ {{ item.predicted_price }}</h3>
                      <p class="m-0">Real price</p>
                      <div v-if="!item.is_active && item.real_end_date != null">
                        <h3>$ {{ item.real_price }}</h3>
                      </div>
                      <div v-else>
                        <h3>Soon</h3>
                      </div>
                    </b-col>
                    <b-col cols="12" md="4"  class="p-4" style="">
                      <p class="m-0">
                        <small>Predicted date</small>
                      </p>
                      <h3>{{ item.predict_end_date }}</h3>
                      <p class="m-0">Real date</p>
                      <div v-if="!item.is_active && item.real_end_date != null">
                        <h3>{{ item.real_end_date }}</h3>
                      </div>
                      <div v-else>
                        <h3>Soon</h3>
                      </div>
                    </b-col>
                    <b-col cols="12" md="1"  class="pr-button ">
                      <div class="m-auto"><p>View answers</p></div>
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
import Loading from "./Loading";
import VForm from "./v-form.vue";
import NoResult from "./no_result";

// import vAnswers from "./v-answers.vue";
import session from "../api/session";
import axios from "axios";
export default {
  components: {
    sideBarAccount,
    Loading,
    VForm,
    NoResult,
    //  vAnswers
  },
  name: "projects",

  data() {
    return {
      top: 100,
      top2: 0,
      user_mail: "",
      user_id: "",
      user_username: "",
      questions: [],
      projects: [],
      avg_price: 0,
      avg_days: 0,
    };
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
          axios
            .get(
              `/getAvgStack${this.projects[this.projects.length - 1].stack}/`
            )
            .then((response) => {
              this.avg_price = response.data.avg_price;
              this.avg_days = response.data.avg_days;
            });
        });
        console.log(this.user_mail);
      })
      .catch((err) => {
        console.log(err);
      });
  },
  methods: {},
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
  hr {
    background-color: $rs;
    height: 5px;
    border: 0;
  }
  .pr-col {
    background-color: #a3cef1;
    // border-radius: 20px 0 0 20px;
  }
  .no-result {
    .box2 {
      background-color: white;
      margin: 0em auto;
      border-radius: 20px;
      &:before {
        margin: 4em;
        padding: 3em;
        border-radius: 50%;
        background: #a3cef1;
        box-shadow: 0 0 0 350px rgba(#a3cef1, 1);
        content: "";
      }
    }
  }
  .pr-button {
    background-color: #ffd037;
    // border-radius: 0 20px 20px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    p {
      color: white;
    }

    text-align: center;
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

.user-icon {
  font-size: 80px;
  color: $blu;
}
.mail-icon {
  color: $blu;
}
.bell-icon,
.out-icon {
  font-size: 30px;
  color: $blu;
}
.badgex {
  padding: 0px 5px 1px;
  position: absolute;
  top: -5px;
  right: -10px;
  display: inline-block;
  min-width: 10px;
  font-size: 18px;
  box-sizing: border-box;
  font-weight: bold;
  color: #ffffff;
  line-height: 1;
  white-space: nowrap;
  text-align: center;
  border-radius: 50%;
}
.badge-danger {
  background-color: #db5565;
}
.bellhold {
  position: relative;
  cursor: pointer;
}
.overview {
  background-color: #e7ecef;
  // height: 900px;
}
.overview-box {
  background-color: #ffffff;
}

.forward {
  position: relative;
  z-index: 7;
}

.graph__wrapper {
  position: absolute;
  top: 0px;
  left: 10%;
  z-index: 1;
  // width: 400px;
  // margin: 30px auto;
  // position: relative;
  svg {
    // top:-110px;
    height: 180px;
    width: 100%;
    // height: 100px;
    // position: absolute;
    // margin: 36px 0px 0px 15px;
  }
}
.path {
  stroke-dasharray: 428;
  stroke-dashoffset: 428;
  animation: dash 15s linear forwards;
  animation-iteration-count: 1;
  animation-delay: 1s;
}
@keyframes dash {
  to {
    stroke-dashoffset: 0;
  }
}
.description {
  font-family: "Roboto";
  color: lighten(#303030, 50%);
  text-align: center;
  margin: 40px 0px;
}
</style>

