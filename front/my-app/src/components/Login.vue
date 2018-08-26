<template>
<div class="login">
  <h1 class="msg">Login</h1>
  <b-container>
    <b-input-group prepend="name">
      <b-form-input v-model="name" placeholder="入力してください"></b-form-input>
    </b-input-group>
    <b-input-group prepend="mail">
      <b-form-input v-model="mail" placeholder="入力してください"></b-form-input>
    </b-input-group>
    <b-btn text="Button" variant="outline-secondary" v-on:click="login">Login</b-btn>
  </b-container>
</div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      name: '',
      mail: '',
      passwd: ''
    }
  },
  methods: {
    login: function (event) {
      alert('Hello' + this.name + '!')
    }
  }
}
</script>
