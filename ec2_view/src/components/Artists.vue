<template>
    <div class="Artist">
        <div class="card">
            <div class="card-content">
               <p>Artist: {{ ArtistName }}</p>
                <div v-for="(elm, index) in AlbumSongs" v-bind:key="index">
                    <Albums :AlbumName="index" :SongList="elm"/>
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