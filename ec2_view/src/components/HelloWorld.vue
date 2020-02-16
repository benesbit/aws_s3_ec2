<template>
  <div class="hello">
    <div class="card">
      <div class="card-content">
        <!-- <div class="columns">
          <div class="column is-4 is-offset-4"> -->
            <div v-for="(elm, index) in this.data" v-bind:key="index">
              <Artists :ArtistName="index" :AlbumSongs="elm"/>
            </div>
          <!-- </div>
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios"
import Artists from './Artists'

export default {
  name: 'HelloWorld',
  components: {
    Artists
  },
  data() {
    return {
      data: {}
    }
  },
  mounted() {
    axios
      .get('http://localhost:3000/shit')
      .then(response => {
        console.log(response.data);
        this.data = response.data;
      });
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
