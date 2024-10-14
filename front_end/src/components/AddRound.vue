<script setup>
import axios from 'axios';
import { ref, onMounted, watch } from 'vue';

const props = defineProps({
    index: Number
})

const fighters = ref([])
const involvedFighters = ref([])
const issue = ref()

const issue_choices = ['victory', 'defeat', 'draw']

const roundData = ref({
    round_rank: props.index,
    fighters_involved: involvedFighters,
    issue: issue
})

const emit = defineEmits(['round-data-update'])

function getFighters() {
    axios
        .get('/api/v1/fighters/')
        .then(response => {
            fighters.value = response.data
        })
        .catch(error =>
            console.log(error)
        )
}

onMounted(() => {
    getFighters()
})

watch(involvedFighters, (newVal) => {
    emit('round-data-update', roundData.value);
});

watch(issue, (newVal) => {
    emit('round-data-update', roundData.value);
});
</script>

<template>
    <div class="vertical-sep-wrapper">
        <div v-if="index > 1" class="vertical-sep"></div>
    </div>
    <div class="added-round">
        <h3 class="round-title">Round {{ index }}</h3>
        <select v-model="involvedFighters" multiple>
            <option v-for="fighter in fighters" :key="fighter.id" :value="fighter.id">
                {{ fighter.first_name }} {{ fighter.last_name }}
            </option>
        </select>
        <div class="detail-section"> <!-- classe définie dans le composant addMatch.vue -->
            <p>Issue</p>
            <select v-model="issue" class="issue-choice">
                <option v-for="choice in issue_choices">
                    {{ choice }}
                </option>
            </select>
        </div>
    </div>
</template>

<style>
.added-round {
    margin: 1vw;
}

.round-title {
    padding: 0;
    margin-bottom: 0.5vw;
}

select[multiple] {
    width: 8vw;
    height: 9vw;
    border: 1px solid #925040;
    background-color: #d9d9d9;
    margin: 0.5vw;
    color: #925040
}

.issue-choice {
    width: 5vw;
    height: 1.5vw;
    border: 1px solid #925040;
    background-color: #d9d9d9;
    margin-left: 0.5vw;
    color: #925040
}

.vertical-sep-wrapper {
    display: flex;
    align-items: center;
}    

.vertical-sep {
    border-left: 1px solid #925040;
    height: 12vw;
}
</style>