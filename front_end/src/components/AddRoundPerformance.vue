<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const licePositions = ref([])

const resistancesList = ref([('B', 'bad'), ('M', 'medium'), ('G', 'good'), ('LS', 'last standing')])

const props = defineProps({
    fighter: Object,
    round: Object
})

function getLicePositions() {
    axios
        .get('/api/v1/licepositions/')
        .then(response => {
            licePositions.value = response.data
        })
        .catch(error =>
            console.log(error)
        )
}

onMounted(() => {
    getLicePositions()
})

const lice_position = ref()
const first_on_ground = ref()
const resistance = ref()
const TK_solo = ref()
const TK_duo = ref()
const DB_fall = ref()

const addRoundPerformanceData = ref({
    fighterID: props.fighter.id,
    lice_position_position: lice_position,
    roundID: props.round.id,
    first_on_ground: first_on_ground,
    resistance_level: resistance,
    takedown_solo: TK_solo,
    takedown_team: TK_duo,
    double_chute: DB_fall
})

const emit = defineEmits(['round-performance-added'])

function saveNewRoundPerformance() {
    axios
        .post('/api/v1/roundperformances/', addRoundPerformanceData.value)
        .then(response => {
        console.log('Round Performance added', response.data)
        emit('round-performance-added', response.data)
        })
        .catch(error => {
        console.error('Error adding Round Performance', error)
        })
}
</script>

<template>
    <div class="add-round-performance-row">
        <div class="round-performance-cell">
            <h3> {{ props.fighter.first_name }} </h3>
        </div>
        <div class="round-performance-cell">
            <select v-model="lice_position">
                <option v-for="liceposition in licePositions">
                    {{ liceposition.position }}
                </option>
            </select>
        </div>
        <div class="round-performance-cell">
            <input type="checkbox" v-model="first_on_ground">
        </div>
        <div class="round-performance-cell">
            <select v-model="resistance">
                <option v-for="resistance in resistancesList">
                    {{ resistance }}
                </option>
            </select>
        </div>
        <div class="round-performance-cell">
            <input v-model="TK_solo"></input>
        </div>
        <div class="round-performance-cell">
            <input v-model="TK_duo"></input>
        </div>
        <div class="round-performance-cell">
            <input type="checkbox" v-model="DB_fall">
        </div>
        <div class="round-performance-cell">
            <button class="save-round-performance-button" @click="saveNewRoundPerformance">Save</button>
        </div>
    </div>

</template>

<style>
.add-round-performance-row {
    display: flex;
    flex-direction: row;
    align-items: center;
    color: #925040;
}

.add-round-performance-row input {  
    color: #925040;
    border: 1px solid #925040;
    background-color: #d9d9d9;
    width: 2vw;
}

.add-round-performance-row select {  
    color: #925040;
    border: 1px solid #925040; 
    background-color: #d9d9d9;
}

.save-round-performance-button {
    width: 4vw;
    height: 2vw
}
</style>