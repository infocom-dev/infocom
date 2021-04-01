<template>
  <div class="">
    <nav-bar></nav-bar>
    <b-container
      fluid
      class="login position-relative d-flex justify-content-center"
    >
      <div class="login_box w-50 mx-auto p-5">
        <p v-show="error">
          Введены неправильный пароль или логин
        </p>
        <!-- <div v-if="!error" router.push({ name: home}) ></div> -->

        <b-row align-v="center" class="justify-content-center">
          <b-form class="w-50 col">
            <div class="form-group">
              <label for="username">Логин:</label>
              <b-input
                v-model="inputs.username"
                type="text"
                id="username"
                placeholder="Логин..."
              ></b-input>
            </div>
            <div class="form-group">
              <label for="password">Пароль:</label>
              <b-input
                v-model="inputs.password"
                type="password"
                id="password"
                placeholder="Пароль..."
              ></b-input>
            </div>

            <div class="">
              <a href="#" @click="login(inputs)" class="btn">Войти</a>
            </div>

            <p class="text-center">
              Ещё не зарегистрированы?
              <router-link to="/register"><h2>Регистрация</h2></router-link>
            </p>
          </b-form>
          <div class="col">
            <b-img
              style="min-width: 200px"
              fluid
              center
              class=""
              :src="require('../assets/images/register2.jpg')"
            />
          </div>
        </b-row>
      </div>
    </b-container>
    <Footer></Footer>
  </div>
</template>
<script>
import NavBar from "./NavBar.vue";
import Footer from "./Footer.vue";
import { mapState } from "vuex";
export default {
  components: {
    NavBar,
    Footer,
  },
  data() {
    return {
      inputs: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login({ username, password }) {
      this.$store
        .dispatch("auth/login", { username, password })
        
        // .catch(() => this.$router.push("/login"))
        // .then(() => this.$router.push("/"))
    },
  },
  computed:{
    ...mapState("auth", [
      "error",
    ]),
  }
};
</script>

<style lang="scss">
.login {
  // background: url("../assets/images/bg_technology.png") no-repeat center center;
  background: url("../assets/images/step.jpg") no-repeat center center;
  background-size: cover;
  // position: relative;
  flex-direction: column;

  height: 100vh;
}
.login_box {
  // background-color: #a3cef1;
  // background: url('../assets/images/bg_login.png') center no-repeat;
  background-color: white;
  border-radius: 40px;
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
}
</style>

