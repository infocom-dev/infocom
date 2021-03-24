<template>
  <div class="">
    <nav-bar></nav-bar>
    <b-container
      fluid
      class="login position-relative d-flex justify-content-center"
    >
      <div class="login_box w-50 mx-auto p-5">
        <b-row align-v="center" class="justify-content-center">
          <b-form class="w-50 col" @submit.prevent="login">
            <div class="form-group">
              <label for="username">Логин:</label>
              <b-input
                v-model="form.username"
                type="text"
                id="username"
                placeholder="Логин..."
              ></b-input>
            </div>
            <div class="form-group">
              <label for="password">Пароль:</label>
              <b-input
                v-model="form.password"
                type="password"
                id="password"
                placeholder="Пароль..."
              ></b-input>
            </div>
            <div class="">
              <a href="#" class="btn">Войти</a>
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
import authRequest from "../mixins/authRequest";
import NavBar from "./NavBar.vue";
import Footer from "./Footer.vue";
export default {
  name: "SignInForm",
  components: {
    NavBar,
    Footer,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
  mixins: [authRequest],
  methods: {
    async login() {
      // логика авторизации
      try {
        const response = await this.authRequest(
          "api/auth/token/login",
          this.form
        );
        // авторизуем юзера
        this.setLogined(response.data.token);
      } catch (error) {
        console.error("AN API ERROR:", error);
      }
    },
    setLogined(token) {
      // сохраняем токен
      console.log(token);
      localStorage.setItem("token", token);
    },
  },
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