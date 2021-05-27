<template>
<div class="curveWrap">
      <svg
        width="100%"
        height="100%"
        viewBox="0 0 1200 100"
        xmlns="http://www.w3.org/2000/svg"
      >
        <g class="curve" fill="none">
          <path d="M 0, 60 S 300, -60, 600, 60, 800, -120, 1200 60" />
          <path d="M 0, 60 S 200, -60, 400, 60, 900, -120, 1200 60" />
          <path d="M 0, 60 S 200, -70, 400, 70, 800, -120, 1200 60" />
          <path d="M 0, 60 S 200, -60, 400, 80, 600, -120, 1200 60" />
        </g>
      </svg>
    </div>
</template>
<style lang="scss">
.curveWrap {
	background: #FFF;
	width: 100%;
	height: 200px;
}
.curveWrap .curve {
stroke-linecap: round;
	stroke-opacity: 0.7;
}
.curveWrap .curve path {
	transform-origin: center;
}
.curveWrap .curve path:nth-child(6n + 1) {
	stroke: #3379B7;
}
.curveWrap .curve path:nth-child(6n + 2) {
	stroke: #1B3F5F;
}
.curveWrap .curve path:nth-child(6n + 3) {
	stroke: #67A1D5;
}
.curveWrap .curve path:nth-child(6n + 4) {
	stroke: #BFE2FF;
}
.curveWrap .curve path:nth-child(1) {
	stroke-width: 24;
	animation: curve 35s linear 1.4s infinite;
}
.curveWrap .curve path:nth-child(2) {
	stroke-width: 21;
	animation: curve 35s linear 2.8s infinite;
}
.curveWrap .curve path:nth-child(3) {
	stroke-width: 48;
	animation: curve 35s linear 4.2s infinite;
}
.curveWrap .curve path:nth-child(4) {
	stroke-width: 41;
	animation: curve 35s linear 5.6s infinite;
}

@keyframes curve {
	0% {
		transform: rotateX(0deg) skewY(0deg);
		stroke-opacity: 0.7;
	}
	50% {
		transform: rotateX(360deg) skewY(8deg);
		stroke-opacity: 1;
	}
	100% {
		transform: rotateX(0deg) skewY(0deg);
		stroke-opacity: 0.7;
	}
}
</style>