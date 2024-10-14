<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import match from './Match.vue';

const matchs_array = ref([])

const props = defineProps({
    tournament: Object,
    index: Number
})

const show_details = ref(false)

function getMatchs() {
    for (let i = 0; i < props.tournament.matchs.length; i++) {
        let id = props.tournament.matchs[i]
        console.log('props.tournament.matchs[i]', props.tournament.matchs[i])
        axios
            .get('/api/v1/matchs/?id=' + id)
            .then(response => {
                console.log('response.data', response.data)
                matchs_array.value.push(response.data)
            })
            .catch(error =>
                console.log(error)
            )
    }
}

onMounted(() => {
    getMatchs();
})

function updateShowDetails() {
    show_details.value = !show_details.value
}

const emit = defineEmits(['tournament-deleted'])

function deleteTournament() {
    axios
        .delete(`/api/v1/tournaments/${props.tournament.id}/`)
        .then(response => {
            console.log('response', response)
            emit('tournament-deleted', props.index)
        })
        .catch(error =>
            console.log(error)
        )   
}
</script>

<template>
    <hr v-if="props.index > 0" class="tournament-separation">
    <div class="tournament-wrapper">
        <div class="title-section" @click="updateShowDetails">
            <h2 v-if="tournament.ranking === 1" :class="{ 'detailed-tournament': show_details }">
            Tournoi de {{ tournament.name }} - {{ tournament.date }} - {{ tournament.ranking }}er </h2>
        <h2 v-else :class="{ 'detailed-tournament': show_details }">
            Tournoi de {{ tournament.name }} - {{ tournament.date }} - {{ tournament.ranking }}ème </h2>
        <img v-if="show_details" src="/trash-icon.png" class="delete-tournament-icon" @click="deleteTournament">
        </div>
        <div v-if="show_details">
            <match v-for="(match, index) in matchs_array.sort((a, b) => a.match_rank - b.match_rank)" :match="match"></match>
        </div>
    </div>
</template>

<style>
.tournament-separation {
    width: 90%;
    color: #3F494B;
}

.title-section {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.detailed-tournament {
    font-size: 2.5em;
}

.delete-tournament-icon {
    margin-left: 1vw;
    width: 3vw;
    height: 3.5vw;
}

.delete-tournament-icon:hover {
    cursor: pointer;
}
</style>