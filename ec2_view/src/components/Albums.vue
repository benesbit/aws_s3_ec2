<template>
    <div class="Album">
        <div class="card">
            <div class="card-content">
                <p>Album: {{ AlbumName }}</p>
                <div v-for="(elm, index) in SongList" v-bind:key="index">
                    <Songs :SongName="index"/>
                    <audio controls>
                        <source v-bind:src="elm" type="audio/mpeg">
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