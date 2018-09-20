<template>
  <section class="container">
    <h1>Demo examples of vue-chartjs</h1>
    <button @click="getItems">Button</button>
    <div class="columns">
      <div class="column">
        <h3>Line Chart</h3>
        <LineChart v-if="loaded" :chart-data="chartdata" :chart-labels="chartlabels"></LineChart>
      </div>
      <div class="column">
        <h3>Bar Chart</h3>
      </div>
    </div>
    <div class="columns">
      <div class="column">
        <h3>Bubble Chart</h3>
      </div>
      <div class="column">
        <h3>Reactivity - Live update upon change in datasets</h3>
      </div>
    </div>
  </section>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import LineChart from '@/components/LineChart'

Vue.use(VueAxios, axios)

export default {
  name: 'VueChartJS',
  components: {
    LineChart
  },
  data () {
    return {
      loaded: false,
      chartdata: [],
      chartlabels: []
    }
  },
  mounted () {
    this.getItems()
  },
  methods: {
    resetState () {
      this.loaded = false
    },
    getItems () {
      this.resetState()
      var _ENDPOINT_ = 'https://poa20jco7d.execute-api.ap-northeast-1.amazonaws.com/getItems'
      Vue.axios.get(_ENDPOINT_).then(response => {
        this.chartdata = response.data.Items.map(Items => Items.scode)
        this.chartlabels = response.data.Items.map(Items => Items.date)
        this.loaded = true
        console.log(this.chartdata)
        console.log(this.chartlabels)
      })
    }
  }
}
</script>

<style scoped>
  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
