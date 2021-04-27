<template>
  <div class="Footer">
    <!-- <footer> -->
      <b-container fluid class="pt-5 mb-0 w-100 ">
        <div class=" pt-3">
          <b-row align-v="center" class="justify-content-center pt-5 mx-5">
            <div class="col ">
              <h1 class="text-uppercase font-weight-bolder">
                INFO<span>com</span>
              </h1>
            </div>
            <div class="col text-center">
              <p>
                © Copyright 2014 - 2015, All Rights Reserved, Designed by:
                www.designoatmeal.com
              </p>
            </div>
            <div class="col text-right">
              <a href=""><i class="fab fa-facebook facebook-icon"></i></a>
              <a href=""><i class="fab fa-twitter twitter-icon"></i></a>
              <a href=""><i class="fab fa-instagram insta-icon"></i></a>
              <a href=""><i class="fab fa-google-plus google-icon"></i></a>
            </div>
          </b-row>
        </div>
      </b-container>
    <!-- </footer> -->
  </div>
</template>
<style lang="scss">
@import "../assets/styles/base.scss";
.Footer {
  background: url('../assets/images/footer.jpg') no-repeat;
  // height: 200px;
  background-size: cover;
  .insta-icon,
  .vk-icon,
  .mail-icon,
  .twitter-icon,
  .facebook-icon,
  .google-icon {
    font-size: 50px;
    color: $ylw;
    line-height: 50px;
    padding: 10px;
    &:hover {
      color: $rs;
    }
  }
  span {
    color: white;
  }
}
</style>
