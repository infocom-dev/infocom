<template>
  <div class="">
    <nav-bar></nav-bar>
    <section class="p-5 signup position-relative d-flex justify-content-center">
      <b-container fluid class="mx-auto w-75">
        <div class="mx-auto p-5 register-box">
          <template v-if="registrationLoading"> loading... </template>
          <div v-else-if="!registrationCompleted">
            <b-row align-v="center" class="justify-content-center">
              <b-form class="col w-50" @submit.prevent="submit">
                <div class="error-message">
                  <p v-show="registrationError">
                    Ваша почта недействительна либо вы уже есть в нашей базе
                    данных
                  </p>
                </div>

                <div class="form-group required">
                  <label class="control-label" for="phone">Почта:</label>
                  <b-form-group
                    id="input-group-1"
                    label-for="input-1"
                    description="We'll never share your email with anyone else."
                  >
                    <b-input
                      type="email"
                      name="email"
                      id="email"
                      required
                      :class="{ email, error: !emailValid }"
                      v-model="inputs.email"
                    />
                    <p v-show="!emailValid">
                      Oh, please enter a valid email address.
                    </p>
                  </b-form-group>
                </div>
                <div class="form-group required">
                  <label class="control-label" for="phone"
                    >Номер телефона:</label
                  >
                  <b-input
                    v-model="inputs.phone"
                    type="text"
                    id="phone"
                    v-imask="phoneNumberMask"
                    placeholder="+7(921)123-45-67"
                    @keypress="isNumber"
                    @accept="onAccept"
                    @complete="onComplete"
                    maxlength="16"
                  />

                  <p>
                    <small>Введите номер в формате: +7(921)123-45-67</small>
                  </p>
                </div>
                <div class="form-group required">
                  <label class="control-label" for="password">Пароль:</label>
                  <b-input
                    v-model="inputs.password1"
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
                    v-model="inputs.password2"
                    type="password"
                    id="repeatPassword"
                    placeholder="Повторите пароль..."
                  />
                </div>
                <p class="text-danger" v-if="!$v.inputs.password1.minLength">
                  Длина пароля меньше 6 символов
                </p>

                <p
                  class="text-danger"
                  v-if="
                    $v.inputs.password1.required &&
                    $v.inputs.password2.required &&
                    !$v.inputs.password2.sameAs
                  "
                >
                  Введённые пароли не совпадают
                </p>
                <p class="mt-2">
                  <small>
                    Все поля отмеченные
                    <span class="text-danger">*</span> обязательны для
                    заполнения.
                  </small>
                </p>
                <div class="">
                  <button
                    :disabled="formValid"
                    @click="createAccount(inputs)"
                    class="btn"
                  >
                    Регистрация
                  </button>
                </div>

                <p class="mt-3">
                  Уже есть аккаунт?
                  <router-link to="/login"><h2>Вход</h2></router-link>
                </p>
              </b-form>
              <div class="col mx-auto">
                <b-img
                  style="min-width: 200px"
                  fluid
                  center
                  class=""
                  :src="require('../assets/images/login2.jpg')"
                /></div
            ></b-row>
          </div>
          <template v-else>
            <div>
              Registration complete. You should receive an email shortly with
              instructions on how to activate your account.
            </div>
            <div>
              <router-link to="/login">return to login page</router-link>
            </div>
          </template>
        </div>
      </b-container>
    </section>

    <Footer></Footer>
  </div>
</template>

<script>
import { required, minLength, sameAs } from "vuelidate/lib/validators";
import { IMaskDirective } from "vue-imask";

import NavBar from "./NavBar";
import Footer from "./Footer";
import { mapActions, mapState } from "vuex";
export default {
  components: {
    NavBar,
    Footer,
  },
  validations: {
    inputs: {
      password1: {
        required,
        minLength: minLength(6),
      },
      password2: {
        required,
        sameAs: sameAs("password1"),
      },
      email: {
        required,
      },
      phone: {
        required,
      },
    },
  },
  data() {
    return {
      inputs: {
        password1: "",
        password2: "",
        email: "",
        phone: "",
      },
      emailValid: true,
      userPhone: "",
      phoneNumberMask: {
        mask: "+{7}(000)000-00-00",
        lazy: true,
      },
    };
  },
  computed: {
    formValid() {
      return this.$v.$invalid;
    },
    ...mapState("signup", [
      "registrationCompleted",
      "registrationError",
      "registrationLoading",
    ]),
  },
  methods: {
    onAccept(e) {
      const maskRef = e.detail;
      this.inputs.phone = maskRef.value;
    },
    onComplete(e) {
      const maskRef = e.detail;
      this.userPhone = maskRef.unmaskedValue;
    },
    isNumber(e) {
      const regex = /[0-9]/;
      if (!regex.test(e.key)) {
        e.returnValue = false;
        if (e.preventDefault) e.preventDefault();
      }
    },
    validate: function (type, value) {
      if (type === "email") {
        this.emailValid = this.isEmail(value) ? true : false;
      }
    },
    // check for valid email adress
    isEmail: function (value) {
      var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;

      return emailRegExp.test(value);
    },
    ...mapActions("signup", ["createAccount", "clearRegistrationStatus"]),
    beforeRouteLeave(to, from, next) {
      this.clearRegistrationStatus();
      next();
    },
  },
  directives: {
    imask: IMaskDirective,
  },
  watch: {
    // watching nested property
    "inputs.email": function (value) {
      this.validate("email", value);
    },
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
  span {
    color: black;
  }
}
.error-message p {
  background: $rs;
  color: #ffffff;
  font-size: 1.4rem;
  text-align: center;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  border-radius: 0.25em;
  padding: 16px;
}
button.btn {
  border-radius: 40px;
  color: #fff;
  display: block;
  text-align: center;
  text-decoration: none;
}
button.btn {
  background-color: #2e2892;
  // border: 1px solid rgb( 33, 126, 74 );
}

button.btn:hover {
  background-color: #274c77;
  color: white;
}
</style>