<template>
    <div>
        <p>{{ ArtistName }}</p>
        <div class="columns">
            <div class="column is-4 is-offset-4">
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