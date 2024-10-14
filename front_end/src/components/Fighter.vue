<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios';

const props = defineProps({
    fighter: Object,
    selectedFighter: Object
})

const emit = defineEmits(['fighter-deleted'])

const fighterPictureURL = ref('')

onMounted(() => {
    fighterPictureURL.value = 'http://127.0.0.1:8000/' + props.fighter.picture
})

function deleteFighter() {
    axios.delete(`/api/v1/fighters/${props.fighter.id}/`)
    .then(response => {
      console.log('Fighter deleted')
      emit('fighter-deleted', props.fighter)
    })
    .catch(error => {
      console.error('Error deleting fighter', error)
    })
}
</script>

<template>
    <div v-if="selectedFighter === fighter" class="selected-fighter">
        <div class="fighter-picture">
            <img v-if="fighter.picture" :src="fighterPictureURL">
            <img v-else src="/images.jpg">
        </div>
        <div class="fighter-information">
            <img src="/trash-icon.png" class="delete-fighter-icon" @click="deleteFighter">
            <h2 v-if="fighter.nickname != ''"> {{ fighter.first_name }} '{{ fighter.nickname }}' {{ fighter.last_name }}</h2>
            <h2 v-else="fighter.nickname"> {{ fighter.first_name }} {{ fighter.last_name }}</h2>
            <h3> Member since : {{ fighter.member_since }}</h3>
            <h3 v-if="fighter.first_tournament"> First tournament : {{ fighter.first_tournament }}</h3>
            <h3 v-if="fighter.first_tournament"> Number of tournament : {{ fighter.tournament_participation }}</h3>
        </diV>
    </div>
    <div v-else class="other-fighter">
        <div class="fighter-information">
            <h2 v-if="fighter.nickname != ''"> {{ fighter.first_name }} '{{ fighter.nickname }}' {{ fighter.last_name }}</h2>
            <h2 v-else="fighter.nickname"> {{ fighter.first_name }} {{ fighter.last_name }}</h2>
        </div>
    </div>
</template>

<style>
.selected-fighter {
    display: inline-flex;
    background-color: #EEE3AF;
    height: 12vw;
    width: 100%;
    color: #3F494B;
    font-weight: bold;
    border-top: 5px solid #3F494B;
    border-bottom: 5px solid #3F494B;
}

.delete-fighter-icon {
    position: absolute;
    top: 2%;
    left: 95.5%;
    margin: 0;
    padding: 0;
    height: 2vw;
}

.delete-fighter-icon:hover {
  cursor: pointer;
}

.selected-fighter {
    position: relative;
}

.fighter-picture img {
    height: 12vw;
    width: auto;
}

.other-fighter {
    margin: auto;
    background-color: #F8F6EC;
    width: 90%;
    color: #3F494B;
}

.fighter-information {
    margin: auto;
}
</style>
