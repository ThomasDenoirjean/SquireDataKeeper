<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import addroundperformance from './AddRoundPerformance.vue';
import roundperformance from './RoundPerformance.vue';

const props = defineProps({
    round: Object,
})

const roundPerformanceData = ref([])

const isFighterInPerformance = (fighterId) => {
    return roundPerformanceData.value.some(performance => performance.fighterID === fighterId);
};

function getRoundPerformance() {
    console.log('fetching round performance')


    axios
        .get('/api/v1/roundperformances/?id=' + props.round.id)
        .then(response => {
            if (response.data) {
                console.log('response.data DE LA ROUNDPERFORMANCE', response.data)
                roundPerformanceData.value = response.data
            } else {
                console.log('no response.data')
            }
        })
        .catch(error => {
            console.log(error);
        });

}

onMounted(() => {
    getRoundPerformance();
})

function removeRoundPerformanceFromList(id) {
    const index = roundPerformanceData.value.findIndex(performance => performance.id === id);
    if (index !== -1) {
        roundPerformanceData.value.splice(index, 1);
    }
}

function addRoundPerformanceToList(data) {
    roundPerformanceData.value.push(data)
}
</script>

<template>
    <div class="round-wrapper">
        <div class="col-names">
            <div class="round-performance-cell">
                <h1 class="round-rank">Round {{ round.round_rank }}</h1>
                <h2 v-if="round.issue === 'V'" class="round-issue">Victory</h2>
                <h2 v-else-if="round.issue === 'DR'" class="round-issue">Draw</h2>
                <h2 v-else-if="round.issue === 'DE'" class="round-issue">Defeat</h2>
            </div>
            <div class="round-performance-cell">
                <h2>Lice Position</h2>
            </div>
            <div class="round-performance-cell">
                <h2>First on ground</h2>
            </div>
            <div class="round-performance-cell">
                <h2>Resistance</h2>
            </div>
            <div class="round-performance-cell">
                <h2>TK solo</h2>
            </div>
            <div class="round-performance-cell">
                <h2>TK duo</h2>
            </div>
            <div class="round-performance-cell">
                <h2>DB fall</h2>
            </div>
            <div class="round-performance-cell">
            </div>
        </div>
        <div class="round-performance-wrapper">
            <div v-for="fighter in round.fighters_involved" :key="fighter.id">
                <div v-if="roundPerformanceData && roundPerformanceData.length > 0">
                    <div v-for="roundPerformance in roundPerformanceData" :key="roundPerformance.id">
                        <div v-if="fighter.id === roundPerformance.fighterID">
                            <roundperformance :roundPerformance="roundPerformance"
                                :fighterFirstName="fighter.first_name"
                                @round-performance-deleted="removeRoundPerformanceFromList">
                            </roundperformance>
                        </div>
                    </div>
                </div>
                <div v-if="!isFighterInPerformance(fighter.id)">
                    <addroundperformance :fighter="fighter" :round="round" @round-performance-added="addRoundPerformanceToList"></addroundperformance>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.round-wrapper {
    margin-bottom: 1vw;
}

.round-performance-wrapper {
    border: 5px solid #3F494B;
    width: 90vw;
    margin: auto;
}

.col-names {
    display: flex;
    flex-direction: row;
    width: 90vw;
    margin: auto;
    align-items: center;
}

.round-performance-cell {
    width: 12vw;
}

.round-rank {
    margin: 0;
    padding: 0;
}

.round-issue {
    margin: 0;
    padding: 0;
    font-style: italic;
}
</style>