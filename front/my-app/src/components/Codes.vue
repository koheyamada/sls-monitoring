<template>
  <div class="axios">
    <h1>{{ title }}</h1>
    <user-list v-bind:items="results" v-bind:fields="fields" />
  </div>
</template>

<script>
import Table from '@/components/Table'
import Registration from '@/components/Registration'
import axios from 'axios'

export default {
  name: 'List',
  components: {
    'user-list': Table,
    'user-regist': Registration
  },
  data () {
    return {
      title: 'Codes',
      fields: [
        { key: 'id', sortable: false },
        { key: 'name', sortable: true },
        { key: 'url', sortable: true },
        { key: 'date', sortable: true },
        { key: 'scode', sortable: true }
      ],
      results: [],
      endpoint: 'https://qxdt0mc8hj.execute-api.ap-northeast-1.amazonaws.com/prod/getitems',
      table: 'S-Status'
    }
  },
  mounted () {
    this.getList()
  },
  methods: {
    getList () {
      axios
        .get(this.endpoint + '?table=' + this.table)
        .then(response => { this.results = response.data })
    }
  }
}
</script>
