<template>
  <div class="container">
    <h2>Github trendings</h2>
    <ul class="trendings">
      <li v-for="trending in trendings">
        <a :href="trending.url" target="_blank">{{ trending.name }}</a>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  asyncData () {
    return axios.get('http://localhost:5000/trendings?lang=python&count=5')
    .then((res) => {
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