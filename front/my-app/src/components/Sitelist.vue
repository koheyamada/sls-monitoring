<template>
  <LineChart v-if="loaded" :chart-data="chartdata" :chart-labels="chartlabels"></LineChart>
</template>

<script>
import LineChart from './LineChart'
</script>
