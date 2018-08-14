<template>
  <div class="axios">
    <h1>{{ title }}</h1>
    <table>
      <tr>
        <th>name</th>
        <th><input class="input" v-model="name" placeholder="名前を入力してください" /></th>
      </tr>
      <tr>
        <th>slack</th>
        <th><input class="input" v-model="slack" placeholder="slack通知先を入力してください" /></th>
        <th><input type="button" value="click" v-on:click="putItems" /></th>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'List',
  data () {
    return {
      title: 'UserList',
      name: '',
      slack: ''
    }
  },
  methods: {
    putItems () {
      var _API_ENDPOINT_ = 'https://gxni4w9ak1.execute-api.ap-northeast-1.amazonaws.com/putItems/'
      var data = {
        'name': this.name,
        'slack': this.slack
      }

      axios.put(_API_ENDPOINT_, data).then(result => {
        console.log(result)
      }).catch(err => {
        this.errorMessage = err.response.data.error
        this.showError = true
      })
    }
  }
}
</script>
