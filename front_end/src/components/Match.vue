<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import round from './Round.vue';

const rounds_array = ref([])

const props = defineProps({
    match: Object,
})

function getRounds() {
    for (let i = 0; i < props.match.rounds.length; i++) {
        let id = props.match.rounds[i]
        console.log('props.match.rounds[i]', props.match.rounds[i])
        axios
            .get('/api/v1/rounds/?id=' + id)
            .then(response => {
                console.log('Rounds : response.data', response.data)
                rounds_array.value.push(response.data)
            })
            .catch(error =>
                console.log(error)
            )
    }
}

const showRounds = ref(false)

onMounted(() => {
    getRounds();
})
</script>

<template>
    <div class="match-wrapper">
        <div class="match-result" @click="showRounds = !showRounds">
            <h2>Match {{ match.match_rank }} - {{ match.enemyteam.name }}</h2>
            <h2 v-if="match.victory" class="match-issue-victory">Victory</h2>
            <h2 v-else class="match-issue-defeat">Defeat</h2>
        </div>
        <div v-if="showRounds" class="rounds-list">
            <round v-for="(round, index) in rounds_array" :round="round"></round>
        </div>
    </div>
</template>

<style>
.match-result {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.match-issue-victory {
    margin-left: 1vw;
    margin-right: 1vw;
    background-color: #3F494B;
    color: #F8F6EC;
    border-radius: 20px;
    width: 7vw;
    height: 2vw;
}

.match-issue-defeat {
    margin-left: 1vw;
    margin-right: 1vw;
    background-color: #F8F6EC;
    color: #3F494B;
    border: 3px solid #3F494B;
    border-radius: 20px;
    width: 7vw;
    height: 2vw;
}

.match-wrapper {
    margin-top: 1vw;
    margin-bottom: 3vw;
}
</style>