<template>
  <div class="trendings">
    <h3>{{ name }}</h3>
    <p><nuxt-link to="/">List of trendings</nuxt-link></p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  validate ({ params }) {
    return !isNaN(+params.id)
  },
  asyncData ({ params, error }) {
    return axios.get(`http://localhost:8000/trendings/${params.id}`)
    .then((res) => res.data)
    .catch(() => {
      error({ message: 'Page not found', statusCode: 404 })
    })
  }
}
</script>

<style scoped>
.trendings {
  text-align: center;
  margin-top: 100px;
  font-family: sans-serif;
}
</style>