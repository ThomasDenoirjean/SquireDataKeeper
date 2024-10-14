<script setup>
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';
import addround from './AddRound.vue'

const ennemyTeams = ref([])
const victory = ref(false)
const enemyFought = ref()
const rounds = ref([])
const number_of_rounds = ref()

const props = defineProps({
    index: Number
})

const matchData = ref({
    enemyteam: enemyFought,
    match_rank: props.index,
    number_of_rounds: number_of_rounds,
    victory: victory,
    rounds: rounds
})

const emit = defineEmits(['match-data-update'])

function getEnnemyTeams() {
    axios
        .get('/api/v1/ennemyteams/')
        .then(response => {
            ennemyTeams.value = response.data
        })
        .catch(error =>
            console.log(error)
        )
}

onMounted(() => {
    getEnnemyTeams()
})

function refreshRoundData(newData) {
    rounds.value[newData.round_rank - 1] = newData
}

watch(enemyFought, (newVal) => {
    emit('match-data-update', matchData.value);
});

watch(number_of_rounds, (newVal) => {
    emit('match-data-update', matchData.value);
});

watch(victory, (newVal) => {
    emit('match-data-update', matchData.value);
});
</script>

<template>
    <div class="added-match">
        <div class="match">
            <h1> Match {{ props.index }}</h1>
            <div class="detail-section">
                <p>Opponents</p>
                <select v-model="enemyFought" class="opponent-choice">
                    <option v-for="ennemy in ennemyTeams" :key="ennemy.id">{{ ennemy.name }}</option>
                </select>
            </div>
            <div class="detail-section">
                <p>Number of rounds</p>
                <input v-model="number_of_rounds">
            </div>
            <div class="detail-section">
                <h3> Victory </h3>
                <input type="checkbox" v-model="victory" class="victory-checkbox">
            </div>
        </div>
        <div class="round">
            <addround v-if="number_of_rounds" v-for="roundIndex in parseInt(number_of_rounds)" :index="roundIndex"
                @round-data-update="refreshRoundData" :key="roundIndex">
            </addround>
        </div>
    </div>
</template>

<style>
.added-match {
    margin: 1vw;
    display: inline-flex;
    align-items: center;
    border: 5px solid #925040;
    border-radius: 25px;
}

.added-match input {
    border: 1px solid #925040;
    background-color: #d9d9d9;
    width: 2vw;
    margin: 0.5vw;
    color: #925040;
}

.match {
    padding: 1vw;
}

.round {
    margin-left: 1vw;
    display: inline-flex;
}

.opponent-choice {
    width: 10vw;
    margin-left: 0.5vw;
    border: 1px solid #925040;
    background-color: #d9d9d9;
    color: #925040;
}

.victory-checkbox {
    margin: 0 !important; 
}

.detail-section {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}

.detail-section p,
.detail-section h3 {
    margin: 0;
}
</style>