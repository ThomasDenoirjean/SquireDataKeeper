<script setup>
import { ref, computed, watch } from 'vue';
import axios from 'axios';
import addmatch from './AddMatch.vue';

const name = ref()
const date = ref()
const localization = ref()
const rank = ref()
const number_of_match = ref()
const matchs = ref([])

const emit = defineEmits('tournament-created')

const tournamentData = computed(() => ({
    name: name.value,
    date: date.value,
    localization: localization.value,
    ranking: rank.value,
    number_of_match: number_of_match.value,
    matchs: matchs.value
}));

function refreshTournamentData(newData) {
    matchs.value[newData.match_rank - 1] = newData
}

function saveNewTournament() {
    console.log('save new tournament')

    let data = tournamentData.value

    axios
        .post('/api/v1/tournaments/', data)
        .then(response => {
            console.log('response', response)
            console.log('response.data', response.data)            
            emit('tournament-created', response.data)
        })
        .catch(error =>
            console.log(error)
        )
    
    resetTournamentData() 
}

function resetTournamentData() {
    name.value = '';
    date.value = '';
    localization.value = '';
    rank.value = null;
    number_of_match.value = null;
    matchs.value = [];
}

watch(number_of_match, (newVal) => {
    while (matchs.value.length > newVal) {
        matchs.value.pop();
    }
    while (matchs.value.length < newVal) {
        matchs.value.push({});
    }
});
</script>

<template>
    <div class="add-tournament-wrapper">
        <h1 class="add-tournament-title">Add a new tournament</h1>
        <div class="inputs-wrapper">
            <div class="input">
                <input v-model="name" placeholder="name" class="new-tournament-inputs">
            </div>
            <div class="input">
                <input v-model="date" placeholder="date" class="new-tournament-inputs"  type="date">
            </div>
            <div class="input">
                <input v-model="localization" placeholder="localization" class="new-tournament-inputs">
            </div>
            <div class="input">
                <input v-model="rank" placeholder="rank" class="new-tournament-inputs" type="number">
            </div>
            <div class="input">
                <input v-model="number_of_match" placeholder="number_of_match" class="new-tournament-inputs" type="number">
            </div>
        </div>
        <div class="match-list">
            <div v-if="tournamentData.number_of_match" v-for="n in tournamentData.number_of_match" :key="n">
                <addmatch :index="n" @match-data-update="refreshTournamentData"></addmatch>
            </div>
        </div>
        <button class="save-tournament-button" @click="saveNewTournament">Save tournament</button>
    </div>
</template>

<style>
.add-tournament-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #925040;
}

.add-tournament-title {
    text-align: center;
}

.input {
    display: inline;
}

.new-tournament-inputs {
    margin: 1vw;
    border: solid #925040;
    background-color: #d9d9d9;
    color: #925040;
}

.match-list {
    width: 90vw;
}

::placeholder {
    opacity: 1;
    color: #925040;
}

.save-tournament-button {
    margin-top: 1vw;
    padding: 1vw;
    border-radius: 25px;
}
</style>