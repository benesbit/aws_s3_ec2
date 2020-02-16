<template>
    <div>
        <p>{{ AlbumName }}</p>
        <div class="columns">
            <div class="column is-4 is-offset-4">
                <div v-for="(elm, index) in Songs" v-bind:key="index">
                    <!-- <Albums :AlbumName="index" :Songs="elm"/> -->
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['AlbumName',
            'Songs']
}
</script>

<style>

</style>