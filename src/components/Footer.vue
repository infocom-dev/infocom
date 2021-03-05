<template>
  <div class="Footer">
    <footer>
      <b-container class="pt-3 mb-0">
        <div class="mx-auto">
          <b-row align-v="center" class="justify-content-center">
            <div class="col-4 text-left">
              <h1 class="text-uppercase font-weight-bolder">
                INFO<span>com</span>
              </h1>
            </div>
            <div class="col-4 text-center">
              <p>
                © Copyright 2014 - 2015, All Rights Reserved, Designed by:
                www.designoatmeal.com
              </p>
            </div>
            <div class="col-4 text-right">
              <a href=""><i class="fab fa-facebook facebook-icon"></i></a>
              <a href=""><i class="fab fa-twitter twitter-icon"></i></a>
              <a href=""><i class="fab fa-instagram insta-icon"></i></a>
              <a href=""><i class="fab fa-google-plus google-icon"></i></a>
            </div>
          </b-row>
        </div>
      </b-container>
    </footer>
  </div>
</template>
<style lang="scss">
@import "../assets/styles/base.scss";
.Footer {
  background-color: $blu;
  .insta-icon,
  .vk-icon,
  .mail-icon,
  .twitter-icon,
  .facebook-icon,
  .google-icon {
    font-size: 70px;
    color: $ylw;
    line-height: 50px;
    padding: 10px;
    &:hover {
      color: $rs;
    }
  }
  span,
  p {
    color: white;
  }
}
</style>
