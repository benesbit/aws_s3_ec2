<template>
  <div class="hello">
    <div class="card">
      <div class="card-content">
        <form id="upload-to-db">
          Upload new entry into DynamoDB
          <br>
          <p>
            <label for="genre">Genre: </label>
            <input id="genre" v-model="genre" type="text" name="genre">
          </p>
          <p>
            <label for="artist">Artist: </label>
            <input id="artist" v-model="artist" type="text" name="artist">
          </p>
          <p>
            <label for="album">Album: </label>
            <input id="album" v-model="album" type="text" name="album">
          </p>
          <p>
            <label for="song">Song: </label>
            <input id="song" v-model="song" type="text" name="song">
          </p>
          <p>
            <input type="submit" value="Submit">
          </p>
        </form>
      </div>
    </div>
    <div class="card">
      <div class="card-content">
        <div v-for="(albumSongs, artist) in this.data" v-bind:key="artist">
          <Artists :ArtistName="artist" :AlbumSongs="albumSongs"/>
        </div>
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
      // .get('http://ec2-54-83-120-223.compute-1.amazonaws.com:3000/listEverything')
      // .get('http://localhost:3000/genres')
      // .get('http://localhost:3000/artists/for/genre?genre=Game%20Music')
      // .get('http://localhost:3000/albums/for/artist?artist=Zelda')
      // .get('http://localhost:3000/songs/for/album?album=OoT')
      .get('http://localhost:3000/song?song=Hyrule')
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
