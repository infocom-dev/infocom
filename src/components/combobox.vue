<template>
<div>
    <div class="combobox" role="combobox" aria-haspopup="listbox" aria-owns="combobox-results" :aria-expanded="isOpen">
      <input type="text"
        v-model="search"
        @click.stop="onClick"
        @input="onChange"
        @keyup.down="onArrowDown"
        @keyup.up="onArrowUp"
        @keyup.enter="onEnter"
        aria-autocomplete="list"
        aria-controls="combobox-results"
        :aria-activedescendant="activedescendant"
        :aria-labelledby="ariaLabelledBy"
        :placeholder="placeholder"
      />
      <i role="button" aria-label="הצג-אפשרויות" class="open-indicator" :class="{'open':isOpen}"></i>
      <div class="results-menu-border-filler" aria-hidden="true" v-show="isOpen"></div>
    </div>

    <ul id="combobox-results" v-show="isOpen" class="combobox-results" role="listbox">
      <li class="loading" v-if="isLoading">
        Loading results...
      </li>
      <li v-else v-for="(result, i) in results" :key="i"
        @click.stop="setResult(result)"
        class="combobox-result"
        :class="{ 'is-active': isSelected(i) }"
        role="option"
        :id="getId(i)"
        :aria-selected="isSelected(i)">
        {{ result }}
      </li>
    </ul>
</div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      required: false,
      default: () => []
    },
    isAsync: {
      type: Boolean,
      required: false,
      default: false
    },
    ariaLabelledBy: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      required: false,
      default: ''
    }
  },
  data() {
    return {
      isOpen: false,
      results: [],
      search: '',
      isLoading: false,
      arrowCounter: -1,
      activedescendant: '',
    }
  },
  methods: {
    onClick() {
      console.log('onClick');
      this.filterResults();
      this.isOpen = true;
    },
    onChange() {
      console.log('onChange');
      this.$emit('input', this.search);
      this.filterResults();
      this.isOpen = true;
    },
    onBlur() {
      console.log('onBlur');
      this.isOpen = false;
    },
    filterResults() {
      console.log('filterResults');
      if(this.search.length > 0) {
        this.results = this.items.filter(item => {
          return item.toLowerCase().indexOf(this.search.toLowerCase()) > -1;
        });
      } else if (this.search.length === 0) {
        this.results = this.items
      }
    },
    setResult(result) {
      console.log('setResult');
      this.search = result;
      this.isOpen = false;
    },
    onArrowDown(evt) {
      if (this.arrowCounter < this.results.length) {
        this.arrowCounter = this.arrowCounter + 1;
        this.setActiveItem();
      }
    },
    onArrowUp() {
      if (this.arrowCounter > 0) {
        this.arrowCounter = this.arrowCounter - 1;
        this.setActiveItem();
      }
    },
    onEnter() {
      this.search = this.results[this.arrowCounter];
      this.isOpen = false;
      this.arrowCounter = -1;
    },
    handleClickOutside(evt) {
      console.log('handleClickOutside');
      if (!this.$el.contains(evt.target)) {
        this.isOpen = false;
        this.arrowCounter = -1;
        this.activedescendant = '';
      }
    },
    setActiveItem() {
      this.activedescendant = this.getId(this.arrowCounter);
    },
    isSelected(index) {
      return index === this.arrowCounter;
    },
    getId(index) {
      return `result-option-${index}`;
    }
  },
  watch: {
    items: function (val, oldValue) {
      if (val.length !== oldValue.length) {
        this.results = val;
        this.isLoading = false;
      }
    }
  },
  mounted() {
    document.addEventListener('click', this.handleClickOutside);
  },
  destroyed() {
    document.removeEventListener('click', this.handleClickOutside);
  }
}
</script>

<style lang="scss">
@import "../scss/fonts.css";
	.combobox {
    align-items: center;
    box-sizing: border-box;
    color: rgb(91, 98, 101);
    cursor: pointer;
    direction: rtl;
    display: flex;
    height: 40px;
    padding: 0;
    width: 258px;
    position: relative;
  }
  
  input {
    border: 1px solid rgba(60, 60, 60, 0.26);
    border-radius: 3px;
    box-shadow: none;
    box-sizing: border-box;
    color: #5b6265;
    direction: rtl;
    font-family: 'Open Sans Hebrew';
    font-size: 16px;
    font-weight: 400;
    margin: 0;
    line-height: 22px;
    height: 40px;
    padding: 0 16px 0 45px;
    outline: none;
    max-width: 100%;
    position: relative;
    text-align: start;
    width: 258px;
    &.hide-caret {
      color: transparent;
      text-shadow: 0 0 0 #5b6265;
    }
    &:focus {
      box-shadow: 0 0 2px 1px #76aaea;
      border: 1px solid #66afe9;
    }
  }
  .open-indicator {
    position: absolute;
    transform: translateY(-50%);
    top: 50%;
    left: 16px;
    width: 16px;
    height: 12px;
    background-repeat: no-repeat;
    
    &.open {
      transform: rotate(180deg) translateY(50%)
    }
  }
	.combobox-results {
    direction: rtl;
		padding: 0;
		margin: 1px 0 0;
    border: 1px solid rgba(60, 60, 60, 0.26);
    border-top: none;
    border-radius: 0 0 4px 4px;
    height: 137px;
    width: 256px;
    overflow-y: scroll;
    overflow-x: hidden;
    position: relative;
    background: #fff;
  }
  .results-menu-border-filler {
    display: block;
    position: absolute;
    border-left: 1px solid rgba(60, 60, 60, 0.26); 
    border-right: 1px solid rgba(60, 60, 60, 0.26);
    height: 2px;
    width: 256px;
    background: transparent;
    bottom: -1px;
    z-index: 100;
    pointer-events: none;
  }
	.combobox-result {
		list-style: none;
		text-align: left;
		padding: 3px 12px;
    cursor: pointer;
    color: #5b6265;
    line-height: 28px;   
    text-align: right;
    font-family: 'Open Sans Hebrew';
	}
	.combobox-result.is-active,
	.combobox-result:hover {
		background-color: #ebebeb;
	}
</style>