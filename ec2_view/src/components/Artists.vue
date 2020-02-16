<template>
    <div class="Artist">
        <div class="card">
            <div class="card-content">
               <p>Artist: {{ ArtistName }}</p>
                <div v-for="(listOfSongs, album) in AlbumSongs" v-bind:key="album">
                    <Albums :AlbumName="album" :SongList="listOfSongs"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Albums from './Albums'

export default {
    components: {
        Albums
    },
    props: ['ArtistName',
            'AlbumSongs']
}
</script>

<style>

</style>