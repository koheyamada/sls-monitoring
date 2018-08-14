<template>
  <div>
    <p class="title">{{ title }}</p>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      title: 'This is Header component'
    }
  }
}
</script>

<style>
.title {
  font-size: 20px;
  font-weight: bold;
}
</style>
