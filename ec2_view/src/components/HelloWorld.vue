<template>
  <div class="hello">
    <div class="card">
      <div class="card-content">
        <form id="upload-to-db" @submit="addToDynamo">
          Upload new entry into DynamoDB
          <br>
          <p>
            <label for="newGenre">Genre: </label>
            <input id="newGenre" v-model="newGenre" type="text" name="newGenre">
          </p>
          <p>
            <label for="newArtist">Artist: </label>
            <input id="newArtist" v-model="newArtist" type="text" name="newArtist">
          </p>
          <p>
            <label for="newAlbum">Album: </label>
            <input id="newAlbum" v-model="newAlbum" type="text" name="newAlbum">
          </p>
          <p>
            <label for="newSong">Song: </label>
            <input id="newSong" v-model="newSong" type="text" name="newSong">
          </p>
          <p>
            <input type="submit" value="Submit">
          </p>
        </form>
      </div>
    </div>
    <div class="card">
      <div class="card-content">

      </div>
    </div>
    <!-- <div class="card">
      <div class="card-content">
        <div v-for="(albumSongs, artist) in this.data" v-bind:key="artist">
          <Artists :ArtistName="artist" :AlbumSongs="albumSongs"/>
        </div>
      </div>
    </div> -->
  </div>
</template>

<script>
import axios from "axios"
// import Artists from './Artists'

export default {
  name: 'HelloWorld',
  // components: {
  //   Artists
  // },
  data: function() {
    return {
      newGenre: null,
      newArtist: null,
      newAlbum: null,
      newSong: null
    }
  },
  methods: {
    addToDynamo: function() {

      if(!this.newGenre) {
        alert('Genre required.');
      } else if(!this.newArtist) {
        alert('Artist required.');
      } else if(!this.newAlbum) {
        alert('Album required.');
      } else if(!this.newSong) {
        alert('Song required.');
      } else {
        axios
          // .post('http://ec2-54-147-162-97.compute-1.amazonaws.com:3000/uploadNewSong', {
          .post('http://localhost:3000/uploadNewSong', {
            genre: this.newGenre,
            artist: this.newArtist,
            album: this.newAlbum,
            song: this.newSong
          })
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });
      }
    }
  },
  mounted() {
    axios
      // .get('http://ec2-54-83-120-223.compute-1.amazonaws.com:3000/listEverything')
      // .get('http://localhost:3000/genres')
      .get('http://ec2-54-147-162-97.compute-1.amazonaws.com:3000/genres')
      // .get('http://localhost:3000/artists/for/genre?genre=Game%20Music')
      // .get('http://localhost:3000/albums/for/artist?artist=Zelda')
      // .get('http://localhost:3000/songs/for/album?album=OoT')
      // .get('http://localhost:3000/song?song=Hyrule')
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
