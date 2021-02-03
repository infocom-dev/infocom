<template>

    <div class= 'v-question-item'>
      <div clsass="selected" v-if="question_data.type === 'selected' ">
        <p class="v-question-item__text">{{question_data.text}} </p>
          <div>
           <multiselect v-model="selectedAnswers" tag-placeholder="Add this as new tag" placeholder="Search" label="value" track-by="id" :options="question_data.answers" :multiple="true" :taggable="true" @tag="addTag"></multiselect>
          </div>
      </div>

      <div v-if="question_data.type === 'checkbox' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <label v-for="val in question_data.answers" :key="val.id">
          <p-check class="p-icon p-round p-pulse" color="success">
             <i slot="extra" class="icon mdi mdi-check"></i>
               {{val.value}}
          </p-check>
        </label>
       </div>

      <div v-if="question_data.type === 'message' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <input v-model="selectedAnswers" placeholder="Type here">
        <p>Answer: {{ selectedAnswers }}</p>
      </div>

      <div v-if="question_data.type === 'range' ">
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <vue-slider :min="question_data.answers[0]"
                    :max="question_data.answers[1]"
                    :interval="10"
                    v-model="value"
                    :marks="marks"
                    :tooltip="'none'"
                    :process="process"
                    :process-style="{ backgroundColor: 'blue' }"
                    :tooltip-style="{ backgroundColor: 'blue', borderColor: 'blue' }"
        >
          <div :class="['custom-dot', { focus }]"></div>
            <template v-slot:step="{ label, active }">
              <div :class="['custom-step', { active }]"></div>
            </template>
          <template v-slot:process="{ start, end, style, index }">
            <div class="vue-slider-process" :style="style">
              <div :class="[
                'merge-tooltip',
                'vue-slider-dot-tooltip-inner',
                'vue-slider-dot-tooltip-inner-top',
              ]">
               {{ value[index] }} - {{ value[index + 1] }}
              </div>
            </div>
          </template>
        </vue-slider>
        <br>
        <div class="set-range">
         <input type="text" v-model="value[0]" placeholder="От" class="form-control" /><br>
         <input type="text" v-model="value[1]" placeholder="До" class="form-control" /><br>
        </div>
      </div>
      <div v-if="question_data.type === 'switch' " >
          <p-check class="p-switch" color="primary">{{question_data.text}}</p-check>
      </div>
      <div v-if="question_data.type === 'datapicker' " >
        <p class="v-catalog-item__text">{{question_data.id}}.{{question_data.text}} </p>
        <date-picker  v-model="selectedAnswers"
                      value-type="format"
                      format="DD.MM.YYYY"
                      range
                      placeholder="tip range"
                      confirm
                      range-separator=" - "
                      >
        </date-picker>
>
      </div>
   
      
    </div>
</template>

<script>

 import VueSlider from 'vue-slider-component'
 import 'vue-slider-component/theme/default.css'
 import Multiselect from 'vue-multiselect'
 import DatePicker from 'vue2-datepicker';
 import 'vue2-datepicker/index.css';




export default {
  name: 'v-question-item',
  components: {
     VueSlider,
     Multiselect,
     DatePicker,

  },
  props:{
        question_data:{
            type:Object,
            default(){
                return{}
            }
        }
    },
  data(){ 
    return {
      activeStep: 0,
      animation: 'animate-in',
      value:[0,50],
      marks: val =>  val % ((this.question_data.answers[1]-this.question_data.answers[0]) /10) === 0,
      selectedAnswers:""
    }
  },
  methods: {
    addTag (newTag) {
      const tag = {
        value: newTag,
        id: newTag.substring(0, 2) + Math.floor((Math.random() * 10000000))
      }
      this.question_data.push(tag)
      this.value.push(tag)
    }
  }
} 
    
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss">


.v-question-item__text{
  color:white;
  text-align: center;
  font-weight: normal;

}

.multiselect{
  //box-sizing: content-box;
  width: 550px;
  margin:0 auto;
   /* Ширина блока */
  //padding: 10px; /* Поля */
  //margin-top: 5px; /* Отступ сверху */
  //-moz-box-sizing: border-box; /* Для Firefox */  
}

.multiselect__input::placeholder {
    color : #555;
    
}
.multiselect__placeholder {
  color : red;
  border-radius: 0px;
}

.multiselect__content-wrapper {
  position: absolute;
  display: block;
  background: #ccc ;
  color:black;
  //transition: 1000ms;
  width: 550px;
  max-height: 240px;
  overflow: auto;
  //border:  blue solid ;
  border-top: none;
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
  z-index: 50;
  -webkit-overflow-scrolling: touch;
}
.multiselect__tag {
    position      : relative;
    display       : inline-block;
    border-radius : px;
    background    : black;
    white-space   : nowrap;
    overflow      : hidden;
    max-width     : 100%;
    text-overflow : ellipsis;
}
.multiselect__tag-icon:after {
    content   : "×";
    color     : red;
    font-size : 220%;
}
.multiselect__tag-icon:focus,
.multiselect__tag-icon:hover {
    background : none;

}
.multiselect__option--highlight {
    background : #555;
    color      : white;
}
.multiselect__option--highlight:after {
    content    : attr(data-select);
    background : black;
}




.set-range {
        flex: 0 0 auto;

        display: flex;

        padding: 20px;

        input {
          width: 100%;
          padding: (20px / 2) 20px;
          border: 2px solid rgb(100, 100, 100);
          border-radius: 5px;
          transition: border-color .2s ease-out;

          &:hover, &:focus {
            border-color: rgb(30, 30, 30);
          }
        }
      }
.merge-tooltip {
      position: absolute;
      left: 50%;
      bottom: 100%;
      transform: translate(-50%, -15px);
    }
.custom-step {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    box-shadow: 0 0 0 3px #ccc;
    background-color: #fff;
  }
  .custom-step.active {
    box-shadow: 0 0 0 3px #3498db;
    background-color: #3498db;
  }
 .custom-dot {
    width: 100%;
    height: 100%;
    border-radius: 0;
    //background-color: rgb(49, 4, 194);
    transition: all .3s;
  }
  .custom-dot.focus {
    border-radius: 25%;
  }
</style>