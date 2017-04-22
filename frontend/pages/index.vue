<template>
  <div class="container">
    <h2>Github trendings</h2>
    <ul class="trendings">
      <li v-for="trending in trendings">
        <nuxt-link :to="'/trendings/'+trending.id">{{ trending.name }}</nuxt-link>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  asyncData () {
    return axios.get('http://localhost:5000/trendings')
    .then((res) => {
      console.log(res.data)
      return { trendings: res.data }
    })
  }
}
</script>

<style scoped>
.container {
  text-align: center;
  margin-top: 100px;
  font-family: sans-serif;
}
.trendings {
  list-style-type: none;
}
.trendings li a {
  display: inline-block;
  width: 200px;
  border: 1px #ddd solid;
  padding: 10px;
  text-align: left;
  color: #222;
  text-decoration: none;
}
.trendings li a:hover {
  color: orange;
}
</style>