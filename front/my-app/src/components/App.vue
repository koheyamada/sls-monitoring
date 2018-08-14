<templage>
  <div>
    <header-component></header-component>
    <p class="blue">This is App component.</p>
  </p>
</template>

<script>
import Header from './Header.vue';

export default {
  components: {
    'header-component': Header
  }
}
</script>

<style>
.blue {
  color: blue;
}
</style>
