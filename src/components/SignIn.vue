<template>
  <div class="login">
    <nav-bar></nav-bar>
  
    <b-container
      fluid
      class="login position-relative d-flex justify-content-center"
    >  <p v-if="incorrectAuth">
      Incorrect username or password entered - please try again
    </p>
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
        <b-button size="lg" variant="outline-warning" type="submit"
          >Войти</b-button
        >
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
        
      },incorrectAuth: false,
    };
  },
  mixins: [authRequest],
  methods: {
    login() {
      this.$store
        .dispatch("userLogin", {
          username: this.form.username,
          password: this.form.password,
        })
        .then(() => {
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          console.log(err);
          this.incorrectAuth = true;
        });
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