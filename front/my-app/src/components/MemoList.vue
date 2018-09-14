<template>
  <section class="container">
    <h1>Demo examples of vue-chartjs</h1>
    <div class="columns">
      <div class="column">
        <h3>Line Chart</h3>
        <LineChart :chart-data="chartdata" :chart-labels="chartlabels"></LineChart>
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
      chartdata: [200, 100, 300],
      chartlabels: ['1', '2', '3']
    }
  },
  mounted () {
    this.getItems()
  },
  methods: {
    getItems: function () {
      var api = 'https://poa20jco7d.execute-api.ap-northeast-1.amazonaws.com/getItems'
      Vue.axios.get(api).then((response) => {
        this.chartdata = response.data[1]
        this.chartlabels = response.data[0]
        console.log(response.data[0])
        console.log(response.data[1])
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
