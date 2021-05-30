<template>
  <div class="load">
    <div class="content ">
      <div class="loading ">
        <p class='text-center'>loading</p>
        <span></span>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Graph",
  data: () => ({}),
  props: {
    options: {
      type: Object,
      default() {
        return {};
      },
    },
    series: [],
    width: Number,
  },
};
</script>
<style lang='scss'>


@import url("https://fonts.googleapis.com/css?family=Oxygen:700&display=swap");

body {
   margin: 0;
}

$bg: white;
$c-01: #274C77;
$c-02: #FFD037;

$font-01: "Oxygen", sans-serif;
.load{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%); 
}
.content {
   display: flex;
   justify-content: center;
   align-items: center;
   .loading {
      width: 200px;
      height: 50px;
      position: relative;
      p {
         top: 0;
         padding: 0;
         margin: 0;
         color: $c-01;
         font-family: $font-01;
         animation: text 3.5s ease both infinite;
         font-size: 12px;
         letter-spacing: 1px;
      }
      span {
         background-color: $c-01;
         border-radius: 50px;
         display: block;
         height: 16px;
         width: 16px;
         bottom: 0;
         position: absolute;
         transform: translateX(64px);
         animation: loading 3.5s ease both infinite;

         &:before {
            position: absolute;
            content: "";
            width: 100%;
            height: 100%;
            background-color: $c-02;
            border-radius: inherit;
            animation: loading2 3.5s ease both infinite;
         }

         @keyframes loading {
            0% {
               width: 16px;
               transform: translateX(0px);
            }

            40% {
               width: 100%;
               transform: translateX(0px);
            }

            80% {
               width: 16px;
               transform: translateX(64px);
            } 

            90% {
               width: 100%;
               transform: translateX(0px);
            }

            100% {
               width: 16px;
               transform: translateX(0px);
            }
         }
         @keyframes loading2 {
            0% {
               transform: translateX(0px);
               width: 16px;
            }

            40% {
               transform: translateX(0%);
               width: 80%;
            }

           80% {
               width: 100%;
               transform: translateX(0px);
            }

            90% {
               width: 80%;
            transform: translateX(15px);
            }
            100% {
               transform: translateX(0px);
               width: 16px;
            }
         }
      }
   }
}
</style>


