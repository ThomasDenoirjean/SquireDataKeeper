<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import tournament from '../components/Tournament.vue';
import addtournament from '../components/AddTournament.vue';

const tournaments_array = ref([])

function getTournaments() {
  axios
    .get('/api/v1/tournaments/')
    .then(response => {
      tournaments_array.value = response.data
    })
    .catch(error => {
      console.error('Failed to fetch tournaments:', error);
    });
}

function removeTournamentFromList(index) {
  tournaments_array.value.splice(index, 1)
}

function addTournamentToList(newTournamentID) {
  axios
    .get(`/api/v1/tournaments/${newTournamentID}/`)
    .then(response => {
      tournaments_array.value.push(response.data)
    })
    .catch(error => {
      console.error('Failed to add tournament:', error);
    });
}

onMounted(() => {
  getTournaments();
})
</script>

<template>
  <div class="tournament-list">
    <tournament v-for="(tournament, index) in tournaments_array" :tournament="tournament" :index="index"
      @tournament-deleted="removeTournamentFromList(index)" :key="tournament.id">
    </tournament>
    <hr v-if="tournaments_array.length > 0" class="tournament-separation">
    <div class="add-tournament-wrapper">
      <addtournament @tournament-created="addTournamentToList"></addtournament>
    </div>
  </div>
</template>

<style>
.tournament-list {
  border: 3px solid #3F494B;
  margin: 1vw;
  text-align: center;
  color: #3F494B;
  border-radius: 20px;
}

.add-tournament-wrapper {
  margin-bottom: 1vw;
}
</style>