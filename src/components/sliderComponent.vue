<template>
    <div id = 'sliderComponent'> 
        <input
            type='range'
            :min='min'
            :max='max'
            :value='input'
            @change='emitInput'
            :class='["slider-component", shapeClass]'
            :style='sliderStyles'
        />
    </div>
</template>

<script>
export default {
    props: {
        value: {
            type: Number,
            required: true
        },
        min: {
            type: Number,
            default: 1
        },
        max: {
            type: Number,
            default: 100
        },
        rounded: {
            type: Boolean,
            default: false
        },
        slideSize: {
            type: String,
            default: '10px'
        },
        slideColor: {
            type: String,
            default: '#ccc'
        },
        controlSize: {
            type: String,
            default: '16px'
        },
        controlColor: {
            type: String,
            default: '#444'
        }
    },
    data () {
        return {
            input: this.value
        }
    },
    methods: {
        emitInput (event) {
            this.input = event.target.value
            this.$emit('input', this.input)
        }
    },
    computed: {
        shapeClass () {
            return this.rounded ? 'round' : ''
        },
        sliderStyles () {
            return '--slider-slide-size:' +  this.slideSize + ';' +
                    '--slider-slide-color:' + this.slideColor + ';' +
                    '--slider-control-size:' + this.controlSize + ';' +
                    '--slider-control-color:'+ this.controlColor + ';'
        }
    },
    watch: {
        value (v) {
            this.input = v
        }
    }
}
</script>

<style lang='scss' scoped>
.slider-component {
    appearance: none;
    width: 100%;
    height: var(--slider-slide-size);
    background: var(--slider-slide-color);
    outline: none;
    &::-webkit-slider-thumb {
        appearance: none;
        width: var(--slider-control-size);
        height: var(--slider-control-size);
        background: var(--slider-control-color);
        cursor: pointer;
    }
    &.round {
        border-radius: 5px;
        &::-webkit-slider-thumb {
            border-radius: 50%;
        }
    }
}
</style>