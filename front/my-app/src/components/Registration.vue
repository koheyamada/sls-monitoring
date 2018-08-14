<template>
  <div class="axios">
  <b-container>
    <b-input-group prepend="name">
      <b-form-input v-model="name" placeholder="入力してください"></b-form-input>
    </b-input-group>
    <b-input-group prepend="slack">
      <b-form-input v-model="slack" placeholder="入力してください"></b-form-input>
    </b-input-group>
    <b-btn text="Button" variant="outline-secondary" v-on:click="putItems">Resist</b-btn>
  </b-container>
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
