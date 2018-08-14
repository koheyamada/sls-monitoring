<template>
  <div class="axios">
  {{ info }}
  </div>
</template>

<script>
export default {
  name: 'Axios',
  data () {
    return {
    }
  },
  mounted ({
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response =. (this.info = response))
    }
  })
}
</script>
