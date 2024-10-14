<script setup>
import axios from 'axios';

const props = defineProps({
    roundPerformance: Object,
    fighterFirstName: String
})

const emit = defineEmits(['round-performance-deleted'])

function deleteRoundPerformance() {
    axios.delete(`/api/v1/roundperformances/${props.roundPerformance.id}/`)
    .then(response => {
      console.log('round performance deleted')
      emit('round-performance-deleted', props.roundPerformance.id)
    })
    .catch(error => {
      console.error('Error deleting round performance', error)
    })
}
</script>

<template>
    <div class="round-performance">
        <div class="round-performance-cell">
            <h3> {{ fighterFirstName }} </h3>
        </div>
        <div class="round-performance-cell">
            <h3> {{ roundPerformance.lice_position_position }}</h3>
        </div>
        <div class="round-performance-cell">
            <h3 v-if="roundPerformance.first_on_groun">Yes</h3>
            <h3 v-else>No</h3>
        </div>
        <div class="round-performance-cell">
            <h3 v-if="roundPerformance.resistance_level === 'B'"> Bad </h3>
            <h3 v-else-if="roundPerformance.resistance_level === 'M'"> Medium </h3>
            <h3 v-if="roundPerformance.resistance_level === 'G'"> Good </h3>
            <h3 v-if="roundPerformance.resistance_level === 'LS'"> Last standing </h3>

        </div>
        <div class="round-performance-cell">
            <h3> {{  roundPerformance.takedown_solo }}</h3>
        </div>
        <div class="round-performance-cell">
            <h3> {{  roundPerformance.takedown_team }}</h3>
        </div>
        <div class="round-performance-cell">
            <h3 v-if="roundPerformance.double_fall">Yes</h3>
            <h3 v-else>No</h3>
        </div>
        <div class="round-performance-cell">
            <img src="/trash-icon.png" class="delete-round-performance-icon" @click="deleteRoundPerformance()">
        </div>
    </div>
</template>

<style>
.round-performance {
    display: flex;
    flex-direction: row;
    width: 90vw;
    margin: auto;
    align-items: center;
    color: #3F494B;
}

.delete-round-performance-icon {
    height: 2vw;
}

.delete-round-performance-icon:hover {
  cursor: pointer;
}

</style>