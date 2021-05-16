<template>
  <div class="v-question-item">
    <div v-for="(question, index) in question_data" :key="question.id">
      <div class="selected" v-if="question.type === 'selected'">
        <p>{{ index + 1 }}.{{ question.text }}</p>
        <div class="m-2">
          <multiselect
            v-model="selectedAnswers[index]"
            placeholder="Search"
            label="value"
            track-by="id"
            :options="question.answers"
            :multiple="true"
            :taggable="true"
            @tag="addTag"
          ></multiselect>
        </div>
      </div>
      <div v-if="question.type === 'checkbox'">
        <p>{{ index + 1 }}. {{ question.text }}</p>

        <b-form-group v-slot="{ ariaDescribedby }">
          <b-form-checkbox-group
            id="checkbox-group-2"
            v-model="selectedAnswers[index]"
            :aria-describedby="ariaDescribedby"
            name="flavour-2"
          >
            <div v-for="val in question.answers" :key="val.id">
              <b-form-checkbox :value="val.value"
                ><p>{{ val.value }}</p></b-form-checkbox
              >
            </div>
          </b-form-checkbox-group>
        </b-form-group>
      </div>
      <div v-if="question.type === 'message'">
        <div class="">
          <p>{{ index + 1 }}. {{ question.text }}</p>

          <b-form-input
            id="input-live"
            v-model="selectedAnswers[index]"
            aria-describedby="input-live-help "
            placeholder="Enter number"
            @keypress="isNumber"
          >
          </b-form-input>
          <b-form-text id="input-live-help">Only numbers are valid</b-form-text>
        </div>
      </div>
      <div v-if="question.type === 'range'">
        <p class="">{{ index + 1 }}. {{ question.text }}</p>
        <vue-slider
          :min="question.answers[0]"
          :max="question.answers[1]"
          v-model="selectedAnswers[index]"
          tooltip="none"
          :min-range="10"
          process="true"
          :marks="true"
          :interval="(question.answers[1] - question.answers[0]) / 10"
        >
          <template v-slot:process="{ style }">
            <div class="vue-slider-process" :style="style">
              <div
                :class="[
                  'merge-tooltip',
                  'vue-slider-dot-tooltip-inner',
                  'vue-slider-dot-tooltip-inner-top',
                ]"
              >
                {{ selectedAnswers[index][0] }} -
                {{ selectedAnswers[index][1] }}
              </div>
            </div>
          </template>
        </vue-slider>

        <br />
      </div>

      <div v-if="question.type === 'switch'">
        <b-row class="w-100 mx-auto">
          <p class="p-0">{{ index + 1 }}. {{ question.text }}</p>
          <b-form-checkbox
            v-model="selectedAnswers[index]"
            name="check-button"
            switch
            class="ml-2"
            size="lg"
          >
          </b-form-checkbox>
        </b-row>
      </div>
      <div v-if="question.type === 'datapicker'">
        <p class="v-question-item__text">{{ question.text }}</p>
        <date-picker
          v-model="selectedAnswers[index]"
          value-type="format"
          format="DD.MM.YYYY"
          range
          placeholder="tip range"
          confirm
          range-separator=" - "
        >
        </date-picker>
      </div>

      <div v-if="question.type === 'textarea'">
        <div class="message">
          <p class="v-question-item__text">{{ question.text }}</p>
          <b-form-textarea
            id="textarea-state"
            v-model="selectedAnswers[index]"
            :state="selectedAnswers[index].length > 2"
            placeholder="Enter at least 10 characters"
            rows="3"
          >
          </b-form-textarea>
        </div>
      </div>
    </div>
    <div>
      Selected: <strong>{{ selectedAnswers }}</strong>
    </div>
  </div>
</template>

<script>
import VueSlider from "vue-slider-component";
import "vue-slider-component/theme/default.css";
import Multiselect from "vue-multiselect";
import DatePicker from "vue2-datepicker";
import "vue2-datepicker/index.css";
//import PrettyCheckbox from 'pretty-checkbox-vue';
import "vue-slider-component/theme/default.css";
// import 'pretty-checkbox/src/pretty-checkbox.scss';

export default {
  name: "v-question-item",
  components: {
    VueSlider,
    Multiselect,
    DatePicker,
    //PrettyCheckbox
  },

  props: {
    question_data: {
      type: Array,
      default() {
        return {};
      },
    },
    questions_len: {
      type: Number,
    },
    selectedAnswers2: {
      type: Array,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      activeStep: 0,
      value: [0, 50],
      // process: (value) => [[value[0], value[1]]],
      selectedAnswers: this.selectedAnswers2,
    };
  },

  methods: {
    isNumber(e) {
      const regex = /[0-9]/;
      if (!regex.test(e.key)) {
        e.returnValue = false;
        if (e.preventDefault) e.preventDefault();
      }
    },
    // rangeSelect(index) {
    //   (value) => [[value[0], value[1]]];

    //   console.log(index);
    //   this.selectedAnswers[index] = this.value.map((car) => car);
    // },
    sendAnswers() {
      let v = [];
      for (let i = 0; i < this.selectedAnswers.length; i++) {
        if (
          this.question_data[i].type == "selected" ||
          this.question_data[i].type == "range" ||
          this.question_data[i].type == "datapicker"
        ) {
          v[i] = {
            id: this.question_data[i].id,
            type: this.question_data[i].type,
            answers: this.selectedAnswers[i],
          };
        } else if (this.question_data[i].type == "checkbox") {
          v[i] = {
            id: this.question_data[i].id,
            type: this.question_data[i].type,
            answers: [],
          };
          for (let j = 0; j < this.question_data[i].answers.length; j++) {
            if (
              this.question_data[i].answers[j].value ==
              this.selectedAnswers[i]
            ) {
              v[i].answers.push({
                id: this.question_data[i].answers[j].id,
                value: this.selectedAnswers[i],
              });
              break;
            }
          }
        } else {
          v[i] = {
            id: this.question_data[i].id,
            type: this.question_data[i].type,
            answers: [this.selectedAnswers[i]],
          };
        }
      }
      return v;
    },
    addTag(newTag) {
      const tag = {
        value: newTag,
        id: newTag.substring(0, 2) + Math.floor(Math.random() * 10000000),
      };
      this.question_data.push(tag);
      this.value.push(tag);
    },
    done() {
      this.$emit("send-answer", this.selectedAnswers, this.questions_len);
      // this.activeStep = this.questions_len;
      this.selectedAnswers = "";
    },
  },
};
</script>
<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style lang="scss">
@import "../assets/styles/base.scss";

.actions {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0 auto;
  button {
    width: 200px;
    margin: 5% 10% 5% 10%;
    padding: 5px 20px;
    display: inline;
    justify-content: space-between;
  }
}
.multiselect {
  width: 550px;
}

.multiselect__input::placeholder {
  color: #274c77;
}
.multiselect__placeholder {
  color: #274c77;
  border-radius: 0px;
}

.multiselect__content-wrapper {
  position: absolute;
  display: block;
  background: #a3cef1;
  color: #274c77;
  width: 550px;
  max-height: 240px;
  overflow: auto;
  border-top: none;
  border-bottom-left-radius: 0px;
  border-bottom-right-radius: 0px;
  z-index: 50;
  -webkit-overflow-scrolling: touch;
}
.multiselect__tag {
  position: relative;
  display: inline-block;

  background: #274c77;
  white-space: nowrap;
  overflow: hidden;
  max-width: 100%;
  text-overflow: ellipsis;
}
.multiselect__tag-icon:after {
  content: "×";
  color: #ffd037;
  font-size: 220%;
}
.multiselect__tag-icon:focus,
.multiselect__tag-icon:hover {
  background: none;
}
.multiselect__option--highlight {
  background: $blu;
  color: white;
}
.multiselect__option--highlight:after {
  content: attr(data-select);
  background: $ylw;
}

.merge-tooltip {
  position: absolute;
  left: 50%;
  bottom: 100%;
  transform: translate(-50%, -15px);
}

.vue-slider {
  padding: 17px 20px;
}

.vue-slider-marks {
  color: $blu;
}
.p-icon {
  align-items: center;
  columns: 60px 4;
  column-gap: 30px;
  margin: 0 auto;
}
.pretty.p-icon .state .icon {
  background-color: $blu;
}

.mx-datepicker-range {
  width: 550px;
}

.merge-tooltip {
  position: absolute;
  left: 50%;
  bottom: 100%;
  transform: translate(-50%, -15px);
}
</style>