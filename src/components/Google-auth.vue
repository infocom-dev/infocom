<template>
  <div id="google_auth">
    <!-- <script  type="application/javascript" defer src="https://apis.google.com/js/api:client.js"></script> -->
    <div class="container">
      <div class="columns" style="margin-top: 100px">
        <div class="column col-2 centered">
          <g-signin-button
            v-if="isEmpty(user)"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError"
          >
            <button class="btn btn-block btn-success">Google Signin</button>
          </g-signin-button>
          <!-- <user-panel v-else :user="user"></user-panel> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script >
import Vue from "vue";
import axios from "axios";
import GSignInButton from "vue-google-signin-button";
Vue.use(GSignInButton);

export default {
  name: "google_auth",
  components: {},
  data() {
    return {
      user: {},

      googleSignInParams: {
        client_id:
          "792219114039-6q0r1a9o70k8oco1fa67jq2m1nvv8ka6.apps.googleusercontent.com",
      },
    };
  },
 
  methods: {
    onGoogleSignInSuccess(resp) {
      const token = resp.Zi.access_token;
      axios
        .post("/google/", {
          access_token: token,
        })
        .then((resp) => {
          console.log(resp.data.user);
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    onGoogleSignInError(error) {
      console.log("OH NOES", error);
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
  },
};
</script>
<style lang="scss">
.g-signin-button {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 3px;
  background-color: #3c82f7;
  color: #fff;
  box-shadow: 0 3px 0 #0f69ff;
}
</style>