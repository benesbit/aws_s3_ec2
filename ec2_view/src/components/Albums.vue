<template>
    <div>
        <p>{{ AlbumName }}</p>
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <div v-for="(elm, index) in SongList" v-bind:key="index">
                    <Songs :SongName="index"/>
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