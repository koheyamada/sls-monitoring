<template>
  <b-container fluid>
    <b-row>
      <b-col md="6" class="my-1">
        <b-form-group horizontal label="Filter" class="mb-0">
          <b-input-group>
            <b-form-input v-model="filter" placeholder="Type to Search" />
            <b-input-group-append>
              <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>
      <b-col md="6" class="my-1">
        <b-form-group horizontal label="Per page" class="mb-0">
          <b-form-select :options="pageOptions" v-model="perPage" />
        </b-form-group>
      </b-col>
    </b-row>

    <b-table show-empty stacked="md" :items="items" :fields="fields" :current-page="currentPage" :per-page="perPage" :filter="filter">
      <template slot="name" slot-scope="row">{{row.value}}</template>
    </b-table>
    <b-row>
      <b-col md="6" class="my-1">
        <b-pagination :per-page="perPage" v-model="currentPage" class="my-0" />
      </b-col>
    </b-row>
    <div class="mt-4">currentPage: {{currentPage}}</div>
  </b-container>
</template>

<script>
export default {
  name: 'Table',
  props: ['items', 'fields'],
  data () {
    return {
      currentPage: 1,
      perPage: 3,
      pageOptions: [ 3, 5, 10 ],
      filter: null
    }
  }
}
</script>
