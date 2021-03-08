<template>
  <div class="v-contact-us pb-3">
    <b-container fluid class="after w-100 mx-0 px-0"></b-container>
    <b-container class="pt-3">
      <form class="vue-form" @submit.prevent="submit">
        <div class="error-message">
          <p v-show="!email.valid">Oh, please enter a valid email address.</p>
          <p v-show="email.valid">Contact Form</p>
        </div>

        <fieldset>

          <div>
            <label class="label" for="name">Name</label>
            <input
              type="text"
              name="name"
              id="name"
              required=""
              v-model="name"
            />
          </div>
          <div>
            <label class="label" for="email">Email</label>
            <input
              type="email"
              name="email"
              id="email"
              required=""
              :class="{ email, error: !email.valid }"
              v-model="email.value"
            />
          </div>
          <div>
            <label class="label" for="textarea">Leave a coment</label>
            <textarea
              class="message"
              name="textarea"
              id="textarea"
              required=""
              v-model="message.text"
              :maxlength="message.maxlength"
            ></textarea>
            <span class="counter"
              >{{ message.text.length }} / {{ message.maxlength }}</span
            >
          </div>

          <div class="">
            <b-button size="lg" variant="outline-warning"
              >Send form</b-button
            >
          </div>
        </fieldset>
      </form>
    </b-container>

    <!-- <div class="debug">
      <pre><code>{{ $data }}</code></pre>
    </div> -->
  </div>
</template>
<script>
export default {
  name: "v-contact-us",
  data: function () {
    return {
      name: "John Doe",
      email: {
        value: "example@com",
        valid: true,
      },
      message: {
        text: `Dear Mr. President,\n...`,
        maxlength: 255,
      },
      submitted: false,
    };
  },
  methods: {
    // submit form handler
    submit: function () {
      this.submitted = true;
    },
    // validate by type and value
    validate: function (type, value) {
      if (type === "email") {
        this.email.valid = this.isEmail(value) ? true : false;
      }
    },
    // check for valid email adress
    isEmail: function (value) {
      var emailRegExp = /^[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
      return emailRegExp.test(value);
    },
    // check or uncheck all
    checkAll: function (event) {
      this.selection.features = event.target.checked ? this.features : [];
    },
  },
  watch: {
    // watching nested property
    "email.value": function (value) {
      this.validate("email", value);
    },
  },
};
</script>
<style lang="scss">
@import "../assets/styles/base.scss";
@import url("https://fonts.googleapis.com/css?family=Source+Code+Pro:300,400");
.v-contact-us {
  background: url("../assets/images/06.jpg");
  padding-bottom: 50px;
}
.after {
  content: "";
  background-image: url('data:image/svg+xml;utf-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1" preserveAspectRatio="none"><polygon style="fill:white;" points="0.5,0.5 0,0 1,0 "/></svg>');
  background-size: 30px 30px;
  height: 30px;
}
.vue-form {
  font-size: 16px;
  width: 100%;
  padding: 15px 30px;
  border-radius: 4px;
  margin: 50px auto;
  // width: 500px;
  background-color: $blu;
  box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.3);
}
.vue-form fieldset {
  margin: 24px 0 0 0;
}
.vue-form legend {
  padding-bottom: 10px;
  border-bottom: 1px solid #ecf0f1;
}
.vue-form div {
  position: relative;
  margin: 20px 0;
  padding-left: 40px;
  padding-right: 40px;
}
.vue-form h4,
.vue-form .label {
  color: #94aab0;
  margin-bottom: 10px;
}
.vue-form .label {
  display: block;
}
.vue-form input,
.vue-form textarea,
.vue-form label {
  color: #2b3e51;
}
.vue-form input[type="text"],
.vue-form input[type="email"],
.vue-form textarea,
.vue-form legend {
  display: block;
  width: 100%;
  appearance: none;
}
.vue-form input[type="text"],
.vue-form input[type="email"],
.vue-form textarea {
  padding: 12px;
  // border: 1px solid #cfd9db;
  background-color: #ffffff;
  border-radius: 0.25em;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.08);
}
.vue-form input[type="text"]:focus,
.vue-form input[type="email"]:focus,
.vue-form textarea:focus {
  outline: none;
  border-color: #2c3e50;
  box-shadow: 0 0 5px rgba(44, 151, 222, 0.2);
}
.vue-form {
  position: relative;
  // padding: 40px;
}
.vue-form {
  margin-top: 16px;
}
.vue-form {
  clear: both;
  content: "";
  display: table;
}
.vue-form {
  // display: inline-block;
  position: relative;
  user-select: none;
  margin: 0 26px 16px 0;
  // float: left;
}
.vue-form textarea {
  min-height: 120px;
  resize: vertical;
  overflow: auto;
}
.vue-form input[type="submit"] {
  border: none;
  background: #2c3e50;
  border-radius: 0.25em;
  padding: 12px 20px;
  color: #ffffff;
  font-weight: bold;
  float: right;
  cursor: pointer;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  appearance: none;
}
.no-touch .vue-form input[type="submit"]:hover {
  background: #42a2e1;
}
.vue-form input[type="submit"]:focus {
  outline: none;
  background: #2b3e51;
}
.vue-form input[type="submit"]:active {
  transform: scale(0.9);
}
.vue-form .error-message {
  height: 35px;
  margin: 0px;
}
.vue-form .error-message p {
  background: $rs;
  color: #ffffff;
  font-size: 1.4rem;
  text-align: center;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  border-radius: 0.25em;
  padding: 16px;
}
.vue-form .error {
  border-color: black !important;
}
.vue-form .counter {
  background-color: #ecf0f1;
  position: absolute;
  right: 0px;
  top: 0px;
  font-size: 10px;
  padding: 4px;
}
.debug {
  border-radius: 4px;
  margin: 50px auto;
  width: 500px;
  background-color: #000;
  padding: 50px;
  background: rgba(0, 0, 0, 0.8);
  box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.3);
}
.debug pre {
  color: #ffffff;
  font-size: 18px;
  line-height: 30px;
  font-family: "Source Code Pro", monospace;
  font-weight: 300;
  white-space: pre-wrap;
}
@-webkit-keyframes cd-bounce {
  0%,
  100% {
    -webkit-transform: scale(1);
  }
  50% {
    -webkit-transform: scale(0.8);
  }
}
@-moz-keyframes cd-bounce {
  0%,
  100% {
    -moz-transform: scale(1);
  }
  50% {
    -moz-transform: scale(0.8);
  }
}
@keyframes cd-bounce {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(0.8);
  }
}
</style> 