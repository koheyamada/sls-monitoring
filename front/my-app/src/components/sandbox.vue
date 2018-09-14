<template>
  <div class="axios">
    <h1>{{ title }}</h1>
    <button v-on:click="test">クリック</button>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

export default {
  name: 'Sandbox',
  data () {
    return {
      title: 'Sandbox',
      fields: [
        { key: 'id', sortable: false },
        { key: 'name', sortable: true },
        { key: 'slack', sortable: true }
      ]
    }
  }
}
</script>
