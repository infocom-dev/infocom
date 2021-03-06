<template>
  <div class="login">
    <nav-bar></nav-bar>
    <b-container
      fluid
      class="login position-relative d-flex justify-content-center"
    >
      <b-form class="w-50 mx-auto" @submit.prevent="login">
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
        <b-button size="lg" variant="outline-warning" type="submit">Войти</b-button>
        <p class="mt-3">
          Ещё не зарегистрированы?
          <router-link to="/auth/signup"><h4>Регистрация</h4></router-link>
        </p>
      </b-form>
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
  background: url("../assets/images/09.jpg") no-repeat center center;
  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 650px;
  font-size: 1rem;
}
</style>