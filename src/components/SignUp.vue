<template>
  <div class="">
    <nav-bar></nav-bar>
    <b-container
      fluid
      class="signup position-relative d-flex justify-content-center"
    >
      <b-form class="w-50 mx-auto" @submit.prevent="register">
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
            <small 

    
              >Минимальная длина логина 5 символов</small
            >
          </p>
        </div>

        <div class="form-group required">
          <label class="control-label" for="phone">Номер телефона:</label>
          <b-input
            v-model="form.phone"
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
            <small 
              >Введите номер в формате: +7(921)123-45-67</small
            >
          </p>
        </div>

        <div class="form-group required">
          <label class="control-label" for="customerOrExecutor"
            >Вы заказчик или исполнитель?</label
          >
          <b-select
            v-model="form.customerOrExecutor"
            :options="customerOrExecutorOptions"
            type="customerOrExecutor"
            id="customerOrExecutor"
          />
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
            <small
              >Минимальная длина пароля 6 символов</small
            >
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

        <b-button size="lg" variant="outline-warning" type="submit" :disabled="formValid"
          >Регистрация</b-button
        >

        <p class="mt-2">
          <small >
            Все поля отмеченные <span class="text-danger">*</span> обязательны
            для заполнения.
          </small>
        </p>

        <p class="mt-3">
          Уже есть аккаунт? <router-link to="/auth/signin"><h4>Вход</h4></router-link>
        </p>
      </b-form>
    </b-container>
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
        phone: "",
        customerOrExecutor: "",
      },
      userPhone: "",
      customerOrExecutorOptions: [
        { text: "Выберите...", value: "", disabled: true, selected: true },
        { text: "Заказчик", value: "customer" },
        { text: "Исполнитель", value: "executor" },
      ],
      phoneNumberMask: {
        mask: "+{7}(000)000-00-00",
        lazy: true,
      },
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
      phone: {
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
    onAccept(e) {
      const maskRef = e.detail;
      this.form.phone = maskRef.value;
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
  background: url("../assets/images/09.jpg") no-repeat center center;
  background-size: cover;
  // position: relative;
  flex-direction: column;
  height: 850px;
  font-size: 1rem;
}
.text{
  color: black !important;
}

</style>