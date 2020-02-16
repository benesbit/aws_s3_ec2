<template>
    <div class="Album">
        <div class="card">
            <div class="card-content">
                <p>Album: {{ AlbumName }}</p>
                <div v-for="(songURL, song) in SongList" v-bind:key="song">
                    <Songs :SongName="song"/>
                    <audio controls>
                        <source v-bind:src="songURL" type="audio/mpeg">
                    </audio>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Songs from './Songs'

export default {
    components: {
        Songs
    },
    props: ['AlbumName',
            'SongList']
}
</script>

<style>

</style>