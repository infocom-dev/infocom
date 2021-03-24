<template>
  <div class="">
    <nav-bar></nav-bar>
    <section class="p-5 signup position-relative d-flex justify-content-center">
      <b-container fluid class="mx-auto">
        <div class="w-50  mx-auto">
          <b-row>
            <b-form class="register-box p-5 col w-50 mx-auto" @submit.prevent="register">
              <p v-if="err">{{ err }}</p>

              <div class="form-group required">
                <label class="control-label" for="username">Логин:</label>
                <b-input
                  v-model="form.username"
                  type="text"
                  id="username"
                  placeholder="Логин..."
                />

                <p>
                  <small>Минимальная длина логина 5 символов</small>
                </p>
              </div>

              <div class="form-group required">
                <b-form-group
                  id="input-group-1"
                  label="Email address:"
                  label-for="input-1"
                  description="We'll never share your email with anyone else."
                >
                  <b-form-input
                    id="input-1"
                    v-model="form.email"
                    type="email"
                    placeholder="Enter email"
                    required
                  ></b-form-input>
                </b-form-group>
              </div>

             

              <div class="form-group required">
                <label class="control-label" for="password">Пароль:</label>
                <b-input
                  v-model="form.password"
                  type="password"
                  id="password"
                  placeholder="Пароль..."
                ></b-input>
                <p>
                  <small>Минимальная длина пароля 6 символов</small>
                </p>
              </div>

              <div class="form-group required">
                <label class="control-label" for="repeatPassword"
                  >Повторите пароль:</label
                >
                <b-input
                  v-model="form.repeatPassword"
                  type="password"
                  id="repeatPassword"
                  placeholder="Повторите пароль..."
                />
              </div>

              <p class="text-danger" v-if="!$v.form.password.minLength">
                Длина пароля меньше 6 символов
              </p>

              <p class="text-danger" v-if="isPasswordTheSame">
                Введённые пароли не совпадают
              </p>
              <div class="">
                <a href="#" class="btn">Регистрация</a>
              </div>

              <p class="mt-2">
                <small>
                  Все поля отмеченные
                  <span class="text-danger">*</span> обязательны для заполнения.
                </small>
              </p>

              <p class="mt-3">
                Уже есть аккаунт?
                <router-link to="login"><h2>Вход</h2></router-link>
              </p>

            </b-form>
          
          </b-row></div
      ></b-container>
    </section>
    <Footer></Footer>
  </div>
</template>
<script>
import { required, minLength, sameAs } from "vuelidate/lib/validators";
import { IMaskDirective } from "vue-imask";
import authRequest from "../mixins/authRequest";
import NavBar from "./NavBar";
import Footer from "./Footer";
export default {
  name: "SignUpForm",
  components: {
    NavBar,
    Footer,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
        repeatPassword: "",
        email: "",
      },
      userEmail: "",


      err: "",
    };
  },
  validations: {
    form: {
      username: {
        required,
        minLength: minLength(5),
      },
      password: {
        required,
        minLength: minLength(6),
      },
      repeatPassword: {
        required,
        sameAs: sameAs("password"),
      },
      email: {
        required,
      },
      customerOrExecutor: {
        required,
      },
    },
  },
  computed: {
    formValid() {
      return this.$v.$invalid;
    },
    isPasswordTheSame() {
      const form = this.$v.form;
      return (
        form.password.required &&
        form.repeatPassword.required &&
        !form.repeatPassword.sameAs
      );
    },
  },
  mixins: [authRequest],
  methods: {
    async register() {
      // логика регистрации
      try {
        await this.authRequest("api/auth/users", this.form);
        // редиректим, если нет ошибки
        this.$router.push("/auth/signin");
      } catch (e) {
        console.error("AN API ERROR", e);
        this.err = e;
      }
    },
  },
  directives: {
    imask: IMaskDirective,
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
.form-group.required .control-label:after {
  content: " *";
  color: red;
}
.signup {
  background: url("../assets/images/step.jpg") no-repeat center center;
  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 1100px;
  font-size: 1rem;
}
.text {
  color: black !important;
}
.register-box {
  background-color: white;
  border-radius: 40px;
  box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0 10px 22px rgba(0, 0, 0, 0.2);
}
</style>